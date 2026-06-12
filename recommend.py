import pickle


movies = pickle.load(
    open(
        "models/movie_list.pkl",
        "rb"
    )
)

similarity = pickle.load(
    open(
        "models/similarity.pkl",
        "rb"
    )
)


def recommend(movie_name):

    index = movies[
        movies["title"]
        == movie_name
    ].index[0]

    scores = list(
        enumerate(
            similarity[index]
        )
    )

    scores = sorted(
        scores,
        reverse=True,
        key=lambda x: x[1]
    )

    result = []

    for i in scores[1:6]:

        title = (
            movies
            .iloc[i[0]]
            .title
        )

        result.append(
            title
        )

    return result