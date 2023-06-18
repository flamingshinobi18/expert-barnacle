import streamlit as st
from dbfile import mycursor,fetch_data
st.title("Customer Log")
ls = fetch_data()
df = {'id':[],"Name":[],"Address":[],"Number":[],"Pending":[],"Cluster":[]}
for i in ls:
    df['id'].append(i[0])
    df["Name"].append(i[1])
    df["Address"].append(i[2])
    df["Number"].append(i[3])
    df["Pending"].append(i[4])
    df["Cluster"].append(i[5])

st.table(df)

