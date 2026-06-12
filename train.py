import pandas as pd
import pickle

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load dataset
movies = pd.read_csv(
    "../data/movies.csv"
)

print("Dataset Loaded")

# Check columns
print(movies.columns)

# Remove missing values
movies["genres"] = (
    movies["genres"]
    .fillna("")
    .astype(str)
)

# Remove rows where genres empty
movies = movies[
    movies["genres"] != ""
]

print("Rows:", len(movies))

# Vectorization
cv = CountVectorizer(
    max_features=5000
)

vectors = cv.fit_transform(
    movies["genres"]
)

print("Vector Shape:", vectors.shape)

# Similarity
similarity = cosine_similarity(
    vectors
)

# Save
pickle.dump(
    movies,
    open(
        "../models/movie_list.pkl",
        "wb"
    )
)

pickle.dump(
    similarity,
    open(
        "../models/similarity.pkl",
        "wb"
    )
)

print("Training completed")