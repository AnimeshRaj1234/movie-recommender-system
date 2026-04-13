# 🎬 Movie Recommendation System

A content-based movie recommendation system built using Machine Learning that suggests similar movies based on user input.

---

## 📌 Project Overview

This project recommends movies similar to a given movie using features such as:

* Genres
* Keywords
* Cast
* Crew (Director)
* Overview

It uses text vectorization and similarity measures to find the closest matches.

---

## 🚀 Features

* Recommend top 5 similar movies
* Uses real-world dataset (TMDB 5000)
* Fast recommendations using precomputed similarity
* Clean and modular code structure
* Optional Streamlit UI

---

## 🧠 Machine Learning Concepts Used

* Text Vectorization (CountVectorizer)
* Cosine Similarity
* Feature Engineering
* NLP Basics

---

## 📂 Dataset

Dataset used:

* TMDB 5000 Movies Dataset

Files:

* `tmdb_5000_movies.csv`
* `tmdb_5000_credits.csv`

---

## 🧱 Project Structure

```
movie-recommender/
│
├── data/
│   ├── tmdb_5000_movies.csv
│   ├── tmdb_5000_credits.csv
│
├── model/
│   ├── movie_list.pkl
│   ├── similarity.pkl
│
├── main.py
├── app.py
├── README.md
```

---

## ⚙️ Installation

1. Clone the repository:

```
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender
```

2. Install dependencies:

```
pip install pandas numpy scikit-learn streamlit
```

---

## ▶️ How to Run

### Step 1: Generate Model Files

```
python main.py
```

This will create:

* `movie_list.pkl`
* `similarity.pkl`

---

### Step 2: Run the App

```
streamlit run app.py
```

---

## 🧪 Example

Input:

```
Avatar
```

Output:

```
Guardians of the Galaxy
John Carter
Star Trek
...
```

---

## 🧠 How It Works

1. Merge movie and credit datasets
2. Extract important features
3. Create a combined "tags" column
4. Convert text into vectors using CountVectorizer
5. Compute similarity using cosine similarity
6. Recommend movies based on highest similarity scores

---

## 💾 Why Pickle (.pkl) is Used

* Saves processed data and similarity matrix
* Avoids recomputation
* Improves performance

---

## 🔮 Future Improvements

* Add movie posters using TMDB API
* Use TF-IDF for better accuracy
* Add user-based (collaborative) filtering
* Deploy on cloud (Render / Streamlit Cloud)
* Add search autocomplete

---

## 📚 Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit

---

## 👨‍💻 Author

Animesh (Avi)

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
