📝 Text-to-SQL using LangChain & Streamlit

This project allows users to input natural language queries, convert them into SQL, and execute them using an SQLite database. It provides a Streamlit UI for user-friendly interaction.

🚀 Features

✅ Convert natural language queries into SQL statements✅ Execute SQL queries on a local SQLite database✅ Display SQL queries and results in a Streamlit UI✅ Easy setup with a local database

📌 Installation and Setup

🔹 Step 1: Clone the Repository

git clone https://github.com/Prathamv007/text-to-sql.git
cd text-to-sql

🔹 Step 2: Create a Virtual Environment

python -m venv venv

Activate the Virtual Environment:

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate

🔹 Step 3: Install Dependencies

pip install -r requirements.txt

🔹 Step 4: Set Up the Database

Before running the app, initialize the database by executing:

python setup_db.py

This will create the required SQLite database and tables.

⚡ Running the Project

▶️ Start the Streamlit App

streamlit run app.py

This will launch the web UI in your browser. 🎉

📂 Project Structure

text-to-sql/
│── app.py                # Streamlit app for user interaction
│── setup_db.py           # Script to create SQLite database & tables
│── query_sql.py          # Generates SQL queries from natural language
│── requirements.txt      # List of dependencies
│── README.md             # Project documentation
└── venv/                 # Virtual environment (optional)

🛠 Git Workflow

✅ Adding & Committing Changes

git add .
git commit -m "Your commit message"

🔄 Pull Latest Changes from Remote

git pull origin main --rebase

🚀 Push Your Code to GitHub

git push origin main

🔄 Fixing Git Issues

❌ If Push is Rejected (Remote Has New Changes)

git pull origin main --rebase
git push origin main

❌ If You Want to Undo Your Last Commit (Before Pushing)

git reset --soft HEAD~1

This removes the commit but keeps the changes.

❌ If You Need to Force Push (Use Carefully)

git push --force

⚠️ This overwrites remote changes, be careful!

📌 Contributing

Feel free to open issues or submit PRs if you’d like to contribute. 🚀

📜 License

This project is open-source and available under the MIT License.

Happy Coding! 🎯

