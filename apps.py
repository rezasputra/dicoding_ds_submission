import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st

data = pd.read_csv('day.csv')

# Assess
data['season'] = data['season'].astype('str')

trend_month = data[['mnth', 'registered']].groupby(by='mnth', as_index=False).sum()
trend_month['mnth'] = trend_month['mnth'].astype('int')
trend_month.sort_values(by='mnth', inplace = True)


st.header('Dashboard Penyewaan Sepeda :sparkles:')
st.write('Dashboard ini menampilkan overview dari stasiun penyewaan Sepeda')
st.write('Data menggunakan [Bike Sharing Dataset](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset/data)')



# Sidebar
with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    
    # Mengambil start_date & end_date dari date_input
    st.write("Halo nama Saya Reza Syahputra")


# Main Page 
st.subheader('Jumlah Penyewa')
col1, col2, col3 = st.columns(3)
with col1:
    total_all = data.cnt.sum()
    st.metric("Total Keseluruhan", value=str(total_all))
 
with col2:
    total_regist = data.registered.sum()
    st.metric("Total Registered", value=str(total_regist))

with col3:
    total_casual = data.casual.sum()
    st.metric("Total Walk In", value=str(total_casual))






fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 15))
 
colors = ["#D3D3D3", "#D3D3D3","#90CAF9", "#D3D3D3"]
colorss = ["#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3","#90CAF9"]
 
sns.barplot(x="season", y="cnt", data=data, palette=colors, ax=ax[0])
ax[0].set_ylabel("Jumlah Sepeda", fontsize=30)
ax[0].set_xlabel("Season", fontsize=30)
ax[0].set_title("Trend Berdasarkan Seasons", loc="center", fontsize=50)
ax[0].tick_params(axis='y', labelsize=35)
ax[0].tick_params(axis='x', labelsize=30)
 
sns.barplot(x="mnth", y="registered", data=trend_month, palette=colorss, ax=ax[1])
ax[1].set_ylabel('Jumlah Sepeda')
ax[1].set_xlabel("Bulan", fontsize=30)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Trend Sewa Sepeda Berdasarkan Bulan", loc="center", fontsize=50)
ax[1].tick_params(axis='y', labelsize=35)
ax[1].tick_params(axis='x', labelsize=30)
 
st.pyplot(fig)