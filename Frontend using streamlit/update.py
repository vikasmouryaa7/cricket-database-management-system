import datetime
import pandas as pd
import streamlit as st
from database import view_all_data1,view_all_data2,view_all_data3,view_all_data4, get_details1,get_details2, edit_details1,edit_details2
 
def update1():
    result = view_all_data1()
    player_name = st.number_input("Enter player id whose jersey number needs to be updated: ")
    selected_result = get_details1(player_name)
    new_jersey_no = st.number_input("New jersey no: ")
    if selected_result: 
        if st.button("Edit Player jersey no"):
            edit_details1(player_name,new_jersey_no)
            st.success("Successfully updated")
            
def update2():
    result = view_all_data3()
    team_name = st.number_input("Enter team id whose coach needs to be updated: ")
    selected_result = get_details2(team_name)
    new_coach = st.text_input("New coach: ")
    if selected_result:
        if st.button("Edit Team coach"):
            edit_details2(new_coach,team_name)
            st.success("Successfully updated")
