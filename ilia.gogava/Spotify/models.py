from django.db import models

# Create your models here.

from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Track(models.Model):
    title = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    duration_ms = models.IntegerField()

    def __str__(self):
        return self.title


class AudioFeatures(models.Model):
    track = models.OneToOneField(Track, on_delete=models.CASCADE)
    tempo = models.FloatField()
    energy = models.FloatField()

    def __str__(self):
        return f"{self.track.title} features"



#ეს ცალკე გავკეთე ქვემოთ და დავტოვე პროსტა--->

class AudioFeature(models.Model):
    track = models.OneToOneField(Track, on_delete=models.CASCADE, related_name="audio_features")

    danceability = models.FloatField()
    energy = models.FloatField()
    tempo = models.FloatField()
    valence = models.FloatField()
    loudness = models.FloatField()

    def __str__(self):
        return f"Audio Features of {self.track.name}"
    

