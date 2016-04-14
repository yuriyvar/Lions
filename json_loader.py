import simplejson as json
import os
import glob



dir1 = '/Users/jtm211/Documents/Education & Training/Data Science Bootcamp/ct16_cap1_ds4/project_1/data/boxofficemojo/'
boxOmojo_movies = []
for filename in glob.glob(os.path.join(dir, '*.json')):
    with open(filename, 'r') as json_file:
            movie = json.load(json_file)
            boxOmojo_movies.append(movie)

dir2 = '/Users/jtm211/Documents/Education & Training/Data Science Bootcamp/ct16_cap1_ds4/project_1/data/metacritic/'
metacritic_movies = []
for filename in glob.glob(os.path.join(dir, '*.json')):
    with open(filename, 'r') as json_file:
            movie = json.load(json_file)
            metacritic_movies.append(movie)