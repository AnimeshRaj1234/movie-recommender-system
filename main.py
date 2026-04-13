import pandas as pd
import ast
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import numpy as np

# Load data
movies_data = pd.read_csv("data/tmdb_5000_movies.csv")
credits_data = pd.read_csv("data/tmdb_5000_credits.csv")

# making copy of datasets
movies_raw = movies_data.copy()
credits_raw = credits_data.copy()

#dataset merge
movies_raw = movies_raw.merge(credits_raw,left_on='id', right_on='movie_id')

# Select columns
movies_raw = movies_raw[['movie_id','title_x','overview','genres','keywords','cast','crew']]
movies_raw.rename(columns={'title_x': 'title'}, inplace=True)

# drop nan values
movies_raw.dropna(inplace=True)

# Convert JSON
def convert(text):
    L = []
    for i in ast.literal_eval(text):
        L.append(i['name'])
    return L

movies_raw['genres'] = movies_raw['genres'].apply(convert)
movies_raw['keywords'] = movies_raw['keywords'].apply(convert)
movies_raw['cast'] = movies_raw['cast'].apply(lambda x: convert(x)[:3])

# Director
def fetch_director(text):
    L = []
    for i in ast.literal_eval(text):
        if i['job'] == 'Director':
            L.append(i['name'])
    return L

movies_raw['crew'] = movies_raw['crew'].apply(fetch_director)

# Remove spaces
def clean(x):
    return [i.replace(" ", "") for i in x]

movies_raw['genres'] = movies_raw['genres'].apply(clean)
movies_raw['keywords'] = movies_raw['keywords'].apply(clean)
movies_raw['cast'] = movies_raw['cast'].apply(clean)
movies_raw['crew'] = movies_raw['crew'].apply(clean)

# making copy of clean data for future use

cleaned_data = movies_raw.copy()

# creating list of words
movies_raw['overview'] = movies_raw['overview'].apply(lambda x: x.split())

# Create tags

movies_raw['tags'] = movies_raw['overview'] + movies_raw['genres'] + movies_raw['keywords'] + movies_raw['cast'] + movies_raw['crew']

# creating a new data frame for model training 
new_df = movies_raw[['movie_id','title','tags']]
new_df = new_df.copy()
new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x))

# Vectorization
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(new_df['tags']).toarray()

# Similarity Matrix
similarity = cosine_similarity(vectors)

# Save files
pickle.dump(new_df, open('model/movie_list.pkl', 'wb'))
pickle.dump(similarity, open('model/similarity.pkl', 'wb'))

# Detail func
def get_movie_details(movie):
    data = cleaned_data[cleaned_data['title'] == movie]

    if data.empty:
        return None
    
    movie_data = data.iloc[0]
    
    details = {
        "title": movie_data['title'],
        "overview": movie_data['overview'],
        "genres": movie_data['genres'],
        "cast": movie_data['cast'],
        "director": movie_data['crew']
    }

    return details

# Recommend func

def recommend(movie):
    data = new_df[new_df['title'] == movie]

    if data.empty:
        return ["Movie Not Found"]
    
    movie_index = data.index[0]
    distances = similarity[movie_index]
    
    movies_list = np.argsort(distances)[::-1][1:6]
    
    return [new_df.iloc[i].title for i in movies_list]

# Find Movie Func

def find(movie):
    recs = recommend(movie)
    details = get_movie_details(movie)

    if details is None:
        print("Movie Not Found")
        return []
    
    return details,recs
