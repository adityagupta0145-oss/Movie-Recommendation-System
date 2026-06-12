import pickle
import streamlit as st

from src.recommend import recommend


movie_data = pickle.load(
    open(
        "models/movie_list.pkl",
        "rb"
    )
)

movie_names = (
    movie_data["title"]
    .values
)

st.set_page_config(
    page_title="Movie Recommendation"
)

st.title(
    "Movie Recommendation System"
)

selected_movie = st.selectbox(
    "Select Movie",
    movie_names
)

if st.button(
    "Recommend"
):

    movies = recommend(
        selected_movie
    )

    st.subheader(
        "Recommended Movies"
    )

    for m in movies:

        st.write(
             m
        )