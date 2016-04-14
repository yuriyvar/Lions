#!/usr/bin/env python
import simplejson as json
import os
import glob


#dir1 = '/Users/jtm211/Documents/Education & Training/Data Science Bootcamp/ct16_cap1_ds4/project_1/data/boxofficemojo/'
dir1='C:/Users/ezo690/Data Science Boot Camp/ct16_cap1_ds4/project_1/data/boxofficemojo'
boxOmojo_movies = []
for filename in glob.glob(os.path.join(dir1, '*.json')):
    with open(filename, 'r') as json_file:
            movie = json.load(json_file)

            boxOmojo_movies.append(movie)

#dir2 = '/Users/jtm211/Documents/Education & Training/Data Science Bootcamp/ct16_cap1_ds4/project_1/data/metacritic/'
dir2='C:/Users/ezo690/Data Science Boot Camp/ct16_cap1_ds4/project_1/data/metacritic'
metacritic_movies = []
for filename in glob.glob(os.path.join(dir2, '*.json')):
    with open(filename, 'r') as json_file:
            movie = json.load(json_file)
            metacritic_movies.append(movie)

print "Box office Mojo"
print boxOmojo_movies[:1]

print "BLANK"
print ""
print "metacritic"
print metacritic_movies[:1]
