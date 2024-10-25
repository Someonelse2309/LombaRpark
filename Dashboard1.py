import streamlit as st
from GetData1 import Show_Data as SD
import shutil
import os

getData = SD()
st.title("Dashboard ROPI - FTI UKDW")
tabVisual, tabUpload= st.tabs(["Visualisasi Data","Upload Iklan (local host only)"])

CWD = os.getcwd()

def create_dirs():
    for i in ['Pria', 'Wanita']:
        for j in ['1-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80']:
            try:
                os.makedirs(os.path.join(CWD,"Iklan",i, j), exist_ok=True)
            except Exception as e:
                print(e)

with tabVisual:
    tabAge, tabEmotion, tabGender, tabAE, tabAG, tabGE = st.tabs(["Age", "Emotion", "Gender", "Age & Emotion", "Age & Gender", "Emotion & Gender"])

    with tabAge:
        st.title("Age")
        st.header("Age Bar Chart")
        st.pyplot(getData.show_age_bar())
        st.header("Age Pie Chart")
        st.pyplot(getData.show_age_pie())

    with tabGender:
        st.title("Gender")
        st.header("Gender Bar Chart")
        st.pyplot(getData.show_gender_bar())
        st.header("Gender Pie Chart")
        st.pyplot(getData.show_gender_pie())

    with tabEmotion:
        st.title("Emotion")
        st.header("Emotion Bar Chart")
        st.pyplot(getData.show_emotion_bar())
        st.header("Emotion Pie Chart")
        st.pyplot(getData.show_emotion_pie())

    with tabAE:
        st.header("Age & Emotion")
        st.pyplot(getData.show_age_emotion_bar())

    with tabAG:
        st.header("Age & Gender")
        st.pyplot(getData.show_age_gender_bar())

    with tabGE:
        st.header("Emotion & Gender")
        st.pyplot(getData.show_emotion_gender_bar())

with tabUpload:

    fileupload = st.file_uploader("Masukan Iklan Anda")
    st.header("Detail Iklan")
    target_gender = st.multiselect(
        label = "Silahkan masukan target gender iklan anda",
        options = ('Pria','Wanita'),
    )
    target_usia = st.multiselect(
        label="Silahkan masukan target usia iklan anda",
        options=('1-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80'),
    )
    if st.button("Upload Data"):
        if fileupload is None:
            st.write("No file uploaded.")
        else:
            create_dirs()
            filename = fileupload.name
            with open(os.path.join(CWD, filename), "wb") as f:
                f.write(fileupload.getbuffer())

            source = os.path.join(CWD, filename)
            for i in target_gender:
                for j in target_usia:
                    shutil.copy(source, os.path.join(CWD,"Iklan", i, j, filename))
            os.remove(os.path.join(CWD, filename))
            st.success(f"Data '{filename}' berhasil ditambahkan")