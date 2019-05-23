class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
    
happy_bday = ["Happy birthday to you",
"I don't want to get sued",
"So I'll stop right there"]
happy_bday_obj = Song(happy_bday)

bulls_on_parade = ["They rally around tha family",
"With pockets full of shells"]
bulls_on_parade_obj = Song()

happy_bday_obj.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
