import streamlit as st 
import pickle
import pandas as pd

pipe = pickle.load(open('pipe.pkl' , 'rb'))

cities = ['Delhi', 'Kolkata', 'Chennai', 'Mumbai', 'Bangalore', 'Sharjah',
       'Raipur', 'Ahmedabad', 'Hyderabad', 'East London', 'Chandigarh',
       'Durban', 'Johannesburg', 'Abu Dhabi', 'Bengaluru', 'Pune',
       'Dharamsala', 'Nagpur', 'Jaipur', 'Dubai', 'Cape Town',
       'Kimberley', 'Port Elizabeth', 'Centurion', 'Ranchi', 'Cuttack',
       'Indore', 'Visakhapatnam', 'Bloemfontein']
teams = ['Delhi Capitals', 'Kolkata Knight Riders', 'Kings XI Punjab',
       'Royal Challengers Bangalore', 'Mumbai Indians',
       'Sunrisers Hyderabad', 'Rajasthan Royals', 'Chennai Super Kings']

st.title('IPL Winning Probability')

col1 , col2 = st.columns(2)

with col1:
    batting_team = st.selectbox("Select Batting Team" , sorted(teams))

with col2:
    bowling_team = st.selectbox("Select Bowling Team" , sorted(teams))

city = st.selectbox("Select the City" , sorted(cities))
target = st.number_input("Target")

col3 , col4 , col5 = st.columns(3)

with col3:
    score = st.number_input("Score")
with col4:
    overs  = st.number_input("Overs Completed")
with col5:
    wickets = st.number_input("Wickets")

 

if st.button("Predict Probability"):
    runs_left = target - score
    balls_left = 120 - (overs*6)
    wickets_left = 10 -wickets
    crr = score / overs
    rrr = (runs_left *6) / balls_left

    df = pd.DataFrame({
        'batting_team' : [batting_team],
        'bowling_team' :[bowling_team],
        'city':[city],
        'first_inning_runs':[target],
        'current_score':[score],
        'runs_left':[runs_left],
        'balls_left':[balls_left],
        'wickets':[wickets_left],
        'crr':[crr],
        'rrr':[rrr]


    })


    result = pipe.predict_proba(df)
    win = result[0][0]
    loss = result[0][1]
    
    st.header(f"{bowling_team} : {round(win*100)} %")
    st.header(f"{batting_team} : {round(loss*100)} %")

