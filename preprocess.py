import pandas as pd
def load_movies():

    movies = pd.read_csv(
         "../data/movies.csv"
    )

    movies["genres"] = (
        movies["genres"]
        .fillna("")
    )

    return movies


if __name__ == "__main__":

    df = load_movies()

    print(df.head())