import streamlit as st  
import pickle
import pandas as pd
import requests

with open("movie_list.pkl", 'rb') as f:
    movies = pd.read_pickle(f)
with open("similarity.pkl", 'rb') as f:
    similarity = pickle.load(f)

    
movie_list= movies['title'].values

st.title("Movie Recommender System")  
selectvalue=st.selectbox("Select movies from dropdown", movie_list)



# Function to fetch movie posters
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=d5a816607e20854724cc4415f7ce38a1" #the key is not important to me so enjoy!
    data = requests.get(url).json()
    poster_path = data.get('poster_path', '')  # Use .get() to prevent KeyError
    if poster_path:
        return "http://image.tmdb.org/t/p/w500/{poster_path}"
    return None  # Return None if no poster is available
    


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommend_movie = []
    recommend_poster = []

    for i in distances[1:6]:  # Get top 5 recommendations
        movie_id = movies.iloc[i[0]]['movie_id']  # Corrected column access
        recommend_movie.append(movies.iloc[i[0]]['title'])
        recommend_poster.append(fetch_poster(movie_id))

    return recommend_movie, recommend_poster


# Button to show recommendations
if st.button("Show Recommend"):
    movie_names, movie_posters = recommend(selectvalue)

    cols = st.columns(5)  # Create 5 columns
    for col, name, poster in zip(cols, movie_names, movie_posters):
        with col:
            st.text(name)
            if poster:  # Check if poster exists
                st.image(poster)
            else:
                st.text("No image available")
            
