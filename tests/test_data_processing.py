import pytest
import pandas as pd
from src.data.preprocess import load_data

def test_load_data():
    movies, credits = load_data('./data/raw/tmdb_5000_movies.csv', './data/raw/tmdb_5000_credits.csv')
    assert not movies.empty
    assert not credits.empty


