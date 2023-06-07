import pandas as pd
import streamlit as st
import sqlite3


conn=sqlite3.connect('C:\\Users\\Saphire\\Desktop\\test.db') # copy path of db file and use ' \\ ' to connect to DB
c= conn.cursor()





#__________________ Main Table _______________________________

show_tables="SELECT name FROM sqlite_master WHERE type='table'"

query1 = "SELECT * FROM Student1"
query2= "SELECT * FROM Teacher"

df_all_tables= pd.read_sql(show_tables,conn)
df_student = pd.read_sql(query1, conn)
df_teacher = pd.read_sql(query2, conn)
# conn.close()



#________________________________ Page Config ___________________________

st.set_page_config(
    page_title='Hospital Management System',
    page_icon=':hospital:',
    layout='wide',
)

#________________________________ Heading ____________________________

st.title("DataBase")

left_col,middle_col=st.columns(2)



#_________________________________ Side Bar _________________________

selection = st.sidebar.multiselect("Table",df_all_tables)
st.write(len(selection),"Selected")


all_student_id=()

for i in selection:
    if i == "Student1":
        c.execute("SELECT * FROM Student1")
        all_student1=c.fetchall()
        with left_col:
            st.subheader("Student")
            st.write(df_student)


    elif i == "Teacher":
        c.execute("SELECT * FROM Student1")
        all_teacher=c.fetchall()
        with middle_col:
            st.subheader("Teacher")
            st.write(df_teacher)
    


#___________________________ User Query _____________________________
st.markdown('---')
user_query = st.text_input("Run Your Query")

# st.write(Query)

c.execute(user_query)
user_query_result=c.fetchall()

st.write(user_query_result)


