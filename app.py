import streamlit as st
import pickle
import pandas as pd
import requests
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv('API_KEY')

# Function to fetch the poster of a movie using the TMDB API
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    else:
        st.error("Failed to fetch movie poster.")
        return None

# Function to recommend movies based on similarity
def recommended(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movie_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].id  # Get movie ID
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))  # Fetch the poster

    return recommended_movies, recommended_movie_posters

# Load the movie data and similarity matrix
movies_dict = pickle.load(open('data/processed/movies_dict.pkl', 'rb'))
similarity = pickle.load(open('data/processed/similarity.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Streamlit UI
st.title("Movie Recommendation System")

selected_movie_name = st.selectbox(
    "Select a movie to get recommendations:",
    movies['title'].values
)

if st.button('Show Recommendations'):
    try:
        names, posters = recommended(selected_movie_name)

        # Display the recommendations
        col1, col2, col3, col4, col5 = st.columns(5)

        for idx, col in enumerate([col1, col2, col3, col4, col5]):
            with col:
                st.text(names[idx])
                if posters[idx]:  # Ensure the poster exists
                    st.image(posters[idx], use_container_width=True)
                else:
                    st.text("No poster available")

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
 