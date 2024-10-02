import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

#Load dataframe
merged_df = pd.read_csv("./main_data.csv", parse_dates=['Date'])
Changping = pd.read_csv("PRSA_Data_Changping_20130301-20170228.csv")
Changping['Date'] = pd.to_datetime(Changping[['year', 'month', 'day']])
Guanyuan = pd.read_csv("PRSA_Data_Guanyuan_20130301-20170228.csv")
Guanyuan['Date'] = pd.to_datetime(Guanyuan[['year', 'month', 'day']])

#Sort the dataframe by 'Date' and reset the index
merged_df.sort_values(by='Date', inplace=True)
merged_df.reset_index(inplace=True)

#Get the minimum and maximum dates
min_date = merged_df['Date'].min().date()
max_date = merged_df['Date'].max().date()

with st.sidebar:
    #menambahkan logo perusahaan
    st.image("https://icons.veryicon.com/png/o/object/warning-icon/air-pollution.png")
    selected_year = st.sidebar.selectbox('Select Year', list(merged_df['Date'].dt.year.unique()))
    selected_month = st.sidebar.selectbox('Select Month', list(merged_df['Date'].dt.month.unique()))

#PM2.5 Changping
st.header("Air Quality level (PM2.5) in Changping")
fig, ax = plt.subplots()
ax.plot(Changping['Date'], Changping['PM2.5'])
plt.xlabel('Date')
plt.ylabel('PM2.5 Concentration')
plt.title('Yearly PM2.5 Levels') 
st.pyplot(fig)

#PM2.5 Guanyuan
st.header("Air Quality level (PM2.5) in Guanyuan")
fig, ax = plt.subplots()
ax.plot(Guanyuan['Date'], Guanyuan['PM2.5'])
plt.xlabel('Date')
plt.ylabel('PM2.5 Concentration')
plt.title('Yearly PM2.5 Levels in Guanyuan')
st.pyplot(fig)

#Temperature Changping
st.header ("Temperatur in Changping")
fig, ax = plt.subplots()
ax.plot(Changping['Date'], Changping['TEMP'], label='Changping', color='green')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Yearly Temperature in Changping')
st.pyplot(fig)

#Temperature Guanyuan
st.header("Temperature in Guanyuan")
fig, ax = plt.subplots()
ax.plot(Guanyuan['Date'], Guanyuan['TEMP'], label='Guanyuan', color='orange')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Yearly Temperature in Guanyuan')
st.pyplot(fig)

#Polutant Changping
st.header("Polutant Changping City")
#Subplot untuk setiap polutant
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

#boxplot untuk setiap polutant

sns.boxplot(x='month', y='PM2.5', data=Changping, ax=axes[0, 0])
axes[0, 0].set_title('PM2.5 Distribution')

sns.boxplot(x='month', y='PM10', data=Changping, ax=axes[0, 1])
axes[0, 1].set_title('PM10 Distribution')

sns.boxplot(x='month', y='SO2', data=Changping, ax=axes[0, 2])
axes[0, 2].set_title('SO2 Distribution')

sns.boxplot(x='month', y='NO2', data=Changping, ax=axes[1, 0])
axes[1, 0].set_title('NO2 Distribution')

sns.boxplot(x='month', y='CO', data=Changping, ax=axes[1, 1])
axes[1, 1].set_title('CO Distribution')

# Remove the empty subplot
fig.delaxes(axes[1, 2])

#Polutant Guanyuan
st.header("Polutant Guanyuan City")
#Subplot untuk setiap polutant
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

#boxplot untuk setiap polutant
sns.boxplot(x='month', y='PM2.5', data=Guanyuan, ax=axes[0, 0])
axes[0, 0].set_title('PM2.5 Distribution')

sns.boxplot(x='month', y='PM10', data=Guanyuan, ax=axes[0, 1])
axes[0, 1].set_title('PM10 Distribution')

sns.boxplot(x='month', y='SO2', data=Guanyuan, ax=axes[0, 2])
axes[0, 2].set_title('SO2 Distribution')

sns.boxplot(x='month', y='NO2', data=Guanyuan, ax=axes[1, 0])
axes[1, 0].set_title('NO2 Distribution')

sns.boxplot(x='month', y='CO', data=Guanyuan, ax=axes[1, 1])
axes[1, 1].set_title('CO Distribution')

# Remove the empty subplot
fig.delaxes(axes[1, 2])


# Adjust layout and show the plot
plt.tight_layout()
plt.show()
st.pyplot(fig)