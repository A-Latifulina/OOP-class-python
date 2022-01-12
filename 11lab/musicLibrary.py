music = {
    'Pink Floyd': {
        'The Dark Side of the Moon': {
            'songs': [ 'Speak to Me', 'Breathe', 'On the Run', 'Money'],
            'year': 1973,
            'platinum': True
        },
        'The Wall': {
            'songs': [ 'Another Brick in the Wall', 'Mother', 'Hey you'],
            'year': 1979,
            'platinum': True
        }
    },
    'N.E.R.D': {
        'No One Really Dies':{
            'songs': ['Lemon', 'Secret Life of Tigers', '1000'],
            'year': 2017,
            'platinum': True
        }
    }
}
user_input = ''

while user_input != '5':
    user_input = input("Select option:\n1. Add Artist \n2. Add Album \n3. Add Song\n4. Display Dictionary\n5. Exit\n")
    if user_input == '1':
        artist = str(input("Enter name of artist:\n"))
        if music.get(artist,'-') == '-':
            music[artist] = {}
            print("Artist added!\n")
        else:
            print("Artist already exists\n")
    elif user_input == '2':
        artist = input("For which artist do you want to add an album?")
        if music.get(artist,'-') != '-':
            album = {}
            year = 0
            platinum = False
            usr_album = input("Enter name of album?\n")
            if music.get(artist,'-').get(usr_album,'-') == '-':
                year = input("Enter year of album:\n")
                platinum = input("Is the album platinum? (True or False)\n")
                album[usr_album] = {'songs':[], 'year':year, 'platinum':platinum}
                music[artist] = album
                print("Album added!\n")
            else:
                print("Album already exists\n")
        else:
            print("Artist doesn't exists\n")
    elif user_input == '3':
        artist = input("What is the name of your artist?\n")
        if music.get(artist,'-') != '-':
            album = input("What is the name of the album:\n")
            if music.get(artist,'-').get(album,'-') != '-':
                song = input("Enter name of song:\n")
                if music.get(artist,'-').get(album,'-').get("songs",'-').count(song) == 0:
                    music[artist][album]['songs'].append(song)
                    print("Song added!\n")
                else:
                    print("Song already exists\n")
            else:
                print("Album doesn't exists\n")
        else:
            print("Artist doesn't exists\n")
    elif user_input == '4':
        print(music, "\n")
    elif user_input == '5':
        print("Bye!\n")
    else:
        print("Invalid choice\n")
