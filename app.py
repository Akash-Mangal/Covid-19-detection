import streamlit as st
from gsheetsdb import connect
from PIL import Image
import pyqrcode
from pyqrcode import QRCode
import cv2
# Create a connection object.
conn = connect()
# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
  rows = conn.execute(query, headers=1)
  return rows
sheet_url = st.secrets["public_gsheets_url"]
name = st.text_input("Name")
rows = run_query(f'SELECT * FROM "{sheet_url}" WHERE Name = "{name}"')
# Print results.
for row in rows:
  st.write(f"{row.Name} is in group number: {int(row.Group_number)}")
  # String which represents the QR code
s = '''https://medium.com/p/12743ca0a9d9/edit'''
# output file name
#filename = “qrcode.png”
# Generate QR code
img = pyqrcode.create(s)

# Create and save the svg file naming “myqr.svg”
#img.svg(“myqr.svg”, scale = 8)
# Create and save the png file naming “myqr.png”
img.png(‘myqr’, scale = 6)
st.image(img)


