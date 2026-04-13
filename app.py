import streamlit as st
import pickle
import pandas as pd
import numpy as np
from dotenv import load_dotenv
import os
import requests
import certifi
import urllib3


# Load data

movies = pickle.load(open('model/movie_list.pkl','rb'))
similarity = pickle.load(open('model/similarity.pkl','rb'))


# env 

load_dotenv()

API_KEY =  os.getenv("API_KEY")

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# poster function

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    
    try:
        response = requests.get(url, verify=certifi.where(), timeout=5)

        if response.status_code != 200:
            print("API Error:", response.status_code)
            return None

        data = response.json()

        poster_path = data.get('poster_path')

        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return None

    except Exception as e:
        print("Error:", e)
        return None


# detail of selected movie

def get_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return None
    
    data = response.json()
    
    return {
        "title": data.get("title"),
        "overview": data.get("overview"),
        "poster": "https://image.tmdb.org/t/p/w500/" + data.get("poster_path") if data.get("poster_path") else None,
        "rating": data.get("vote_average"),
        "year": data.get("release_date", "")[:4],
        "genres": [g['name'] for g in data.get("genres", [])]
    }

# recommend function

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    
    distances = similarity[movie_index]
    
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    recommended_movie_ids = []
    
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movie_ids.append(movies.iloc[i[0]].movie_id)
    
    return recommended_movies, recommended_movie_ids



# UI
st.title("🎬 Movie Recommender System")

selected_movie = st.selectbox(
    "Select a movie",
    movies['title'].values.tolist(),
    index=None,
    placeholder="Select a movie")

# 🚫 If user hasn't selected anything

if selected_movie is None:
    st.warning("⚠️ Please select a movie to see")
    st.stop()   # 🔥 stops execution below

# 🔹 Get selected movie ID

movie_id = movies[movies['title'] == selected_movie].iloc[0].movie_id
    
# 🔹 Get details

details = get_movie_details(movie_id)

# detail is not there
if not details:
    st.error("Failed to fetch movie details.")
    st.stop()
    
# 🔥 SHOW SELECTED MOVIE DETAILS
if details:
    st.markdown("## 🎬 Selected Movie")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        if details['poster']:
            st.image(details['poster'])
    
    with col2:
        st.title(details['title'])
        st.markdown(f"⭐ {details['rating']} | 📅 {details['year']}")
        st.write(", ".join(details['genres']))
        st.write(details['overview'])

# 🔥 SHOW RECOMMENDATIONS BELOW
names, ids = recommend(selected_movie)

st.markdown("## 🎯 Similar Movies")

cols = st.columns(len(names))

for i in range(5):
    with cols[i]:
        poster = fetch_poster(ids[i])
        if poster:
            st.image(poster)
        st.caption(names[i])