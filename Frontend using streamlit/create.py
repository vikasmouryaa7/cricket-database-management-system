import streamlit as st
from database import add_data1
from database import add_data2
from database import add_data3
from database import add_data4
from database import query0

def create0():
    query=st.text_input("Your query: ")
    if st.button("My query"):
        result = query0(query)
        st.write(result)
        st.success("Sucessfully executed your query")
        
def create1():
    col1, col2 = st.columns(2)
    with col1:
        pid = st.number_input("Player ID:")
        fname = st.text_input("Player's first name:")
        lname= st.text_input("Player's Last name:")
        dob=st.date_input("Date of birth:")
    with col2:
        nationality=st.text_input("Nationality:")
        type=st.text_input("Batsman/Bowler/Allrounder:")
        tid=st.number_input("Enter the team Id:")
        jersey_no=st.number_input("Jersey Number:")
 
    if st.button("Add Player"):
        add_data1(pid,fname,lname,dob,nationality,type,tid,jersey_no)
        st.success("Successfully added player: {}".format(pid))
        
def create2():
    col1, col2 = st.columns(2)
    with col1:
        gid = st.number_input("Game ID:")
        date= st.date_input("Match Date:")
        toss=st.text_input("Toss Result:")
    with col2:
        result=st.text_input("Match Result:")
        player_of_match=st.text_input("Player of the match:")
        tid=st.number_input("Enter the team Id:")
 
    if st.button("Add Game"):
        add_data2(gid,date,toss,result,player_of_match,tid)
        st.success("Successfully added Game: {}".format(gid))
        
def create3():
    col1, col2 = st.columns(2)
    with col1:
        tid = st.number_input("Team ID:")
        Tname= st.text_input("Team name:")
        ShortN= st.text_input("Shorthand team name:")
    with col2:
        coach=st.text_input("Coach:")
        Field_bat=st.text_input("Is the team batting or fielding:")
        Trophy_won=st.number_input("Number of trophies won:")
 
    if st.button("Add Team"):
        add_data3(tid,Tname,ShortN,coach,Field_bat,Trophy_won)
        st.success("Successfully added Team: {}".format(tid))
        
def create4():
    col1, col2 = st.columns(2)
    with col1:
        pid = st.number_input("Player ID:")
    with col2:
        gid = st.number_input("Game ID:")
    if st.button("Add Participates"):
        add_data4(pid,gid)
        st.success("Successfully added Participates: {}".format(gid))