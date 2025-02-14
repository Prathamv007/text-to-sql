import streamlit as st
import google.generativeai as genai
from sqlalchemy import create_engine, text
import sqlite3
import pandas as pd
import re

# Set up Gemini API Key
genai.configure(api_key="your-gemini-api-key")  # Replace with your actual key

# Create SQLite engine and connection
engine = create_engine("sqlite:///users.db")

# Sample data for demonstration (Run this only once to create the table)
def create_sample_data():
    with engine.connect() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT,
                city TEXT
            )
        """))
        conn.execute(text("""
            INSERT INTO users (name, email, city) VALUES
            ('Alice Johnson', 'alice@example.com', 'New York'),
            ('Bob Smith', 'bob@example.com', 'San Francisco'),
            ('Charlie Brown', 'charlie@example.com', 'New York')
        """))
        conn.commit()

#create_sample_data()

# Function to clean SQL output from Gemini
def clean_sql_output(sql_text):
    return re.sub(r"```sql|```", "", sql_text).strip()

# Use Gemini to generate SQL query
def generate_sql(natural_query):
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"Convert the following text into an SQL query for a SQLite database:\n\n'{natural_query}'"

    response = model.generate_content(prompt)
    return clean_sql_output(response.text.strip())

# Streamlit UI
st.title("📝 Text-to-SQL Converter")
st.markdown("Convert natural language statements into SQL queries and fetch data!")

# User Input
user_query = st.text_input("Enter your query (e.g., 'Show names and emails of users in New York'):")

if st.button("Generate SQL & Fetch Data"):
    if user_query:
        # Generate SQL query
        sql_query = generate_sql(user_query)
        st.subheader("🛠️ Generated SQL Query:")
        st.code(sql_query, language="sql")

        try:
            # Execute the query
            with engine.connect() as connection:
                result = connection.execute(text(sql_query))
                rows = result.fetchall()
                columns = result.keys()
                
            # Display results
            if rows:
                df = pd.DataFrame(rows, columns=columns)
                st.subheader("📊 Query Results:")
                st.dataframe(df)
            else:
                st.info("No records found.")
        except Exception as e:
            st.error(f"❌ Error executing SQL: {e}")
    else:
        st.warning("Please enter a query!")

