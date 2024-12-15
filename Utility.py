# Utility.py

import csv

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
            #Compare Tomatometer scores (index 4) and swap if necessary
            if float(movies[i][4]) < float(movies[j][4]):
                #Swap movies[i] and movies[j]
                movies[i], movies[j] = movies[j], movies[i]
    return movies

#Sort movies by most recent release date
def sort_movies_by_date(movies):
    for i in range(len(movies)):
        for j in range(i + 1, len(movies)):
            # Compare release dates (index 2) and swap if necessary
            if movies[i][2] < movies[j][2]:  # Lexicographical comparison works for 'YYYY-MM-DD'
                # Swap movies[i] and movies[j]
                movies[i], movies[j] = movies[j], movies[i]
    return movies
