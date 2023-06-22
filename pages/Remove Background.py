import streamlit as st 
from PIL import Image 
from rembg import remove
st.title("Remove Image Background")
def main():
    image = st.file_uploader(label = "",type=['png','jpg','jpeg'])
    submit = st.button("Remove Background")
    if submit:
        remove_func(image)

def remove_func(input_image): 
    if input_image is not None:
        input_image = Image.open(input_image) 
        output=remove(input_image)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("Original Image")
            st.image(input_image)
        with col2:
            st.markdown("Generated Image")
            st.image(output)
        st.write("Remove background succesfully")
    else:
        st.write("Upload an Image")

if __name__ == "__main__":
  main()

