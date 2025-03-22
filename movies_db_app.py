MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


def add():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })


def movies_list():
    for movie in movies:
        if len(movies) > 0:
            print(f"Title: {movie['title']}, Director: {movie['director']}, Year: {movie['year']}")
        else:
            print("No movies in the Database")


def find_movies():
    movie_to_find = input("Which movie are you looking for? ")

    for movie in movies:
        if movie_to_find.lower() == movie['title'].lower():
            print(movie)
        else:
            print("Movie is not in the Database")


def choices():
    while True:
        selection = input(MENU_PROMPT)
        if selection == "a":
            add()
        elif selection == "l":
            movies_list()
        elif selection == "f":
            find_movies()
        elif selection == "q":
            print("Goodbye")
            break
        else:
            print('Unknown command. Please try again.')


choices()
