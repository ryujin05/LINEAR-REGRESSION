import streamlit as st
from predict import model  # Import model từ predict.py



st.title("🏠 Dự Báo Giá Nhà")

dien_tich = st.number_input("Diện tích (m²)", min_value=10, value=75)
so_phong = st.number_input("Số phòng ngủ", min_value=1, value=2)

if st.button("Dự báo"):
    gia = model.predict([[dien_tich, so_phong]])[0]
    st.success(f"💰 Giá dự báo: **{gia:,.0f} triệu đồng**")
