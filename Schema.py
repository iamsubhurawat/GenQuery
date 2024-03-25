import streamlit as st  

st.set_page_config(page_title="GenQuery",layout="centered")

hiding_st_style = """
                <style>
                MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
st.markdown(hiding_st_style, unsafe_allow_html=True)

st.title(":memo: GenQuery")
st.subheader("I am your assistant to generate SQL queries for you.")

"---"

# if "table_details" not in st.session_state:
st.session_state = []

with st.form(key="data_form",border=True):
    tbl_name = st.text_input("Enter table name")
    col1, col2 = st.columns(2)

    for i in range(5):
        with col1:
            col_name = st.text_input(f"Column{i+1} name",key=f'col{i}name')
        with col2:
            col_datatype = st.text_input(f"Column{i+1} datatype",key=f'col{i}datatype')
        st.session_state.append({"table name":tbl_name,"column name":col_name,"column datatype":col_datatype})
    
    st.form_submit_button("Submit schema")

