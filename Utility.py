import csv

def import_movies():
    movies = []
    # Open CSV file and read movies
    with open("Data_RottenTomatoes_2024Dec11.csv", mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            movie = [row[0], row[1], row[2], row[3], int(row[4]), row[5]]
            # Movie Name, Genre, Release Date, Rating, Tomatometer Score, Where to Watch
            movies.append(movie)
    return movies

def get_two_most_recent_movies(movies, genre):
    genre_movies = []
    for movie in movies:
        if movie[1] == genre:
            genre_movies.append(movie)

    # Sort movies by release date (strings in YYYY-MM-DD format can be compared directly)
    for i in range(len(genre_movies)):
        for j in range(i + 1, len(genre_movies)):
            if genre_movies[i][2] < genre_movies[j][2]:
                temp = genre_movies[i]
                genre_movies[i] = genre_movies[j]
                genre_movies[j] = temp

    # Return top two movies
    return genre_movies[:2]

def get_top_two_movies_by_score(movies, genre):
    genre_movies = []
    for movie in movies:
        if movie[1] == genre:
            genre_movies.append(movie)

    top_two = []
    while len(top_two) < 2 and len(genre_movies) > 0:
        max_score = genre_movies[0][4]
        max_index = 0
        for i in range(1, len(genre_movies)):
            if genre_movies[i][4] > max_score:
                max_score = genre_movies[i][4]
                max_index = i
        top_two.append(genre_movies.pop(max_index))
    return top_two

def display_movies(movies):
    for movie in movies:
        print("Movie Name: " + movie[0])
        print("Genre: " + movie[1])
        print("Release Date: " + movie[2])
        print("Rating: " + movie[3])
        print("Tomatometer Score: " + str(movie[4]) + "%")
        print("Where to Watch: " + movie[5])
        print("-" * 40)
