#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from random import shuffle

tracks_path = "/home/user/tracks_folder/"
separation_artist = 10
separation_title = 10
playlist_path = '/home/user/playlist_folder/playlist.m3u'
playlist_size = len(os.listdir(tracks_path))

nb_pl = 0

bac = []
playlist = []
artists = []
titles = []
error = []

class Track:
    def __init__(self, artist, title, filename, duration=0):
        self.artist = artist
        self.title = title
        self.filename = filename
        self.duration = duration

def read_folder(folder):
    for song_file in os.listdir(folder):
        split = os.path.splitext(song_file)[0].split(' - ')
        artist = split[0]
        title = split[1]
        filename = folder+song_file
        bac.append(Track(artist, title, filename))
        artists.append(artist)
        titles.append(title)

def get_track(i):
    j = i % len(bac)
    print "i : %d" % i
    print "j : %d" % j
    track = bac[i]
    print track.artist
    playlist.append(track)

read_folder(tracks_path)

max_artist = len(list(set(artists)))/2
max_titles = len(list(set(titles)))/2

if separation_artist == 0:
    error.append("Warning: separation_artist must be set and greater than 0.")
if separation_title == 0:
    error.append("Warning: separation_title must be set and greater than 0.")
if playlist_size == 0:
    error.append("Warning: playlist_size must be set and greater than 0.")
if max_artist < separation_artist:
    error.append('Warning: separation_artist is too high: %d use a value between 1 and %d' % (separation_artist, max_artist))
if max_titles < separation_title:
    error.append('Warning: separation_title is too high: %d use a value between 1 and %d' % (separation_title, max_titles))

if len(error) != 0:
    for err in error:
        print err
    sys.exit(0)

shuffle(bac)

while True:
    get_track(nb_pl)
    nb_pl+=1
    if playlist_size == nb_pl:
        break

m3u = open(playlist_path, 'w')
m3u.write('#EXTM3U\n')

for song in playlist:
    m3u.write('#EXTINF:%s,%s - %s\n' % ('-1',song.artist,song.title))
    m3u.write(song.filename+'\n')
m3u.close()
