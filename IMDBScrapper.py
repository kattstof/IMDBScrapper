import imdb
import pprint
from colorama import Fore, init
init(convert=True)
ia = imdb.IMDb()
print(Fore.YELLOW + """
(_)             | | |
 _ _ __ ___   __| | |__    ___  ___ _ __ __ _ _ __  _ __   ___ _ __
| | '_ ` _ \ / _` | '_ \  / __|/ __| '__/ _` | '_ \| '_ \ / _ \ '__|
| | | | | | | (_| | |_) | \__ \ (__| | | (_| | |_) | |_) |  __/ |
|_|_| |_| |_|\__,_|_.__/  |___/\___|_|  \__,_| .__/| .__/ \___|_|
                                             | |   | |
                                             |_|   |_|
""")
print('[1] Trivia')
print('[2] Runtime')
print('[3] Rating')
print('[4] Director')
print('[5] Cast')
print('[6] Top 250')
print('[7] Box Office')
print('[8] Plot')
print('[0] Testing')
main = input('Please enter choice: ')
if main == '1':
    search = input('What movie?: ')
    s_result = ia.search_movie(search)
    movie = s_result[0]
    ia.update(movie, 'trivia')
    trivia = (movie['trivia'])
    for index, value in enumerate(trivia, 1):
        print("{}. {}".format(index, value + '\n'))
if main == '2':
    search = input('What movie?: ')
    s_result = ia.search_movie(search)
    movie = s_result[0]
    ia.update(movie)
    run = movie['runtime']
    print(movie['runtime'], 'Minutes')
if main == '3':
    search = input('What Movie?')
    s_result = ia.search_movie(search)
    movie = s_result[0]
    ia.update(movie)
    print(movie['rating'], '/10')
if main == '4':
    search = input('What movie?: ')
    s_result = ia.search_movie(search)
    movie = s_result[0]
    ia.update(movie)
    director = movie['director']
    for person in director:
        print(person['name'])
if main == '5':
    search = input('What movie?: ')
    s_result = ia.search_movie(search)
    movie = s_result[0]
    ia.update(movie)
    cast = movie['cast']
    for person in cast:
        print(person['name'])
if main == '6':
    top = ia.get_top250_movies()
    for item in top:
        print(item['title'])
if main == '7':
    search = input('What movie?: ')
    s_result = ia.search_movie(search)
    movie = s_result[0]
    ia.update(movie)
    boxoffice = movie['box office']
    print(boxoffice)
if main =='0':
    search = input('What movie?: ')
    s_result = ia.search_movie(search)
    movie = s_result[0]
    ia.update(movie)
    print(movie.infoset2keys)
if main == '8':
    search = input('What movie?: ')
    s_result = ia.search_movie(search)
    movie = s_result[0]
    ia.update(movie)
    plot = movie['plot']
    print(plot)
