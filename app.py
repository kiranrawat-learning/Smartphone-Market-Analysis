import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
smartphones=pd.read_csv('smartphones (3).csv')
st.title("Smartphone Market Analysis")
st.sidebar.title('Select brand you want to gain insight on ')

#--------------------------------------------------------------------------------------------------------------------------------
#overall analysis
def univariate_overall_analysis():
    st.title("📊 Explore the Market Trends")
    fig, ax = plt.subplots(figsize=(7, 7))
    smartphones['budget_categorisation'].value_counts().plot(kind='pie', autopct='%1.1f%%',textprops={'fontsize': 12, 'fontweight': 'bold'})
    ax.set_title("Budget Categorisation Distribution", fontsize=14, fontweight='bold')
    st.pyplot(fig)


    st.subheader("📊 Average Price per Brand")
    avg_price = smartphones.groupby('brand_name')['price (inr)'].mean().sort_values(ascending=False)
    fig6, ax6 = plt.subplots(figsize=(13, 10))
    avg_price.plot(kind='bar', color='royalblue',ax=ax6,fontsize=15)
    ax6.set_ylabel("Average Price (INR)",fontsize=12, fontweight='bold', color='black')
    ax6.set_xlabel("Brand Name",fontsize=12, fontweight='bold', color='black')
    ax6.set_title("Average Price of Smartphones per Brand")
    plt.xticks(rotation=90)
    ax6.grid(axis='x', linestyle='--', alpha=0.7)
    st.pyplot(fig6)


    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Top Smartphone Brands (by Model Count)")
        fig1, ax1 = plt.subplots(figsize=(6, 6))
        smartphones['brand_name'].value_counts().head(5).plot(kind='pie', colormap='Set3', autopct='%0.1f%%',
                                                              textprops={'fontsize': 12, 'fontweight': 'bold'})
        st.pyplot(fig1)

    with col2:
        st.subheader("Price Distribution of Smartphones")
        fig2, ax2 = plt.subplots(figsize=(6, 6))
        sns.histplot(smartphones['price (inr)'], bins=30, kde=True, color='skyblue')
        ax2.set_xlabel("Price (INR)", fontsize=12)
        ax2.set_ylabel("Number of Models", fontsize=12)
        st.pyplot(fig2)

    with col1:
        st.subheader("5G vs Non-5G Smartphones")
        fig3, ax3 = plt.subplots(figsize=(6, 6))
        smartphones['has_5g'].value_counts().plot(kind='pie', autopct="%0.1f%%",
                                                  textprops={'fontsize': 12, 'fontweight': 'bold'})
        st.pyplot(fig3)


    with col2:
        st.subheader("NFC vs Non-NFC Smartphones")
        fig4, ax4 = plt.subplots(figsize=(6, 6))
        smartphones['has_nfc'].value_counts().plot(kind='pie', autopct="%0.1f%%",
                                                   textprops={'fontsize': 12, 'fontweight': 'bold'})
        st.pyplot(fig4)
#ram
    ram = smartphones['ram_capacity (gb)'].value_counts().reset_index()
    ram.columns = ['storage(gb)', 'count']
    ram['type'] = 'ram'
    rom = smartphones['rom_capacity (gb)'].value_counts().reset_index()
    rom.columns = ['storage(gb)', 'count']
    rom['type'] = 'Internal'
    storage = pd.concat([ram, rom], axis=0)
    fig,ax=plt.subplots(figsize=(6,4))
    sns.barplot(data=storage, x='storage(gb)', y='count', hue='type')
    ax.set_title("Storage Distribution", fontsize=12, fontweight='bold', color='black')
    st.pyplot(fig)
#camera
    brand_camera = smartphones.groupby('brand_name').agg(
        avg_rear_camera=('rear_camera (mp)', 'mean'),
        avg_front_camera=('front_camera (mp)', 'mean'),).sort_values(by='avg_rear_camera', ascending=False).reset_index()
    brand_camera_melted = brand_camera.melt(id_vars='brand_name', value_vars=['avg_rear_camera', 'avg_front_camera'],
                                            var_name='Camera Type', value_name='Average MP')
    fig, ax = plt.subplots(figsize=(12 ,10))
    sns.barplot(data=brand_camera_melted, y='brand_name', x='Average MP', hue='Camera Type', palette='Set2')
    ax.set_title("Camera Distribution by Brand", fontsize=16, fontweight='bold', color='black')
    ax.set_xlabel('Average MP', fontsize=14, fontweight='bold', color='black')
    ax.set_ylabel('Brand Name', fontsize=14, fontweight='bold', color='black')
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)

    st.pyplot(fig)

    #rating
    brand_rating = smartphones.groupby('brand_name')['rating'].mean().sort_values(ascending=False).reset_index()
    brand_rating.columns = ['brand_name', 'avg_rating']
    st.subheader("📊 Average Rating per Brand")
    fig7, ax7 = plt.subplots(figsize=(13, 10))
    sns.barplot(y=brand_rating['brand_name'], x=brand_rating['avg_rating'], palette="viridis")
    ax7.set_ylabel("Average rating", fontsize=12, fontweight='bold', color='black')
    ax7.set_xlabel("Brand Name", fontsize=12, fontweight='bold', color='black')
    ax7.set_title("Average Rating of Smartphones per Brand")
    plt.xticks(rotation=90)
    ax7.grid(axis='x', linestyle='--', alpha=0.7)
    st.pyplot(fig7)
#os
    fig8, ax8 = plt.subplots(figsize=(8, 8))
    smartphones['os'].value_counts().plot(kind='pie', autopct='%1.1f%%',textprops={'fontsize': 12, 'fontweight': 'bold'})
    ax8.set_title("Operating System Distribution", fontsize=16, fontweight='bold',)
    st.pyplot(fig8)


#-------------------------------------------------------------------------------------------------------------------------------------------
#bivariate
def bivariate_overall_analysis():
   st.title("📊 Explore the Market Trends")

   #Brand-wise Price Distribution where model count>10
   temp_df = smartphones.groupby('brand_name').count()['model']
   x = temp_df[temp_df > 10]
   temp_df = smartphones[smartphones['brand_name'].isin(x.index)]
   temp_df = temp_df.groupby('brand_name').agg(avg_price=('price (inr)', 'mean')).sort_values(by='avg_price',
                                                                                              ascending=False)
   temp_df.reset_index(inplace=True)

   fig1,ax1=plt.subplots(figsize=(15, 6))
   ax1 = sns.barplot(data=temp_df, x='brand_name', y='avg_price', palette="viridis", alpha=0.8)
   ax1.set_title("Brand-wise Price Distribution where model count>10", fontsize=14, fontweight='bold')
   ax1.set_xlabel("Brand", fontsize=12)
   ax1.set_ylabel("Price (INR)", fontsize=12)
   ax1.grid(axis='y', linestyle='--', alpha=0.7)
   st.pyplot(fig1)

   #prics vs rating
   col1,col2=st.columns(2)

   with col1:
        correlation = smartphones[['price (inr)', 'rating']].corr()
        fig2, ax2= plt.subplots(figsize=(8,8))
        sns.heatmap(correlation,annot=True,cmap='viridis')
        ax2.set_title('Price Distribution vs Rating',fontsize=14, fontweight='bold')
        st.pyplot(fig2)
   with col2:
       fig3, ax3 = plt.subplots(figsize=(8, 8))
       sns.regplot(data=smartphones, x='price (inr)', y='rating')
       ax3.set_title("Price vs Rating", fontsize=14, fontweight='bold')
       ax3.set_xlabel("Price (INR)", fontsize=12)
       ax3.set_ylabel("Rating", fontsize=12)
       ax3.grid(alpha=0.3)
       st.pyplot(fig3)

   #brand wise comparision of price if 5g or not

   temp_df = smartphones.groupby(['has_5g', 'brand_name'])['price (inr)'].mean().reset_index()

   fig4,ax4=plt.subplots(figsize=(14,6))
   sns.barplot(data=temp_df, x='brand_name', y='price (inr)',hue='has_5g', palette="viridis")
   plt.xticks(rotation=90)
   ax4.set_title("Brand-wise Price Comparison (5G vs Non-5G)", fontsize=14, fontweight='bold')
   ax4.grid(axis='y', linestyle='--', alpha=0.7)
   st.pyplot(fig4)

    #processor vs price
   with col1:
       fig5,ax5=plt.subplots(figsize=(10,10))
       sns.barplot(data=smartphones, x='processor_brand', y='price (inr)', palette='viridis')
       plt.xticks(rotation=45)
       ax5.set_title("Processor Brand vs Price", fontsize=14, fontweight='bold')
       ax5.set_ylabel("Price (INR)")
       ax5.grid(axis='y', linestyle='--', alpha=0.7)
       plt.legend(bbox_to_anchor=(1, 1), title="Brand", fontsize=10)
       st.pyplot(fig5)

   #num core vs price
   with col2:
       fig6,ax6=plt.subplots(figsize=(10,10))
       sns.barplot(data=smartphones, x='num_cores', y='price (inr)', palette='viridis', estimator=np.median)
       ax6.set_title('Processor  core vs Price',fontsize=14, fontweight='bold')
       st.pyplot(fig6)

   #storage vs price
   correlation_data = smartphones[["price (inr)", "ram_capacity (gb)", "rom_capacity (gb)"]].corr()
   fig7,ax7=plt.subplots(figsize=(6,4))
   sns.heatmap(data=correlation_data,annot=True,cmap='viridis')
   st.pyplot(fig7)

   fig8,ax8=plt.subplots(figsize=(10, 6))
   sns.scatterplot(data=smartphones, x="ram_capacity (gb)", y="price (inr)", hue="rom_capacity (gb)", palette="viridis",
                   size="rom_capacity (gb)", sizes=(20, 200))

   ax8.set_title("Price vs RAM & ROM (Color: ROM, Size: ROM)",fontsize=14, fontweight='bold')
   ax8.set_xlabel("RAM Capacity (GB)")
   ax8.set_ylabel("Price (INR)")
   plt.legend(title="ROM Capacity (GB)")
   st.pyplot(fig8)

    #corr  cameras
   correlation_matrix = smartphones[
       ['rear_camera (mp)', 'num_of_rear_cameras', 'price (inr)', 'num_of_front_cameras', 'front_camera (mp)']].corr()
   fig9,ax9=plt.subplots(figsize=(6, 4))
   sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
   ax9.set_title('Correlation between price and camera characteristics',fontsize=14, fontweight='bold')
   st.pyplot(fig9)

#------------------------------------------------------------------------------------------------------------------------------------------
#brand wise
def brand_wise_analysis():
    st.title(selected_brand+" Wise Analysis")
    brand_data = smartphones[smartphones['brand_name'] == selected_brand]
#analysis
    fig, ax = plt.subplots(figsize=(7, 7))
    brand_data['budget_categorisation'].value_counts().plot(kind='pie', autopct='%1.1f%%',textprops={'fontsize': 12, 'fontweight': 'bold'})
    ax.set_title("Budget Categorisation Distribution for --> "+selected_brand, fontsize=14, fontweight='bold')
    st.pyplot(fig)



    st.subheader("Price Distribution of "+selected_brand+" Smartphones")
    fig1, ax1 = plt.subplots(figsize=(6, 6))
    sns.histplot(brand_data['price (inr)'], bins=30, kde=True, color='skyblue')
    ax1.set_xlabel("Price (INR)", fontsize=12)
    ax1.set_ylabel("Number of Models", fontsize=12)
    st.pyplot(fig1)

    col1,col2=st.columns(2)
    with col1:
        st.subheader("5G vs Non-5G  "+selected_brand+" Smartphones")
        fig2, ax2 = plt.subplots(figsize=(6, 6))
        brand_data['has_5g'].value_counts().plot(kind='pie', autopct="%0.1f%%",textprops={'fontsize': 12, 'fontweight': 'bold'})
        st.pyplot(fig2)
    with col2:
        st.subheader("NFC vs Non-NFC "+selected_brand+" Smartphones")
        fig3, ax3 = plt.subplots(figsize=(6, 6))
        brand_data['has_nfc'].value_counts().plot(kind='pie', autopct="%0.1f%%",
                                                   textprops={'fontsize': 12, 'fontweight': 'bold'})
        st.pyplot(fig3)



    st.subheader("IR blaster vs Non-IR "+selected_brand+" Smartphones")
    fig4, ax4= plt.subplots(figsize=(4, 2))
    brand_data['has_ir_blaster'].value_counts().plot(kind='pie', autopct="%0.1f%%",
                                                     textprops={'fontsize': 12, 'fontweight': 'bold'})
    st.pyplot(fig4)


#processsor
    processor_count = brand_data['processor_brand'].value_counts().reset_index()
    processor_count.columns = ['Processor Brand', 'Number of Models']
    fig5, ax5 = plt.subplots(figsize=(8,4))
    sns.barplot( x=processor_count['Processor Brand'], y=processor_count['Number of Models'], palette='viridis')
    plt.xticks(rotation=45)
    ax5.set_title("Distribution of Processor in " +selected_brand +" Smartphones", fontsize=14, fontweight='bold')
    ax5.set_ylabel("Number of Models")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.legend(bbox_to_anchor=(1, 1), title="Brand", fontsize=10)
    st.pyplot(fig5)
#ram
    ram_count = brand_data['ram_capacity (gb)'].value_counts().reset_index()
    ram_count.columns = ['Storage (GB)', 'Number of Models']
    ram_count['type'] = 'RAM Capacity (GB)'

    rom_count = brand_data['rom_capacity (gb)'].value_counts().reset_index()
    rom_count.columns = ['Storage (GB)', 'Number of Models']
    rom_count['type'] = 'Internal Storage'
    storage = pd.concat([ram_count, rom_count])

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(data=storage, x='Storage (GB)', y='Number of Models', hue='type',
                palette={"RAM Capacity (GB)": "grey", "Internal Storage": "skyblue"})
    ax.set_title("Distribution of RAM Capacities in "+selected_brand +" Smartphones", fontsize=14, fontweight='bold')
    ax.set_xlabel("RAM Capacity (GB)")
    ax.set_ylabel("Number of Models")
    plt.xticks(rotation=45)
    st.pyplot(fig)


#camera
    front_camera = brand_data['front_camera (mp)'].value_counts().reset_index()
    front_camera.columns = ['Camera (MP)', 'Number of Models']
    front_camera['Type'] = 'Front Camera'

    rear_camera = brand_data['rear_camera (mp)'].value_counts().reset_index()
    rear_camera.columns = ['Camera (MP)', 'Number of Models']
    rear_camera['Type'] = 'Rear Camera'


    camera_data = pd.concat([front_camera, rear_camera])

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=camera_data, x='Camera (MP)', y='Number of Models', hue='Type',
                palette={"Front Camera": "red", "Rear Camera": "blue"})

    ax.set_title("Distribution of Front & Rear Cameras in "+selected_brand+ " Smartphones", fontsize=14, fontweight='bold')
    ax.set_xlabel("Camera Megapixels (MP)")
    ax.set_ylabel("Number of Models")
    plt.xticks(rotation=45)

    st.pyplot(fig)









#----------------------------------------------------------------------------------------------------------------------------------
#model specification
def model_specification():
    brand_data = smartphones[smartphones['brand_name'] == selected_brand]
    st.title(selected_model+" Detailed Information")
    specification=brand_data[brand_data['model'] == selected_model]
    specification=specification.T
    specification.reset_index(inplace=True)
    specification.columns = ['Attribute', 'Value']
    st.table(specification)




option= st.sidebar.selectbox("Choose Analysis Type:", ["Select","📊 Overview", "🏢 Brand Analysis"])

if option=="📊 Overview":
    option1=st.sidebar.radio("Analysis Type:",["Univariate","Bivariate"])
    if option1=="Univariate":
        b0=st.sidebar.button("Market Overview (Univariate)")
        if b0:
            univariate_overall_analysis()
    elif option1=="Bivariate":
        b0 = st.sidebar.button("Market Overview (Bivariate)")
        if b0:
            bivariate_overall_analysis()



elif option == "🏢 Brand Analysis":
    selected_brand = st.sidebar.selectbox("Choose brand name", ["Select"] + sorted(smartphones['brand_name'].unique().tolist()))
    b1 =st.sidebar.button("Brand-wise Analysis")
    if b1 and selected_brand !="Select":
        brand_wise_analysis()




    brand_models = smartphones.groupby('brand_name')['model'].apply(list).get(selected_brand, [])
    selected_model = st.sidebar.selectbox("Choose model:", ["Select"] + brand_models)
    b2=st.sidebar.button("Model Specification")
    if b2:
        model_specification()

