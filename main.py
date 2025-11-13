import streamlit as st
from extract_data import skapa_dataframe  # updated function name
from graph import graph  # assuming your graph function stays the same

st.set_page_config(layout="wide")

def layout():
    st.title("Väder applikation")
    
    city = st.selectbox("Välj stad:", options=["stockholm", "göteborg", "malmö"])
    df = skapa_dataframe(city)  # call the updated function
    st.plotly_chart(graph(df))
        
if __name__ == "__main__":
    layout()
