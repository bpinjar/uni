import yfinance as yf
##############################################################################################################

# Personal
def update_email( user_id, new_email):
    """Updates the email ID for the given user."""
    return f"Email ID for user {user_id} updated to {new_email}."

def update_mobile_number(  user_id, new_mobile):
    """Updates the mobile number for the given user."""
    return f"Mobile number for user {user_id} updated to {new_mobile}."

def view_nominee(  account_number):
    """Returns the nominee details for the given account."""
    return f"Displaying nominee details for account {account_number} and UI flag = Nominee."

def add_update_nominee( account_number, nominee_name, relationship):
    """Adds or updates the nominee for the given account."""
    print("Adding/Updating nominee...")
    return f"Nominee '{nominee_name}' ({relationship}) added/updated for account {account_number}."

