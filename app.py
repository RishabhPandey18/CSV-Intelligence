import streamlit as st;
from data_info import analyze_data
from visualization import bar_graph,pie_chart

# title of the login page 
st.title("CSV Intelligence ")
st.subheader("Welcome to your personal data analysis  tool ")

st.subheader("What should we call you? ")
name = st.text_input("Enter your full name ")
if name:
    st.write("Hello ", name)

    st.subheader("Upload Your csv file below ")
    st.warning("Choosen File should be csv . We are still growing ")

    st.selectbox("file  format", ["csv","Excel","jpg"])
    uploaded_file = st.file_uploader("Upload Csv ", 
    type=["csv"])

    if  uploaded_file is not None:
        st.write("File uploaded!")

        result = analyze_data(uploaded_file)
        st.write(result)
        
        df = result["data"]
        column = df.columns.tolist()
        x_column = st.selectbox("Choose X column " , column)
        y_column = st.selectbox("Choose Y column " , column)
        graph_title = st.text_input("Graph Name")
        
        fig = bar_graph(df,x_column,y_column,graph_title)
        
        st.pyplot(fig)
        
        column = df.columns.tolist()
        st.subheader("Pie chart ")
        
        pie_column = st.selectbox("select column " , column)
        
        components = df[pie_column].dropna().unique().tolist()
        selected_components = st.multiselect("Choose components" , components)
        graph_title = st.text_input("pie chart Name : ")
        fig = pie_chart(df,pie_column,graph_title,selected_components)
        st.pyplot(fig)

