import streamlit as st

# Initialize an empty mobile recharge ledger
mobile_recharge_ledger = {}

# Function to add or update mobile recharge records
def add_mobile_recharge(user_name, recharge_amount, recharge_plan, date_of_recharge):
    # If user is not already in the ledger, add them
    if user_name not in mobile_recharge_ledger:
        mobile_recharge_ledger[user_name] = []

    # Add a recharge record for the user
    recharge = {
        "Recharge Amount": recharge_amount,
        "Recharge Plan": recharge_plan,
        "Date of Recharge": date_of_recharge
    }
    mobile_recharge_ledger[user_name].append(recharge)

# Streamlit app title and description
st.title("Mobile Recharge Ledger")
st.markdown("""
This app allows you to record and view mobile recharge details. You can add a recharge record and see the full ledger below.
""")

# Input fields for adding recharge records
st.subheader("Add a Recharge Record")

user_name = st.text_input("User Name", "Ajoy Jayarajan")
recharge_amount = st.number_input("Recharge Amount", min_value=0, step=1, value=299)
recharge_plan = st.selectbox("Recharge Plan", ["Data Pack", "Unlimited Pack", "Talktime Pack"])
date_of_recharge = st.date_input("Date of Recharge", value="2025-04-25")

if st.button("Add Recharge"):
    add_mobile_recharge(user_name, recharge_amount, recharge_plan, str(date_of_recharge))
    st.success(f"Recharge done for {user_name} on {date_of_recharge}: {recharge_plan} plan costing {recharge_amount}.")

# Displaying the mobile recharge ledger
st.subheader("Mobile Recharge Ledger")

# Check if the ledger is empty
if mobile_recharge_ledger:
    for user, recharges in mobile_recharge_ledger.items():
        st.write(f"### {user}")
        for recharge in recharges:
            st.write(f"**Recharge Amount**: {recharge['Recharge Amount']}")
            st.write(f"**Recharge Plan**: {recharge['Recharge Plan']}")
            st.write(f"**Date of Recharge**: {recharge['Date of Recharge']}")
            st.write("---")
else:
    st.write("No recharge records added yet.")
