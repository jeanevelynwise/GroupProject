#Main.py

import csv
from Utility_2 import filter_movies_by_genre, sort_movies_by_rating, sort_movies_by_date

print("Let's find a movie to watch!")

def display_menu():
    print("Please choose a genre:")
    print("1. Action")
    print("2. Comedy")
    print("3. Drama")
    print("4. Mystery/Thriller")
    print("5. Horror")

def display_sort_menu():
    print("Please choose an option:")
    print("1. Top Rated Movies")
    print("2. Most Recent Movies")

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

def display_movies(movies):
    for movie in movies:
        print("Movie Name: " + movie[0])
        print("Genre: " + movie[1])
        print("Release Date: " + movie[2])
        print("Rating: " + movie[3])
        print("Tomatometer Score: " + str(movie[4]) + "%")
        print("Where to Watch: " + movie[5])
        print("-" * 40)

#Load movie data from the CSV file
movies = movie_data()

while True:
    display_menu()
    genre_choice = input("Enter the number of your choice: ")

    # Handle invalid genre input
    if genre_choice == '1':
        selected_genre = 'Action'
    elif genre_choice == '2':
        selected_genre = 'Comedy'
    elif genre_choice == '3':
        selected_genre = 'Drama'
    elif genre_choice == '4':
        selected_genre = 'Mystery/Thriller'
    elif genre_choice == '5':
        selected_genre = 'Horror'
    else:
        print("Invalid choice. Please try again.")
        continue

    # Filter movies by the user-selected genre
    filtered_movies = filter_movies_by_genre(movies, selected_genre)

    if len(filtered_movies) == 0:
        print("No movies found for genre: " + selected_genre + ". Try another genre.")
        continue

    display_sort_menu()
    sort_choice = input("Enter the number corresponding to your sorting choice: ")

    if sort_choice == '1':  #Sort by top-rated
        sorted_movies = sort_movies_by_rating(filtered_movies)
    elif sort_choice == '2':  #Sort by most recent release date
        sorted_movies = sort_movies_by_date(filtered_movies)
    else:
        print("Invalid choice! Please try again.")
        continue

    #Display the top two movies
    print("\nHere are the top two movies based on your selection:")
    display_movies(sorted_movies[:2])

    #Ask user if they want to search again, otherwise exit
    again = input("\nWould you like to search again? (Y or N): ")
    if again.upper() != 'Y':
        print("Thank you for using our Movie Recommendation program!")
        break
