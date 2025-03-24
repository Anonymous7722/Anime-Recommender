import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

print('[+] Data Preprocessign for model Traning....')
anime=pd.read_csv('anime-dataset-2023.csv')

df=anime[['English name','Name','Score','Synopsis','Genres','Rank','Rating','Popularity','Image URL','Favorites']]

df['English name']=np.where(df['English name']=='UNKNOWN',
                            df['Name'],
                            df['English name'])
df[df['English name']=='UNKNOWN']

df.drop_duplicates(subset=['English name'],keep='first',inplace=True)

df=df[df['Synopsis']!='No description available for this anime.']

df.drop(columns=['Name'],inplace=True)

df=df[df['Genres']!='UNKNOWN']
df=df[df['Rating']!='UNKNOWN']

df=df.reset_index(drop=True)

df['Tags']=df['Synopsis']+df['Genres']

print('[+] Data Preprocessing Done...')
print('[+] Traning the model...')

count_vector = CountVectorizer(max_features=df.shape[0], stop_words='english')
vector = count_vector.fit_transform(df['Tags'].values.astype('U')).toarray()

similarity = cosine_similarity(vector)

print('[+] Traning Done...')

print('[+] Dumping Trained Models...')

pickle.dump(df.to_dict(),open('animes.pkl','wb'))
pickle.dump(similarity,open('similarity.pkl','wb'))


anime=pd.read_csv('anime-dataset-2023.csv')
df=anime[['English name','Name','Score','Synopsis','Genres','Rank','Rating','Popularity','Image URL','Favorites']]

df=df[df['English name']!='UNKNOWN']
df.drop_duplicates(subset=['English name'],keep='first',inplace=True)

df=df[df['Synopsis']!='No description available for this anime.']
df.drop(columns=['Name'],inplace=True)
df=df[df['Genres']!='UNKNOWN']
df=df[df['Rating']!='UNKNOWN']

df=df.reset_index(drop=True)

pickle.dump(df.to_dict(),open('dataframe_anime.pkl','wb'))