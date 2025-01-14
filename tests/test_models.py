from src.models.recommender import calculate_similarity
import numpy as np

def test_calculate_similarity():
    mock_vectors = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    similarity = calculate_similarity(mock_vectors)
    assert similarity.shape == (3, 3)
