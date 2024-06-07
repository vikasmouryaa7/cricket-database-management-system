import streamlit as st
import streamlit as st
import mysql.connector
from create import create1
from create import create2
from create import create3
from create import create4,create0
from database import create_table1
from database import create_table2
from database import create_table3
from database import create_table4
from delete import delete
from read import read1
from read import read2
from read import read3
from read import read4

from update import update1,update2
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234"
)
c = mydb.cursor()
 
def main():
    st.title("Cricket Database CS274")
    menu = ["My query","Add Player", "Add Game","Add Team","Add participates","View player info","View game info","View team Info","View participates","Edit Player jersey no","Edit Team coach","Delete player"]
    choice = st.sidebar.selectbox("Menu", menu)
 
    if choice == "My query":
        st.subheader("Enter your query: ")
        create0()  
    elif choice == "Add Player":
        create_table1()
        st.subheader("Enter Player Details:")
        create1()
    elif choice == "Add Game":
        create_table2()
        st.subheader("Add Game Details:")
        create2()
    elif choice == "Add Team":
        create_table3()
        st.subheader("Add Team Details:")
        create3()
    elif choice == "Add participates":
        create_table4()
        st.subheader("A player participates in a given game:")
        create4()
    elif choice == "View player info":
        create_table4()
        st.subheader("Provide the player's performance in the particular match:")
        read1()
    elif choice == "View game info":
        create_table4()
        st.subheader("Provide the player's performance in the particular match:")
        read2()
    elif choice == "View team Info":
        create_table4()
        st.subheader("Provide the player's performance in the particular match:")
        read3()
    elif choice == "View participates":
        create_table4()
        st.subheader("Provide the player's performance in the particular match:")
        read4()
    elif choice == "Edit Player jersey no":
        st.subheader("Edited Player Details:")
        update1()
    elif choice == "Edit Team coach":
        st.subheader("Edited Team Details:")
        update2()
    elif choice=="Delete player":
        st.subheader("Provide details of player to delete")
        delete()
    else:
        st.subheader("About Cricket")
 
 
if __name__ == '__main__':
    main()