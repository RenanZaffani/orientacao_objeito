class Program:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name.title()

    def __str__(self):
        return f'{self.name} - {self.year} - {self.likes} Likes'


class Movie(Program):
    def __init__(self, name, year, length):
        super().__init__(name, year)
        self.length = length

    def __str__(self):
        return f'{self.name} - {self.year} - {self.length} min - {self.likes} Likes'


class Series(Program):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return f'{self.name} - {self.year} - {self.seasons} seasons - {self.likes} Likes'


class Playlist:
    def __init__(self, name, programs):
        self.name = name
        self._programs = programs

    def __getitem__(self, item):
        return self._programs[item]

    @property
    def listing(self):
        return self._programs

    def __len__(self):
        return len(self._programs)


avengers = Movie('The Avengers: Infinity War', 2018, 160)
suits = Series('Suits', 2011, 9)
tmep = Movie('Everyone in Panic', 1999, 100)
flash = Series('The Flash', 2016, 6)

avengers.dar_like()
tmep.dar_like()
tmep.dar_like()
flash.dar_like()
flash.dar_like()
flash.dar_like()
flash.dar_like()
suits.dar_like()
suits.dar_like()

movies_and_series = [avengers, suits, tmep]
playlist_weekend = Playlist('Weekend', movies_and_series)

print(f'Playlist´s size: {len(playlist_weekend)}')

print(playlist_weekend[0])

for program in playlist_weekend.listing:
    print(program)
