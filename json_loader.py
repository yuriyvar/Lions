import simplejson as json
import os
import copy
import glob



dir1 = '/Users/jtm211/Documents/Education & Training/Data Science Bootcamp/ct16_cap1_ds4/project_1/data/boxofficemojo/'
boxOmojo_movies = []
for filename in glob.glob(os.path.join(dir1, '*.json')):
    with open(filename, 'r') as json_file:
            movie = json.load(json_file)
            boxOmojo_movies.append(movie)

dir2 = '/Users/jtm211/Documents/Education & Training/Data Science Bootcamp/ct16_cap1_ds4/project_1/data/metacritic/'
metacritic_movies = []
for filename in glob.glob(os.path.join(dir2, '*.json')):
    with open(filename, 'r') as json_file:
            movie = json.load(json_file)
            metacritic_movies.append(movie)

metacr_movies_genre = []
for filename in glob.glob(os.path.join(dir2, '*.json')):
    with open(filename, 'r') as json_file:
            movie = json.load(json_file)
            metacr_movies_genre.append(movie)




genre_keys = ('title', 'genre')
movie_fields = {genre_keys: metacritic_movies[genre_keys] for genre_keys in metacritic_movies if genre_keys in metacritic_movies}
movie_fields = {k: metacritic_movies[('title', 'genre')] for k in ('title', 'genre')}


interesting_keys = ('title', 'genre')
subdict = {x: bigdict[x] for x in interesting_keys if x in bigdict}

import re


def GetMovieAndRating(request):
    m = MOVIE_RATING_RE.match(request)
    if m:
        return (int(m.group(1)), int(m.group(2)))
    else:
        return (None, None)
    genre_df = pd.DataFrame(new_list)
    return new_list


# Breaking the key 'genre' into three columns
nl = []

for dct in a:
    c = copy.deepcopy(dct)
    nd = {}
    if type(c) != type({}) or 'title' not in c.keys() or type(c['genre']) != type([]): continue
    nd['title'] = c['title']
    nd['director'] = c['director']
    genre = c['genre']
    for i in xrange(3): genre.append(None)

    nd['genre_0'] = genre[0]
    nd['genre_1'] = genre[1]
    nd['genre_2'] = genre[2]

    nl.append(nd)

