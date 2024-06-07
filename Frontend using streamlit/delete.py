import pandas as pd
import streamlit as st
from database import delete_data

def delete():
    selected=st.number_input("Enter pid of the player to be deleted")
    if st.button("Delete player"):
        delete_data(selected)
        st.success("Player has been deleted successfully")
