import streamlit as st
import joblib
import pandas as pd
model = joblib.load('house_model.pkl')
features = joblib.load('features_list.pkl')
st.title("Dự báo giá nhà")
st.subheader("Nhập thông tin căn hộ")
gr_liv_area=st.number_input("Diện tích phòng khác",value =1500)
overall_qual=st.slider("Chất lượng",1,10,5)
bedrooms=st.number_input("Số phòng ngủ",1,10,3)
bathrooms=st.number_input("Số phòng tắm",1,10,2)
input_df = pd.DataFrame([[gr_liv_area, bedrooms, bathrooms, overall_qual]],
columns=features)
prediction = model.predict(input_df)[0]
st.success(f" Giá nhà dự báo: {prediction:,.2f}")