import yfinance as yf

def get_stock_price(symbol: str) -> float:    
    print('Getting stock price for symbol:', symbol)
    return ("Getting stock price for symbol:", symbol)
    

def get_bank_balance(account_number: str) -> float:
    print('Getting bank balance for account number:', account_number)    
    return 1000.0
 
# Personal
def update_email(self, user_id, new_email):
    """Updates the email ID for the given user."""
    return f"Email ID for user {user_id} updated to {new_email}."

def update_mobile_number(self, user_id, new_mobile):
    """Updates the mobile number for the given user."""
    return f"Mobile number for user {user_id} updated to {new_mobile}."

def view_nominee(self, account_number):
    """Returns the nominee details for the given account."""
    return f"Displaying nominee details for account {account_number}."

def add_update_nominee(self, account_number, nominee_name, relationship):
    """Adds or updates the nominee for the given account."""
    return f"Nominee '{nominee_name}' ({relationship}) added/updated for account {account_number}."




##############################################################################################################
# Relationship
def fix_appointment_with_rm(self, user_id, date_time):
    """Schedules an appointment with the Relationship Manager."""
    return f"Appointment scheduled with RM for user {user_id} on {date_time}."

def get_rm_details(self, user_id):
    """Returns Relationship Manager details for the given user."""
    return f"Fetching Relationship Manager details for user {user_id}."

##############################################################################################################

# Account Information
def balance_inquiry(self, account_number):
    """Returns balance for the given account."""
    return f"Balance inquiry request received for account {account_number}."

def rupay_offers(self, card_number):
    """Returns available offers on the user's RuPay debit card."""
    return f"Fetching RuPay offers for card {card_number}."

def download_fd_advice(self, fd_account_number):
    """Provides a download link for the FD Advice."""
    return f"FD Advice available for download for FD account {fd_account_number}."

def view_15g_15h_status(self, user_id):
    """Allows the user to submit, view, or download the 15G/H form."""
    return f"Displaying 15G/H form status for user {user_id}."

##############################################################################################################
# Banking Information
def get_fd_rd_rates(self):
    """Returns the latest FD/RD rates."""
    return "Fetching latest Fixed Deposit and Recurring Deposit rates."

def find_nearest_branch_atm(self, location):
    """Finds the nearest branch or ATM based on user location."""
    return f"Searching for nearest branch/ATM in {location}."

##############################################################################################################
# Debit/ATM Services
def apply_for_debit_card(self, user_id, account_number):
    """Applies for a new debit card for the selected account."""
    return f"Debit card application submitted for account {account_number} of user {user_id}."

def set_reset_green_pin(self, card_number):
    """Allows the user to set or reset the Green PIN for their debit card."""
    return f"Green PIN reset request received for card {card_number}."

def block_unblock_debit_card(self, card_number, action):
    """Blocks or unblocks a debit card based on user request."""
    if action.lower() == "block":
        return f"Debit card {card_number} has been blocked."
    elif action.lower() == "unblock":
        return f"Debit card {card_number} has been unblocked."
    else:
        return "Invalid action. Please specify 'block' or 'unblock'."


##############################################################################################################
# Cheque Book Services
def apply_for_cheque_book(self, account_number):
    """Requests a new cheque book for the user's account."""
    return f"Cheque book request submitted for account {account_number}."

def stop_cheque_payment(self, cheque_number):
    """Stops the payment of a specific cheque."""
    return f"Stop payment request submitted for cheque number {cheque_number}."

def cheque_leaf_status(self, cheque_number):
    """Checks the status of a specific cheque leaf."""
    return f"Fetching status of cheque number {cheque_number}."
