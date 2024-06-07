import pandas as pd
import streamlit as st
from database import view_all_data1
from database import view_all_data2
from database import view_all_data3
from database import view_all_data4

def read1():
    result = view_all_data1()
    df = pd.DataFrame(result, columns = ['pid','fname','lname','dob','nationality','type','tid','jersey_no'])
    with st.expander("View player info"):
        st.dataframe(df)
        
def read2():
    result = view_all_data2()
    df = pd.DataFrame(result, columns = ['gid','date','toss','result','player_of_match','tid'])
    with st.expander("View game info"):
        st.dataframe(df)
    
def read3():
    result = view_all_data3()
    df = pd.DataFrame(result, columns = ['tid','Tname','ShortN','coach','Field_bat','Tropy_won'])
    with st.expander("View team Info"):
        st.dataframe(df)
    
def read4():
    result = view_all_data4()
    df = pd.DataFrame(result, columns = ['pid','gid'])
    with st.expander("View participates"):
        st.dataframe(df)