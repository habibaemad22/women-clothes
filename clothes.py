
import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('cleaned_df.csv',index_col=0)

bins = [0, 30, 50, 100]
labels = ['Young', 'Middle-Aged', 'Senior']
df['AgeGroup'] = pd.cut(df['age'], bins=bins, labels=labels)

page = st.sidebar.selectbox(
    "Select a Page",
    ["🏠 Home", "📚 Intro", "📈 Univariate", "🔀 Bivariate", "📊 Multivariate"]
)


if page == "🏠 Home":
    st.title("👗 Women's Clothing E-Commerce Reviews Dataset")
    st.image("https://cdn.vectorstock.com/i/1000v/34/56/womens-clothes-word-concepts-banner-vector-28883456.jpg", caption="Customer Reviews", use_container_width=True)
    st.write("""
    Welcome to the E-Commerce Clothing Reviews Dashboard!  
    Explore the dataset, perform interactive univariate, bivariate, and multivariate analysis.
    """)



elif page == "📚 Intro":
    st.title("📚 Dataset Overview")
    st.write(df.head())

    st.subheader("Column Descriptions")
    columns = {
        "Clothing ID": "Unique ID for each product",
        "Age": "Age of the reviewer",
        "Title": "Short summary of the review",
        "Review Text": "Full text of the review",
        "Rating": "Product rating (1-5)",
        "Recommended IND": "Indicates if reviewer recommends the product",
        "Positive Feedback Count": "Number of positive feedbacks (likes)",
        "Division Name": "Broad category",
        "Department Name": "Department (e.g. Tops, Dresses)",
        "Class Name": "Product class (e.g. Blouses, Pants)"
    }

    for col, desc in columns.items():
        st.write(f"**{col}**: {desc}")


elif page == "📈 Univariate":
    st.title("📈 Univariate Analysis")
    fig1 = px.histogram(df, x='rating', title='Product Ratings Distribution')
    st.plotly_chart(fig1)
    fig2 = px.histogram(df, x='class_name', title='Most Popular Product Classes')
    st.plotly_chart(fig2)



elif page == "🔀 Bivariate":
    st.title("🔀 Bivariate Analysis")

    st.subheader("Age vs Rating")
    fig1 = px.box(df, x='rating', y='age', title='Age by Rating')
    st.plotly_chart(fig1)

    st.subheader("Department vs Recommendation")
    dept_crosstab = pd.crosstab(df['department_name'], df['recommended_ind'])
    fig2 = px.bar(dept_crosstab, barmode='stack', title='Recommendation by Department')
    st.plotly_chart(fig2)


elif page == "📊 Multivariate":
    st.title("📊 Multivariate Analysis")



    st.subheader("Department × Rating × Recommendation")
    grouped = df.groupby(['department_name', 'rating', 'recommended_ind']).size().reset_index(name='Count')
    fig2 = px.bar(
        grouped,
        x='department_name',
        y='Count',
        color='rating',
        barmode='group',
        facet_col='recommended_ind',
        title='Ratings and Recommendation by Department'
    )
    st.plotly_chart(fig2)
