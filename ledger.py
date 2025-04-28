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
    print(f"Recharge done for {user_name} on {date_of_recharge}: {recharge_plan} plan costing {recharge_amount}.")

# Adding recharge records for users
add_mobile_recharge("Ajoy Jayarajan", 299, "Data Pack", "2025-04-25")
add_mobile_recharge("Ajoy Jayarajan", 499, "Unlimited Pack", "2025-04-27")
add_mobile_recharge("Sahil Wayal", 199, "Talktime Pack", "2025-04-26")

# Displaying the mobile recharge ledger
print("\nMobile Recharge Ledger:")
for user, recharges in mobile_recharge_ledger.items():
    print(f"\nUser: {user}")
    for recharge in recharges:
        print(recharge)
