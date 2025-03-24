import streamlit as st
import pandas as pd
import pickle
import requests
import json


movies_dict=pickle.load(open('animes.pkl', 'rb'))
similarity=pickle.load(open('similarity.pkl', 'rb'))
animes_dict=pickle.load(open('dataframe_anime.pkl', 'rb'))
new_pt=pd.DataFrame(movies_dict)
anime=pd.DataFrame(animes_dict)





def movie_recommendation(Movie_Name):
    movie_id=new_pt[new_pt['English name'].str.contains(Movie_Name)].index[0]
    items=sorted(list(enumerate(similarity[movie_id])),reverse=True, key=lambda x:x[1])[0:15]
    movie_list = []
    poster_id= []
    for i in items:
        movie_list.append(new_pt['English name'].iloc[i[0]])
        poster_id.append(new_pt['Image URL'].iloc[i[0]])

    return movie_list,poster_id



def anime_col(score_anime):
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(score_anime['English name'].iloc[0])
        st.image(score_anime['Image URL'].iloc[0])
    with col2:
        st.text(score_anime['English name'].iloc[1])
        st.image(score_anime['Image URL'].iloc[1])

    with col3:
        st.text(score_anime['English name'].iloc[2])
        st.image(score_anime['Image URL'].iloc[2])
    with col4:
        st.text(score_anime['English name'].iloc[3])
        st.image(score_anime['Image URL'].iloc[3])
    with col5:
        st.text(score_anime['English name'].iloc[4])
        st.image(score_anime['Image URL'].iloc[4])


    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(score_anime['English name'].iloc[5])
        st.image(score_anime['Image URL'].iloc[5])
    with col2:
        st.text(score_anime['English name'].iloc[6])
        st.image(score_anime['Image URL'].iloc[6])

    with col3:
        st.text(score_anime['English name'].iloc[7])
        st.image(score_anime['Image URL'].iloc[7])
    with col4:
        st.text(score_anime['English name'].iloc[8])
        st.image(score_anime['Image URL'].iloc[8])
    with col5:
        st.text(score_anime['English name'].iloc[9])
        st.image(score_anime['Image URL'].iloc[9])
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(score_anime['English name'].iloc[10])
        st.image(score_anime['Image URL'].iloc[10])
    with col2:
        st.text(score_anime['English name'].iloc[11])
        st.image(score_anime['Image URL'].iloc[11])

    with col3:
        st.text(score_anime['English name'].iloc[12])
        st.image(score_anime['Image URL'].iloc[12])
    with col4:
        st.text(score_anime['English name'].iloc[13])
        st.image(score_anime['Image URL'].iloc[13])
    with col5:
        st.text(score_anime['English name'].iloc[14])
        st.image(score_anime['Image URL'].iloc[14])


st.title('Anime Recommender System')

options = ["Most Popular", "Top Ranked", "Most Rated", "Most Favorites"]
selection = st.pills("Directions", options)


option = st.selectbox(
"Enter Anime name for Recommendation",
new_pt['English name'].values,
index=None,
placeholder="Select the Movie...",
)


if st.button('Recommend'):
    recommended_movie_names,recommended_movie_posters=movie_recommendation(option)
    #recommended_movie_posters=get_poster(poster_id)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[5])
        st.image(recommended_movie_posters[5])
    with col2:
        st.text(recommended_movie_names[6])
        st.image(recommended_movie_posters[6])

    with col3:
        st.text(recommended_movie_names[7])
        st.image(recommended_movie_posters[7])
    with col4:
        st.text(recommended_movie_names[8])
        st.image(recommended_movie_posters[8])
    with col5:
        st.text(recommended_movie_names[9])
        st.image(recommended_movie_posters[9])
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[10])
        st.image(recommended_movie_posters[10])
    with col2:
        st.text(recommended_movie_names[11])
        st.image(recommended_movie_posters[11])

    with col3:
        st.text(recommended_movie_names[12])
        st.image(recommended_movie_posters[12])
    with col4:
        st.text(recommended_movie_names[13])
        st.image(recommended_movie_posters[13])
    with col5:
        st.text(recommended_movie_names[14])
        st.image(recommended_movie_posters[14])



anime_choice=anime[anime['Rank']!='UNKNOWN']
anime_choice['Rank']=anime_choice['Rank'].astype(float)
anime_choice=anime_choice[anime_choice['Rank']>=1]
anime_choice=anime[anime['Score']!='UNKNOWN']
anime_choice['Score']=anime_choice['Score'].astype(float)
#anime_choice=anime_choice[anime_choice['Rank']>=1]

if selection:
    if "Top Ranked" in selection:
        score_anime=anime_choice.sort_values(by='Rank', ascending=True).iloc[0:20][['English name','Rank','Image URL']]
        anime_col(score_anime)
        selection=[]

    elif "Most Popular" in selection:
        score_anime=anime_choice.sort_values(by='Popularity', ascending=True).iloc[0:20][['English name','Rank','Image URL']]
        anime_col(score_anime)


    elif "Most Rated" in selection:
        score_anime=anime_choice.sort_values(by='Score', ascending=False).iloc[0:20][['English name','Rank','Image URL']]
        anime_col(score_anime)
        selection=[]

    elif "Most Favorites" in selection:
        score_anime=anime_choice.sort_values(by='Favorites', ascending=False).iloc[0:20][['English name','Rank','Image URL']]
        anime_col(score_anime)
        selection=[]








def movie_recommendation(Movie_Name):
    movie_id=new_pt[new_pt['English name'].str.contains(Movie_Name)].index[0]
    items=sorted(list(enumerate(similarity[movie_id])),reverse=True, key=lambda x:x[1])[0:15]
    movie_list = []
    poster_id= []
    for i in items:
        movie_list.append(new_pt['English name'].iloc[i[0]])
        poster_id.append(new_pt['Image URL'].iloc[i[0]])

    return movie_list,poster_id




        
        
        
        











