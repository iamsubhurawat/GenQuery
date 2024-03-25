import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

st.set_page_config(page_title="GenQuery",layout="centered")

hiding_st_style = """
                <style>
                MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
st.markdown(hiding_st_style, unsafe_allow_html=True)

st.title("SQL Query Generation")

"---"

query_template ="""
                You are an intelligent Database Administrator. You have to write an sql query for the question given by the user.
                Only give sql query that you generated and no additional information from your side.

                Information about the database. 
                1. Table name is given below.
                2. Column names are given in a list below with the datatypes.
                3. Follow up by the question asked by the user.

                Only give the generated sql query. If no table name and column details list is provided then just respond only
                "Sorry, may be you haven't provide the appropriate data to form an sql query. Please enter table details first"
                No other explaination is required 
                
                table name: {table_name}
                list: {list}
                question: {question}
                """
prompt = ChatPromptTemplate.from_template(query_template)
llm = ChatGroq()
chain = prompt | llm | StrOutputParser()

list = []

def response(table_name,user_question):
    result = chain.invoke({'table_name':table_name,'list': list,'question': user_question})
    "---"
    if user_question is None or user_question == "":
        st.warning("Please enter the question in the above field.")
    else:
        st.markdown(f" **Input:**   **:blue[{user_question}]**")
        with st.spinner(text="This may take a moment..."):
            st.markdown(f" **SQL query:**   **:green[{result}]**")
    "---"
    
for detail in st.session_state:
    table_name = detail['table name']
    tpl = ()
    tpl = tpl + (detail['column name'],detail['column datatype']) 
    list.append(tpl)

with st.form("Give question:",clear_on_submit=True):
    user_question = st.text_input("Enter your text")
    get_sql_query = st.form_submit_button("Get SQL query")

if get_sql_query:
    response(table_name,user_question)