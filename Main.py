#Main.py

from Utility import movie_data, filter_movies_by_genre, sort_movies_by_rating, sort_movies_by_date, display_movies

print("Let's find a movie to watch!")

#Load movie data from the CSV file
movies = movie_data()

while True:
    #Display Genre Menu
    print("\nPlease choose a genre:")
    print("1. Action")
    print("2. Comedy")
    print("3. Drama")
    print("4. Mystery/Thriller")
    print("5. Horror")
    genre_choice = input("Enter the number of your choice: ")

    #Handle invalid genre input and map the user's choice to the genre
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

    #Filter movies by the user-selected genre
    filtered_movies = filter_movies_by_genre(movies, selected_genre)

    if len(filtered_movies) == 0:
        print("No movies found for genre: " + selected_genre + ". Try another genre.")
        continue

    #Display Sort Option Menu
    print("\nPlease choose an option:")
    print("1. Top Rated Movies")
    print("2. Most Recent Movies")
    sort_choice = input("Enter the number of your choice: ")

    #Sort based on the user's choice
    if sort_choice == '1':  # Sort by top-rated
        sorted_movies = sort_movies_by_rating(filtered_movies)
    elif sort_choice == '2':  # Sort by most recent release date
        sorted_movies = sort_movies_by_date(filtered_movies)
    else:
        print("Invalid choice! Please try again.")
        continue

    #Display the top two movies based on user-selected Sort Option
    print("\nHere are the top two movies based on your selection:")
    display_movies(sorted_movies[:2])

    #Ask user if they want to search again, otherwise exit
    again = input("\nWould you like to search again? (Y or N): ")
    if again.upper() != 'Y':
        print("Thank you for using our Movie Recommendation program!")
        break
