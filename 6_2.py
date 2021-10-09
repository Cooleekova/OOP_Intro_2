class Track:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def show(self):
        return f'{self.name} - {self.duration}'


yellow_submarine = Track('Yellow Submarine', 5)
she_said = Track('She Said She Said', 4)
good_day_sunshine = Track('Good Day Sunshine', 4)

breed = Track('Breed', 3)
lithium = Track('Lithium', 4)
polly = Track('Polly', 2)


class Album:
    def __init__(self, name, band):
        self.name = name
        self.band = band
        self.tracks = []

    def get_tracks(self):
        for track in self.tracks:
            print(track.show())

    def add_track(self, new_track):
        self.tracks.append(new_track)

    def get_duration(self):
        album_duration = 0
        for track in self.tracks:
            album_duration += track.duration
        print(f'Длительность альбома {self.name} - {album_duration} минут')


print()
revolver = Album('Revolver', 'Beatles')
revolver.tracks = [yellow_submarine, she_said, good_day_sunshine]
revolver.get_tracks()

print()
nevermind = Album('Nevermind', 'Nirvana')
nevermind.tracks = [breed, lithium, polly]
nevermind.get_tracks()

print()
revolver.get_duration()
nevermind.get_duration()
