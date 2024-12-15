# Utility.py

import csv

#Import and read movie data from Data_RottenTomatoes_2024Dec11.csv
def movie_data():
    movies = []
    with open('Data_RottenTomatoes_2024Dec11.csv', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            movie_name = row[0]
            genre = row[1]
            release_date = row[2]
            rating = row[3]
            tomatometer = row[4]
            where_to_watch = row[5]
            movie = [movie_name, genre, release_date, rating, tomatometer, where_to_watch]
            movies.append(movie)
    return movies

#Filter movies by the user-selected genre
def filter_movies_by_genre(movies, genre):
    filtered_movies = []
    for movie in movies:
        if movie[1].lower() == genre.lower():
            filtered_movies.append(movie)
    return filtered_movies

#Sort movies by Tomatometer score
def sort_movies_by_rating(movies):
    for i in range(len(movies)):
        for j in range(i + 1, len(movies)):
            if float(movies[i][4]) < float(movies[j][4]):
                movies[i], movies[j] = movies[j], movies[i]
    return movies

#Sort movies by most recent release date
def sort_movies_by_date(movies):
    for i in range(len(movies)):
        for j in range(i + 1, len(movies)):
            if movies[i][2] < movies[j][2]:
                movies[i], movies[j] = movies[j], movies[i]
    return movies

#Display movie details and add line separation for readability
def display_movies(movies):
    for movie in movies:
        print("Movie Name: " + movie[0])
        print("Genre: " + movie[1])
        print("Release Date: " + movie[2])
        print("Rating: " + movie[3])
        print("Tomatometer Score: " + str(movie[4]) + "%")
        print("Where to Watch: " + movie[5])
        print("-" * 40)
