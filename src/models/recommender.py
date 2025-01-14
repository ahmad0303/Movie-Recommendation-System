from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
nltk.download('stopwords')

def prepare_tags(data):
    from nltk.stem.porter import PorterStemmer
    ps = PorterStemmer()
    
    def stem(text):
        if isinstance(text, list):
            text = " ".join(text)  # Convert list to string
        return " ".join([ps.stem(i) for i in text.split()])
    
    data['tags'] = data['tags'].apply(stem)
    return data

def vectorize_tags(data):
    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(data['tags']).toarray()
    return vectors, cv.get_feature_names_out()

def calculate_similarity(vectors):
    return cosine_similarity(vectors)

def recommend(movie, data, similarity_matrix):
    movie_index = data[data['title'] == movie].index[0]
    distances = similarity_matrix[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [data.iloc[i[0]].title for i in movies_list]
