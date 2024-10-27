import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px 
from PIL import Image

df3 = pd.read_csv("C:/Users/LENOVO/OneDrive/Desktop/Tuwaiqpro/Usecase-6-Project-3/data/RiyadhVillasAqar.csv")
ra = pd.read_csv(r"C:\Users\LENOVO\OneDrive\Desktop\Tuwaiqpro\Usecase-6-Project-3\data\realEstate.csv")
st.markdown(
    """
    <style>
    body {
        background-color: #D3D3D3;  /* لون خلفية رمادي فاتح */
    }
    </style>
    """,
    unsafe_allow_html=True
)

image_path = r"C:\Users\LENOVO\OneDrive\Desktop\Tuwaiqpro\Usecase-6-Project-3\pic\king.png"  
image = Image.open(image_path)

st.image(image, use_column_width=True)
st.markdown(
    """
    <h1 class='title' style='text-align: right; direction: rtl;'>نظرة في عقار العاصمة: اين تسكن في مدينة <span style='color: #003366;'>المستقبل؟</span></h1>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <div style='text-align: center; font-size: 16px; color: black;'>
       رحلة البحث عن سكن مناسب في الرياض قد تكون من أصعب التجارب، كثرة الخيارات والتنافس الشديد بينهما قد يجعلك تقف حائرا في مكان واحد 
        نختصر عليك عناء البحث ونجاوب على كل سؤال قد يتبادر الى ذهنك ببيانات حقيقية من عقارات الرياض
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br><br><br>", unsafe_allow_html=True)


st.markdown(
    """
    <div style='text-align: right; font-size: 24px; color: black; direction: rtl;'>
        <span style='color: black; font-weight: bold; font-size: 24px;'>من شرق الرياض إلى غربها</span>: 
        <span style='font-weight: normal; font-size: 16px;'> مقارنة بين متوسط أسعار العقارات حسب المنطقة</span>
        <br><br>
    </div>
    """,
    unsafe_allow_html=True
)


df3=df3.rename(columns={
    'front': 'الواجهة',
    'rooms': 'الغرف',
    'lounges': 'الصالات',
    'bathrooms': 'الحمامات',
    'streetWidth': 'عرض الشارع',
    'stairs': 'الدرج',
    'propertyAge': 'عمر العقار',
    'driverRoom': 'غرفة السائق',
    'tent': 'الخيمة',
    'patio': 'الفناء',
    'kitchen': 'المطبخ',
    'outdoorRoom': 'غرفة خارجية',
    'garage': 'الكراج',
    'duplex': 'دوبلكس',
    'space': 'المساحة',
    'apartments': 'الشقق',
    'maidRoom': 'غرفة الخادمة',
    'elevator': 'المصعد',
    'furnihsed': 'مفروشة',
    'pool': 'المسبح',
    'basement': 'البدروم',
    'neighbourhood': 'الحي',
    'location': 'الموقع',
    'price': 'السعر',
    'square price': 'سعر المتر المربع'
})



# Group the data by the location column
grouped = df3.groupby('الموقع')

# Calculate the mean price for each location group
mean_prices = grouped['السعر'].mean().reset_index()

# Plot the mean prices as a bar chart using Plotly
fig = px.bar(
    mean_prices,
    x='الموقع',
    y='السعر',
    title='متوسط السعر على حسب الجهة',
    labels={'السعر': 'السعر', 'الموقع': 'الموقع'},
)

# Update layout for better visualization
fig.update_layout(
    xaxis_title='الموقع',
    yaxis_title='السعر',
    xaxis_tickangle=-75,
    height=400,
    width=800,
)

# Show the figure
st.plotly_chart(fig, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    """
    <div style='text-align: right; font-size: 24px; color: black; direction: rtl;'>
        <span style='color: black; font-weight: bold; font-size: 24px;'>جولة في أحياء الرياض</span>: 
        <span style='font-weight: normal; font-size: 16px;'>كيف تختار بوعي بناء على متوسط الأسعار</span>
        <br><br>
    </div>
    """,
    unsafe_allow_html=True
)

column_mapping = {
    'price': 'السعر',
    'refresh': 'تاريخ التحديث',
    'beds': 'غرف النوم',
    'livings': 'غرف المعيشة',
    'wc': 'الحمام',
    'area': 'المساحة',
    'street_width': 'عرض الشارع',
    'age': 'العمر',
    'latest update': 'اخر تحديث',
    'ac': 'مكيفات',
    'furnished': 'مفروشة',
    'district': 'الحي',
    'width': 'العرض',
    'length': 'الطول',
    'advertiser_type': 'نوع المعلن',
    'creation date': 'تاريخ الإنشاء',
    'review': 'مراجعة',
    'IsRent': 'للإيجار'
}

# Renaming the columns
ra.rename(columns=column_mapping, inplace=True)

# Display the modified DataFrame
print(ra.columns)





# Calculate average prices by district
average_prices = ra.groupby('الحي')['السعر'].mean().reset_index()

# Create a bar chart using Plotly
fig = px.bar(
    average_prices, 
    x='الحي', 
    y='السعر', 
    title='متوسط الأسعار حسب الأحياء',
    labels={'السعر': 'متوسط السعر', 'الحي': 'الحي'},
    color='السعر',  # Color by average price for better visualization
    color_continuous_scale=['#00BFFF', '#DDA0DD', '#0033CC']
)

fig.update_layout(
    width=800,  # يمكنك تعديل هذا الرقم حسب الحاجة
    height=400,  # يمكنك تعديل هذا الرقم حسب الحاجة
)
# Show the figure
st.plotly_chart(fig, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    """
    <div style='text-align: right; font-size: 24px; color: black; direction: rtl;'>
        <span style='color: black; font-weight: bold; font-size: 24px;'>بين العمر والسعر</span>: 
        <span style='font-weight: normal; font-size: 16px;'>لرياض تتطور بسرعة كل يوم، عندك فضول تعرف كيف تتفاوت اسعار العقارات حسب حداثتها؟</span>
        <br><br>
    </div>
    """,
    unsafe_allow_html=True
)

# Create a scatter plot to show the relationship between age and price
fig = px.scatter(
    ra, 
    x='العمر', 
    y='السعر', 
    title='تأثير العمر على السعر',
    labels={'العمر': 'العمر', 'السعر': 'السعر'},
    color='الحي'  # Optionally color by district for additional context
)

fig.update_layout(
    width=800,  # يمكنك تعديل هذا الرقم حسب الحاجة
    height=400,  # يمكنك تعديل هذا الرقم حسب الحاجة
)

# Show the figure
st.plotly_chart(fig, use_container_width=True)



# Dropdown for selecting district
selected_district = st.selectbox(
    'اختر الحي:',
    ra['الحي'].unique()  # قائمة بالأحياء الفريدة
)

# Filter data based on selected district
filtered_data = ra[ra['الحي'] == selected_district]

# Calculate price range
min_price = filtered_data['السعر'].min()
max_price = filtered_data['السعر'].max()

# Display the price range without "حي" أو "البيانات"
st.write(f"أسعار العقارات في {selected_district} تتراوح بين: {min_price:.2f} إلى {max_price:.2f}")

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    """
    <div style='text-align: right; font-size: 20px; color: black; direction: rtl;'>
        <span style='color: #003366; font-weight: bold;'>استثمر</span> وقتك في فهم أسعار العقارات في الأحياء المختلفة، واختَر سكنك بعناية بما يتناسب مع ميزانيتك واحتياجاتك.
    </div>
    """,
    unsafe_allow_html=True
)



