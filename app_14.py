import streamlit as st
import pickle

st.title('Crop prediction syatem')
model = pickle.load(open('model_12.pkl','rb'))

col_1,col_2 = st.columns(2)
n = col_1.number_input("Enter nitrogen: ")
p = col_2.number_input("Enter phosporus: ")
k = col_1.number_input("Enter potassium: ")
t = col_2.number_input("ENter temperature: ")
h = col_1.number_input("Enter humidity: ")
ph = col_2.number_input("Enter ph: ")
r = col_1.number_input("Enter rainfall: ")

if st.button('Predict'):
    data = [[n,p,k,t,h,ph,r]]
    result = model.predict(data)[0]
    st.success(result)

