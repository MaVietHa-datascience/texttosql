from dotenv import load_dotenv
load_dotenv() ## load environment variables
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

#configure apikey
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

#function to load  google gemni model
def get_gemini_response(question,prompt):
    try: 
        model=genai.GenerativeModel('gemini-2.0-flash')
        response=model.generate_content([prompt[0],question])
        return response.text.strip()
    except:
        return f"Error generating SQL: {e}"

## Fucntion To retrieve query from the database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt
prompt = [
    """
    Convert the following English question into a SQL query for a database named STUDENT with columns NAME, CLASS, SECTION, MARKS. 
    Return only the SQL query, no explanations, no extra text, no ``` marks, and no "sql" word. 
    Examples:
    - "How many entries of records are present?" → SELECT COUNT(*) FROM STUDENT
    - "Tell me all the students studying in Data Science class?" → SELECT * FROM STUDENT WHERE CLASS="Data Science"
    Input: 
    """
]

## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    st.write("Generated SQL:", response)  # Debug: Show the query
    result = read_sql_query(response, "student.db")
    st.subheader("The Response is")
    if isinstance(result, str):  # Error case
        st.error(result)
    else:
        for row in result:
            st.write(row)  # Better formatting