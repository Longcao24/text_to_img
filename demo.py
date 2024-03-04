# đang test được
import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image
import numpy as np
from pathlib import Path
import io
import google.generativeai as genai

# from IPython.display import Image
# from IPython.display import Markdown
# from IPython.core.display import HTML


genai.configure(api_key="AIzaSyBd7Nzs86buJDk4MRo6xndb1X_vZ0cwDTA")

## Function to load OpenAI model and get respones


##initialize our streamlit app

st.set_page_config(page_title="Đọc ảnh")

generation_config = {
  "temperature": 0.4,
  "top_p": 1,
  "top_k": 32,
  "max_output_tokens": 4096,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]



st.title("Menu:")
uploaded_img = st.file_uploader("Tải ảnh cần mô tả lên (lưu ý: dung lượng file dưới 4mb)", type=["jpg", "png", "jpeg"], accept_multiple_files=False)

if uploaded_img is not None:    
    img = Image.open(uploaded_img)
    st.image(uploaded_img)
    
else:
    st.write("vui lòng upload file")

model = genai.GenerativeModel("gemini-pro-vision")

st.header("Mô tả hình ảnh")

input_request = st.text_input("Nhập yêu cầu", key="input")
submit = st.button("Submit")

if submit:
        # print(PIL.Image.__file__)
        # st.image(img, caption="Ảnh đã tải lên")
    st.subheader("Đang xử lý...")
        # img_bytes = io.BytesIO()
        # img.save(img_bytes, format=img.format)
        # img_data = img_bytes.getvalue()
    response = model.generate_content([input_request,img])
    response.resolve()
    st.write(response.text)