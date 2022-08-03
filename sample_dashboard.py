import streamlit as st

st.set_page_config(
    page_title="Example Title",
    layout='wide',
)

img_container = st.container()

img_container.warning("upload an image to display here")

file = st.sidebar.file_uploader("Select an image", type=['png','jpg','gif','webp'])
if file:
    st.snow()
    img_container.image(file)
    img_container.success(f"you have uploaded {file.name}")
    img_container.success(f'TYPE : {file.type}')