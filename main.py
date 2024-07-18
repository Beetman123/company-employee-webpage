import streamlit as st
import pandas

# tadas

st.title("Company Website")
st.write("Here is the description of the company. Blah blah blah")

col1, brkc1, col2, brekc2, col3 = st.columns([1,.25,1,.25,1])

data = pandas.read_csv("data.csv", sep=';')

num_employees = len(data)

num_col1 = num_employees/3 + num_employees%3
num_col2 = num_employees/3
if num_employees%3 > 1:
    num_col2 += 1

with col1:
    for index, row in data[:num_col1].iterrows():
        st.header(row["first name"] + row["last name"])
        st.write(row["role"])
        st.image("images/" + row['image'])

with col2:
    for index, row in data[num_col1:num_col2].iterrows():
        st.header(row["first name"] + row["last name"])
        st.write(row["role"])
        st.image("images/" + row['image'])

with col3:
    for index, row in data[num_col2:].iterrows():
        st.header(row["first name"] + row["last name"])
        st.write(row["role"])
        st.image("images/" + row['image'])