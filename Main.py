import Utility

print("Let's find a movie to watch!")

def display_genre_menu():
    print("\nChoose a Genre:")
    print("1. Action")
    print("2. Comedy")
    print("3. Drama")
    print("4. Mystery/Thriller")
    print("5. Horror")
    choice = input("Enter the number of your choice: ")
    return choice

def display_score_menu():
    print("\nChoose an Option:")
    print("1. Most Recent Movies")
    print("2. Top Rated Movies")
    choice = input("Enter the number of your choice: ")
    return choice

def main():
    movies = Utility.import_movies()

    genre_choice = display_genre_menu()

    if genre_choice == "1":
        genre = "Action"
    elif genre_choice == "2":
        genre = "Comedy"
    elif genre_choice == "3":
        genre = "Drama"
    elif genre_choice == "4":
        genre = "Mystery/Thriller"
    elif genre_choice == "5":
        genre = "Horror"
    else:
        print("Invalid choice. Exiting program.")
        return

    score_choice = display_score_menu()

    if score_choice == "1":
        # Get the two most recent movies
        recent_movies = Utility.get_two_most_recent_movies(movies, genre)
        print("\nMost Recent Movies:")
        Utility.display_movies(recent_movies)

    elif score_choice == "2":
        # Get the two top-rated movies
        top_movies = Utility.get_top_two_movies_by_score(movies, genre)
        print("\nTop Rated Movies:")
        Utility.display_movies(top_movies)

    else:
        print("Invalid choice. Exiting program.")

if __name__ == "__main__":
    main()
