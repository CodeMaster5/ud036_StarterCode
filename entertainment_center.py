import media
import fresh_tomatoes
import urllib
import json

#movieList stores the generated Movies.
movieList = []

#movie_urls is a 2d list with each list containing imdb id and youtube url.
movie_urls = [ ["tt0114709", "www.youtube.com/watch?v=NTdKQzVFeis"],
["tt0371746", "https://www.youtube.com/watch?v=8hYlB38asDY"],
["tt0145487", "https://www.youtube.com/watch?v=0KW8stZ2jSQ"],
["tt0372784", "https://www.youtube.com/watch?v=neY2xVmOfUM"],
["tt1211837", "https://www.youtube.com/watch?v=HSzx-zryEgM"],
["tt2975590", "https://www.youtube.com/watch?v=0WWzgGyAH6Y"]]

#tvList stores the generated TV_Shows.
tvList = []
#tv_urls is a 2d list with each list containing imdb id and youtube url.
tv_urls = [ ["tt3107288", "https://www.youtube.com/watch?v=Yj0l7iGKh8g"],
["tt2193021", "https://www.youtube.com/watch?v=XQS7JkQmlx8"],
["tt2364582", "https://www.youtube.com/watch?v=T3T-evQZiQo"],
["tt3749900", "https://www.youtube.com/watch?v=QxKYJW9n_5w"]]

""" This loop goes through every list in movie_urls and generates a Movie. Then
    the generated Movie is stored in movieList """
for url in movie_urls:
    #Opens a connection to the imdb database based on the given id
    connection = urllib.urlopen("http://www.omdbapi.com/?i="+url[0])
    #Stores the json data from the connection to json_data
    json_data = json.load(connection)
    #Generates the Movie from the json_data and youtube url from url[1]
    movie = media.Movie(json_data['Title'], json_data['Plot'],
    json_data['Poster'], url[1], json_data['imdbRating'], json_data['Production'])
    #Generated Movie is added to movieList
    movieList.append(movie)
    #Closing connection
    connection.close()

""" This loop goes through every list in tv_urls and generates a TV_Show. Then
    the generated TV_Show is stored in tvList """
for url in tv_urls:
    #Opens a connection to the imdb database based on the given id
    connection = urllib.urlopen("http://www.omdbapi.com/?i="+url[0])
    #Stores the json data from the connection to json_data
    json_data = json.load(connection)
    #Generates the TV_Show from the json_data and youtube url from url[1]
    tv = media.TV_Show(json_data['Title'], json_data['Plot'],
    json_data['Poster'], url[1], json_data['imdbRating'], json_data['totalSeasons'])
    #Generated TV_Show is added to tvList
    tvList.append(tv)
    #Closing connection
    connection.close()

fresh_tomatoes.open_movies_page(movieList, tvList)
