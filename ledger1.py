import streamlit as st
import pandas as pd
import os

# File path for storing the ledger
CSV_FILE = "mobile_recharge_ledger.csv"

# Function to load the data from the CSV file
def load_ledger():
    if os.path.exists(CSV_FILE):
        return pd.read_csv(CSV_FILE)
    else:
        # If file doesn't exist, return an empty DataFrame
        return pd.DataFrame(columns=["User Name", "Recharge Amount", "Recharge Plan", "Date of Recharge"])

# Function to save data to the CSV file
def save_ledger(df):
    df.to_csv(CSV_FILE, index=False)

# Function to add a new recharge record
def add_mobile_recharge(user_name, recharge_amount, recharge_plan, date_of_recharge):
    # Load the existing ledger
    ledger = load_ledger()
    
    # Create a new record
    new_record = {
        "User Name": user_name,
        "Recharge Amount": recharge_amount,
        "Recharge Plan": recharge_plan,
        "Date of Recharge": str(date_of_recharge)
    }
    
    # Append the new record to the ledger (use pd.concat() instead of append())
    ledger = pd.concat([ledger, pd.DataFrame([new_record])], ignore_index=True)
    
    # Save the updated ledger back to the CSV
    save_ledger(ledger)

# Streamlit app title and description
st.title("Mobile Recharge Ledger")
st.markdown("""
This app allows you to record and view mobile recharge details. The records are saved in a CSV file.
""")

# Input fields for adding recharge records
st.subheader("Add a Recharge Record")

user_name = st.text_input("User Name", "Ajoy Jayarajan")
recharge_amount = st.number_input("Recharge Amount", min_value=0, step=1, value=299)
recharge_plan = st.selectbox("Recharge Plan", ["Data Pack", "Unlimited Pack", "Talktime Pack"])
date_of_recharge = st.date_input("Date of Recharge", value="2025-04-25")

if st.button("Add Recharge"):
    add_mobile_recharge(user_name, recharge_amount, recharge_plan, date_of_recharge)
    st.success(f"Recharge done for {user_name} on {date_of_recharge}: {recharge_plan} plan costing {recharge_amount}.")

# Displaying the mobile recharge ledger
st.subheader("Mobile Recharge Ledger")

# Load and display the ledger from the CSV file
ledger = load_ledger()

# Check if the ledger has any records
if not ledger.empty:
    st.write(ledger)
else:
    st.write("No recharge records added yet.")
