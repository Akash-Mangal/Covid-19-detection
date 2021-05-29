import streamlit as st
from gsheetsdb import connect
from PIL import Image
import pyqrcode
from pyqrcode import QRCode
import cv2
import numpy as np
import png
import sys
# Create a connection object.
conn = connect()
# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
  rows = conn.execute(query, headers=1)
  return rows
sheet_url = st.secrets["public_gsheets_url"]
specific= st.button("Specific member")
if specific:
  name = st.text_input("Name")
  row = run_query(f'SELECT * FROM "{sheet_url}" WHERE Name = "{name}"')
  st.write(f"{row.Name} is in group number: {int(row.Group_number)}")
# Print results.
all_memb= st.button("Show all data")
if all_memb:
  rows = run_query(f'SELECT * FROM "{sheet_url}"')
  for row in rows:
    st.write(f"{row.Name} is in group number: {int(row.Group_number)}")
 

 


