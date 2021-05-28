import streamlit as st
from gsheetsdb import connect
from PIL import Image
# Create a connection object.
conn = connect()
# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
  rows = conn.execute(query, headers=1)
  return rows
sheet_url = st.secrets["public_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')
# Print results.
for row in rows:
  st.write(f"{row.Student_Photo} {row.Name} has a : {int(row.Group_number)}:")
  im = Image.open(row.Student_Photo)
  st.image(im,use_column_width=True)


