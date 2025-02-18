
##############################################################################################################
# Debit/ATM Services
def apply_for_debit_card( user_id, account_number):
    """Applies for a new debit card for the selected account."""
    return f"Debit card application submitted for account {account_number} of user {user_id}."

def set_reset_green_pin( card_number):
    """Allows the user to set or reset the Green PIN for their debit card."""
    return f"Green PIN reset request received for card {card_number}."

def block_unblock_debit_card( card_number, action):
    """Blocks or unblocks a debit card based on user request."""
    if action.lower() == "block":
        return f"Debit card {card_number} has been blocked."
    elif action.lower() == "unblock":
        return f"Debit card {card_number} has been unblocked."
    else:
        return "Invalid action. Please specify 'block' or 'unblock'."
