#!Python3
__Author__ = 'Kattstof'
import imdb
from colorama import Fore, init


while True:
    init(convert=True)
    ia = imdb.IMDb()
    print(Fore.YELLOW + """
    (_)             | | |
     _ _ __ ___   __| | |__    ___  ___ _ __ __ _ _ __  _ __   ___ _ __
    | | '_ ` _ \ / _` | '_ \  / __|/ __| '__/ _` | '_ \| '_ \ / _ \ '__|
    | | | | | | | (_| | |_) | \__ \ (__| | | (_| | |_) | |_) |  __/ |
    |_|_| |_| |_|\__,_|_.__/  |___/\___|_|  \__,_| .__/| .__/ \___|_|
                                                 | |   | |
                                                 |_|   |_|""")
    print('[1] Trivia')
    print('[2] Runtime')
    print('[3] Rating')
    print('[4] Director')
    print('[5] Cast')
    print('[6] Top 250')
    print('[7] Box Office')
    print('[8] Plot')
    print('[9] Release Date')
    print('[10] Goofs')
    print('[0] Exit')
    main = input('Please enter choice: ')
    search = input('What movie?: ')
    s_result = ia.search_movie(search)
    movie = s_result[0]
    if main == '1':
        ia.update(movie, 'trivia')
        trivia = (movie['trivia'])
        for index, value in enumerate(trivia, 1):
            print("{}. {}".format(index, value + '\n'))
        input("Press Enter To Go Back To Main Menu... ")
    if main == '2':
        ia.update(movie)
        run = movie['runtime']
        print(movie['runtime'], 'Minutes')
        input("Press Enter To Go Back To Main Menu...")
    if main == '3':
        ia.update(movie)
        print(movie['rating'], '/10')
        input("Press Enter To Go Back To Main Menu...")
    if main == '4':
        ia.update(movie)
        director = movie['director']
        for person in director:
            print(person['name'])
        input("Press Enter To Go Back To Main Menu...")
        
    if main == '5':
        ia.update(movie)
        cast = movie['cast']
        for person in cast:
            print(person['name'])
        input("Press Enter To Go Back To Main Menu...")
    if main == '6':
        top = ia.get_top250_movies()
        for item in top:
            print(item['title'])
        input("Press Enter To Go Back To Main Menu...")
    if main == '7':
        ia.update(movie)
        boxoffice = movie['box office']
        print(boxoffice)
        input("Press Enter To Go Back To Main Menu...")
    if main == '8':
        ia.update(movie)
        plot = movie['plot']
        print(plot)
        input("Press Enter To Go Back To Main Menu...")
    if main =='9':
        ia.update(movie)
        release = movie['original air date']
        print(movie, 'Was released on: ',release)
        input("Press Enter To Go Back To Main Menu...")
    if main == '10':
        ia.update(movie, 'goofs')
        goof = (movie['goofs'])
        for index, value in enumerate(goof, 1):
            print("{}. {}".format(index, value['text'] + '\n'))
        print('')
        input('Press enter to go back to main menu: ') 
    if main == '0':
        print('Exiting...')
        quit()
