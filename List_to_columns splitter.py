import simplejson as json
import os
import copy
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
import statsmodels.api as sm
from sklearn.cross_validation import train_test_split
from sklearn.metrics import mean_squared_error
import math

dir1 = '/Users/jtm211/Documents/Education & Training/Data Science Bootcamp/ct16_cap1_ds4/project_1/data/boxofficemojo/'
boxOmojo_movies = []
for filename in glob.glob(os.path.join(dir1, '*.json')):
    with open(filename, 'r') as json_file:
            movie = json.load(json_file)
            boxOmojo_movies.append(movie)

dir2 = '/Users/jtm211/Documents/Education & Training/Data Science Bootcamp/ct16_cap1_ds4/project_1/data/metacritic/'

metacr_movies_genre = []
for filename in glob.glob(os.path.join(dir2, '*.json')):
    with open(filename, 'r') as json_file:
            movie = json.load(json_file)
            metacr_movies_genre.append(movie)


# Breaking the key 'genre' into three columns
nl = []

for dct in metacr_movies_genre:
    nd = {}
    if type(dct) != type({}) or 'title' not in dct.keys() or type(dct['genre']) != type([]) or dct['complete'] == False:
            #or dct['genre'] not in ['Comedy','Drama','Action','Adventure']:
        continue
    nd['title'] = dct['title']
    nd['director'] = dct['director']
    nd['metascore'] = dct['metascore']
    nd['num_user_ratings'] = dct['num_user_ratings']
    nd['release_date'] = dct['release_date']
    nd['year'] = dct['year']
    nd['studio'] = dct['studio']
    nd['user_score'] = dct['user_score']
    genre = dct['genre']
    for i in xrange(3): genre.append(None)

    nd['genre_0'] = genre[0]
    nd['genre_1'] = genre[1]
    nd['genre_2'] = genre[2]

    nl.append(nd)

genre_df = pd.DataFrame(nl)
mj_df = pd.DataFrame(boxOmojo_movies)

df = pd.merge(mj_df, genre_df, how = 'inner', on=['title', 'year'])
df['growth_factor'] = df['domestic_gross'] / df['opening_weekend_take']

# df.columns
# df.head
df = df.query("genre_0 in ('Comedy','Drama','Action','Adventure')")
#Filtering
# PANDAS -  df.query("genre_0 in ('Comedy','Drama','Action','Adventure')")
# PANDAS - list of values: df.query("genre_0 == ['Comedy','Drama','Action','Adventure']")
# Pure Python:    df[df.genre_0.isin(['Comedy','Drama'])]

import seaborn as sns
#run in terminal %pylab
g = sns.FacetGrid(df, col="genre_0", col_wrap=4, sharex=True, ylim=(0,50), hue="year")
'''
g.map(plt.scatter, 'opening_per_theater', 'growth_factor')
g.map(sns.kdeplot, 'opening_per_theater', 'growth_factor')
'''
g.map(plt.scatter, 'opening_per_theater', 'growth_factor')
g.add_legend()
#g = g.map(sns.regplot, 'opening_per_theater', 'growth_factor')
#g.savefig('fig.jpeg')