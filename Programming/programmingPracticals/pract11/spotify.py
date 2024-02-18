class Song:

    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = int(duration)

    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist

    def getDuration(self):
        return self.duration

    def __str__(self):
        output = f"Song Name: {self.title}\n - Artist: {self.artist}"
        output += f"\n - Song duration: {self.duration} seconds"
        return output


def testSong():
    song = Song("A", "Artist", 234)
    print(song.getTitle())
    print(song)

# testSong()


class Playlist:

    def __init__(self, name, user):
        self.name = name
        self.user = user
        self.private = False
        self.songs = set()

    def getName(self):
        return self.name

    def getUser(self):
        return self.user

    def getPrivate(self):
        return self.private

    def rename(self, name):
        self.name = str(name)

    def addSong(self, title, artist, duration):
        self.songs.add(Song(title, artist, duration))

    def removeSong(self, name):
        for song in self.songs:
            if name.lower() == song.title:
                self.songs.remove(song)

    def totalDuration(self):
        total = 0
        for song in self.songs:
            total += song.duration
        return total

    def totalSongs(self):
        count = 0
        for song in self.songs:
            count += 1
        return count

    def playlistPrivacy(self):
        if self.private:
            self.private = False
        else:
            self.private = True

    def __str__(self):
        output = f"Playlist name: {self.name}\nPrivate: {self.private}\n"
        output += f"Made by: {self.user} | {self.totalSongs()} "
        output += f"Songs | about {self.totalDuration()} seconds\n"
        output += f"{'#':^5}{'Title':<50}{'Duration':<10}"
        count = 1
        for song in self.songs:
            output += f"\n{count:^5}{song.title:<50}{song.duration:^10}\n\tBy: {song.artist}"
            count += 1
        return output + "\n"


def testPlaylist():
    playlist = Playlist("HeeBeeJeeBees", "Collin")
    playlist.addSong("Cut", "The Cure", 213)
    playlist.addSong("Grace", "Jeff Buckley", 322)
    playlist.addSong("Sour Times", "portishead", 218)
    playlist.playlistPrivacy()
    print(playlist)


# testPlaylist()


class Library:

    def __init__(self, user):
        self.playlists = []
        self.__playlistIndex = 0
        self.__edible = False
        self.user = user

    def createPlaylist(self, name, user):
        if user == "":
            self.playlists.append(Playlist(name, self.user))
        else:
            self.playlists.append(Playlist(name, user))

    def removePlaylist(self):
        self.playlists.pop(self.__playlistIndex)

    def selectPlaylist(self, index):
        if index.isdigit():
            index = int(index)
            self.__playlistIndex = index - 1
        else:
            for i in self.playlists:
                if index.lower() == i.getName().lower():
                    self.__playlistIndex = self.playlists.index(i)
                    if self.playlists[self.__playlistIndex].getUser().lower() == self.user.lower():
                        self.__edible = True

    def setPrivacy(self):
        if self.__edible:
            self.playlists[self.__playlistIndex].playlistPrivacy()

    def renamePlaylist(self, name):
        if self.__edible:
            self.playlists[self.__playlistIndex].rename(name)

    def addSongToPlaylist(self, title, artist, duration):
        if self.__edible:
            self.playlists[self.__playlistIndex].addSong(
                title, artist, duration)

    def removeSongFromPlaylist(self, songName):
        if self.__edible:
            for song in self.playlists[self.__playlistIndex]:
                if song.title.lower() == songName.lower():
                    self.playlists[self.__playlistIndex].removeSong(songName)

    def displayPlaylist(self):
        return self.playlists[self.__playlistIndex]

    def __str__(self):
        output = f"Playlists"
        for i in self.playlists:
            output += f"\n- {i.getName()}"
        return output + "\n"

    def validPlaylist(self, selector):
        if selector.isdigit():
            selector = int(selector)
            if 0 <= selector - 1 < len(self.playlists):
                return True
        else:
            for i in self.playlists:
                print(i.getName().lower())
                if selector.lower() == i.getName().lower():
                    return True
            return False

    def editable(self):
        if self.playlists[self.__playlistIndex].getUser().lower() == self.user.lower():
            return True
        else:
            return False


def testLibrary():
    lib = Library("Dave")
    lib.createPlaylist("A", "")
    lib.createPlaylist("One", "")
    lib.createPlaylist("Two", "")
    print(lib, "\n")
    lib.selectPlaylist("0")
    lib.addSongToPlaylist("Cut", "The Cure", 213)
    lib.addSongToPlaylist("Grace", "Jeff Buckley", 322)
    lib.addSongToPlaylist("Sour Times", "portishead", 218)
    print(lib.displayPlaylist())
    lib.selectPlaylist("One")
    lib.addSongToPlaylist("Grace", "Jeff Buckley", 322)
    lib.addSongToPlaylist("Sour Times", "portishead", 218)
    print(lib.displayPlaylist())
    lib.selectPlaylist("Two")
    lib.addSongToPlaylist("Cut", "The Cure", 213)
    lib.addSongToPlaylist("Sour Times", "portishead", 218)
    print(lib.validPlaylist("One"))


# testLibrary()


def main():
    user = input("Enter Username: ")
    myLibrary = Library(user)
    myLibrary.createPlaylist("Rock Classics", "Spotify")
    myLibrary.playlists[0].addSong("Runaway", "Bon Jovi", 231)
    myLibrary.playlists[0].addSong("Thunderstruck", "AC/DC", 293)
    myLibrary.playlists[0].addSong(
        "I Love Rock 'N Roll", "Joan Jett & the Blackhearts", 175)
    myLibrary.playlists[0].addSong(
        "Paint it, Black", "The Rolling Stones", 202)
    myLibrary.playlists[0].addSong("Dream On", "Aerosmith", 268)
    myLibrary.createPlaylist("Rap UK", "Spotify")
    myLibrary.playlists[1].addSong("Brilliant Mind", "Blanco", 137)
    myLibrary.playlists[1].addSong("Entrapreneur", "Central Cee", 144)
    myLibrary.playlists[1].addSong("L's", "Nemzzz", 117)
    userInput = ""
    while userInput.lower() != "q":
        print(myLibrary)
        userInput = input(
            "Select playlist or C to create a playlist or q to exit: ")
        if userInput.lower() == "c":
            name = input("Enter playlist name: ")
            myLibrary.createPlaylist(name, "")
        elif userInput.lower() == "q":
            break
        else:
            if myLibrary.validPlaylist(userInput):
                myLibrary.selectPlaylist(userInput)
                if myLibrary.editable():
                    while userInput.lower() != "b":
                        print(myLibrary.displayPlaylist())
                        userInput = input(
                            "1 to delete playlist or 2 to \
private playlist or 2 to rename playlist, \
or 3 to add a song or 4 to remove a song or b to go back: ")
                        if userInput == "1":
                            myLibrary.removePlaylist()
                            break
                        elif userInput == "2":
                            myLibrary.setPrivacy()
                        elif userInput == "3":
                            title = input("Enter the title of the song: ")
                            artist = input("Enter the artist of the song: ")
                            duration = int(
                                input("Enter the duration of the song in seconds: "))
                            myLibrary.addSongToPlaylist(
                                title, artist, duration)
                        elif userInput == "4":
                            songName = input("Enter song name: ")
                            myLibrary.removeSongFromPlaylist(songName)
                        else:
                            break
                else:
                    print(myLibrary.displayPlaylist())
                    userInput = input(
                        "Enter 1 to delete playlist or b to go back: ")
                    if userInput == "1":
                        myLibrary.removePlaylist()
            else:
                print("Not valid Playlist")


main()
