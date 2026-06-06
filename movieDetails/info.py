import requests
#   data = requests.get("https://www.omdbapi.com/?i=tt3896198&apikey=6e4120b6").json()
while True:
    movie = input("Enter movie name: ")
    url = f"https://www.omdbapi.com/?t={movie}&apikey=6e4120b6"
    data = requests.get(url).json()
    print("movie name: ", data["Title"])
    print("movie year: ", data["Year"])
    print("movie genre: ", data["Genre"])   
    print("movie director: ", data["Director"])
    print("movie actors: ", data["Actors"])
    print("movie plot: ", data["Plot"])
    print("movie language: ", data["Language"])
    print("movie country: ", data["Country"])
    print("movie awards: ", data["Awards"])
    print("movie poster: ", data["Poster"])
    if input("Do you want to search for another movie? (yes/no): ") == "no":
        break