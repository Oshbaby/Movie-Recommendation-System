import streamlit as st  
import pickle
import pandas as pd
import requests

# Load Data
with open("movie_list.pkl", 'rb') as f:
    movies = pd.read_pickle(f)
with open("similarity.pkl", 'rb') as f:
    similarity = pickle.load(f)

movie_list = movies['title'].values

# Streamlit Page Config
st.set_page_config(page_title="Movie Recommender", layout="wide")

# Custom CSS for Styling
st.markdown(
    """
    <style>
        body {
            background-color: #0e1117;
            color: white;
            font-family: 'Arial', sans-serif;
        }
        .title {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            color: #ff4b4b;
        }
        .dropdown {
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 20px;
        }
        .recommend-btn {
            background-color: #ff4b4b;
            color: white;
            font-size: 18px;
            border-radius: 10px;
            padding: 10px 20px;
            width: 100%;
        }
        .movie-card {
            border-radius: 15px;
            padding: 10px;
            text-align: center;
            background: rgba(255, 255, 255, 0.1);
            transition: 0.3s;
        }
        .movie-card:hover {
            background: rgba(255, 255, 255, 0.2);
        }
        img {
            border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title with Styling
st.markdown("<div class='title'>🎬 Movie Recommender System 🍿</div>", unsafe_allow_html=True)

# Movie Selection Dropdown
selectvalue = st.selectbox("Select a Movie:", movie_list, key="movie_select")

# Function to Fetch Movie Posters
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=d5a816607e20854724cc4415f7ce38a1"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        poster_path = data.get('poster_path', '')  
        if poster_path:
            return f"http://image.tmdb.org/t/p/w500{poster_path}"
    return None    

# Function to Get Movie Recommendations
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommend_movie = []
    recommend_poster = []

    for i in distances[1:6]:  # Get top 5 recommendations
        movie_id = movies.iloc[i[0]]['movie_id']
        recommend_movie.append(movies.iloc[i[0]]['title'])
        recommend_poster.append(fetch_poster(movie_id))

    return recommend_movie, recommend_poster

# Button to Show Recommendations
if st.button("🎥 Show Recommendations", key="recommend_btn"):
    movie_names, movie_posters = recommend(selectvalue)

    st.markdown("### Recommended Movies:")
    cols = st.columns(5)  # Create 5 columns for display
    
    for col, name, poster in zip(cols, movie_names, movie_posters):
        with col:
            st.markdown(f"<div class='movie-card'>", unsafe_allow_html=True)
            st.text(name)
            if poster:
                st.image(poster, use_column_width=True)
            else:
                st.text("No Image Available")
            st.markdown("</div>", unsafe_allow_html=True)
