import streamlit as st
import pandas

st.title("The best Company ")
content = """Lorem ipsum dolor sit amet, 
consectetur adipiscing elit, sed do eiusmod tempor
 incididunt ut labore et dolore magna aliqua. Ut enim
  ad minim veniam, quis nostrud exercitation ullamco 
  laboris nisi ut aliquip ex ea commodo consequat. 
  Duis aute irure dolor in reprehenderit in voluptate 
  velit esse cillum dolore eu fugiat nulla pariatur."""
st.write(content)
st.subheader("Out team")
col1, col2, col3 = st.columns(3)
content = pandas.read_csv("data.csv", sep=",")
with col1:
    for index, row in content[:4].iterrows():
        name = row["first name"] + " " + row["last name"]
        st.subheader(name.title())
        st.write(row["role"])
        st.image(f"images/{row['image']}")

with col2:
    for index, row in content[4:8].iterrows():
        name = row["first name"] + " " + row["last name"]
        st.subheader(name.title())
        st.write(row["role"])
        st.image(f"images/{row['image']}")

with col3:
    for index, row in content[8:].iterrows():
        name = row["first name"] + " " + row["last name"]
        st.subheader(name.title())
        st.write(row["role"])
        st.image(f"images/{row['image']}")