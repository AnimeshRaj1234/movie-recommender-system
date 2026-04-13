# 🎬 Movie Recommender System

A content-based Movie Recommender System built using **Machine Learning** and deployed using **Streamlit**. This system suggests similar movies based on user selection and displays detailed information using the TMDB API.

---

## 🚀 Features

* 🎯 Recommend top 5 similar movies
* 🧠 Content-based filtering using cosine similarity
* 🎬 Fetch movie posters dynamically via TMDB API
* 📊 Displays:

  * Movie title
  * Rating ⭐
  * Release year 📅
  * Genres 🎭
  * Overview 📝
* ⚡ Interactive UI using Streamlit

---

## 🧠 How It Works

### 1. Data Preprocessing

* Datasets used:

  * TMDB 5000 Movies
  * TMDB 5000 Credits
* Merged datasets on movie ID
* Extracted important features:

  * Genres
  * Keywords
  * Cast (top 3 actors)
  * Director
  * Overview

### 2. Feature Engineering

* Converted JSON-like columns into lists
* Removed spaces for consistency
* Created a **tags column** combining all features

### 3. Vectorization

* Used **CountVectorizer (Bag of Words)**
* Limited to 5000 features
* Removed English stop words

### 4. Similarity Calculation

* Used **Cosine Similarity** to measure similarity between movies

### 5. Model Storage

* Saved:

  * `movie_list.pkl`
  * `similarity.pkl`

---

## 🖥️ Tech Stack

* Python 🐍
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* TMDB API

---

## 📁 Project Structure

```
movie-recommender-system/
│
├── app.py                  # Streamlit app (UI + API)
├── main.py                 # Model building & preprocessing
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
├── .gitignore              # Ignored files
│
├── data/                   # Dataset (not included)
├── model/                  # Trained model files (not included)
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/AnimeshRaj1234/movie-recommender-system.git
cd movie-recommender-system
```

---

### 2️⃣ Create virtual environment (optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Add Dataset

Download TMDB datasets and place them inside:

```
data/
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
```

---

### 5️⃣ Train the Model

```bash
python main.py
```

This will generate:

```
model/
├── movie_list.pkl
├── similarity.pkl
```

---

### 6️⃣ Add API Key

Create a `.env` file:

```
API_KEY=your_tmdb_api_key_here
```

Get your API key from: https://www.themoviedb.org/

---

### 7️⃣ Run the App

```bash
streamlit run app.py
```

---

## 📸 Screenshots

* Movie selection dropdown
* Selected movie details
* Recommended movies with posters

---

## 🔐 Environment Variables

| Variable | Description  |
| -------- | ------------ |
| API_KEY  | TMDB API Key |

---

## 🚫 Important Notes

* Dataset (`data/`) is not included due to size
* Model files (`.pkl`) are not included
* Virtual environment is ignored

---

## 💡 Future Improvements

* 🔍 Search-based recommendations
* 🎥 Trailer integration
* 🤖 Hybrid recommendation system
* ⭐ User ratings & personalization

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork and improve.

---

## 📬 Contact

**Animesh Raj**

* GitHub: https://github.com/AnimeshRaj1234

---

## 🌐 Live Demo

👉 https://movie-recommender-system-gy3dvs7gwbvwgosdwuwrm8.streamlit.app/

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
