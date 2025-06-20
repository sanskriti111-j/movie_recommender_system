import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommendations = []


    for i in movie_list:
        movie_id=i[0]
        #fetch poster from api
        recommendations.append(movies.iloc[i[0]].title)
    return recommendations


st.title('CineMate - Your intelligent movie buddy')

movie_dict=pickle.load(open('movie_dict.pkl', 'rb'))
movies=pd.DataFrame(movie_dict)

similarity=pickle.load(open('similarity.pkl', 'rb'))

selected_movie_name = st.selectbox(
    'Which movie would you like to watch?',movies['title'].values
)

if st.button('Watch movie'):
    recommendations1=recommend(selected_movie_name)
    for r in recommendations1:
        st.write(r)

