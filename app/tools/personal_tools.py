
from typing import Dict, Any, Callable
#from bank_functons import get_stock_price, get_bank_balance, update_users_emailid
from functions.personal import update_email, update_mobile_number, view_nominee, add_update_nominee

# # Manual tool definition
# get_stock_price_tool = {
#     'type': 'function',
#     'function': {
#         'name': 'get_stock_price',
#         'description': 'Get the current stock price for any symbol',
#         'parameters': {
#             'type': 'object',
#             'required': ['symbol'],
#             'properties': {
#                 'symbol': {'type': 'string', 'description': 'The stock symbol (e.g., AAPL, GOOGL)'},
#             },
#         },
#     },
# }

# get_bank_balance_tool = {
#     'type': 'function',
#     'function': {
#         'name': 'get_bank_balance',
#         'description': 'Get the bank balance for a user',
#         'parameters': {
#             'type': 'object',
#             'required': ['account_number'],
#             'properties': {
#                 'symbol': {'type': 'string', 'description': ' The account number of the user'},
#             },
#         },
#     },
# }

# update_users_emailid_tool = {
#     'type': 'function',
#     'function': {
#         'name': 'update_users_emailid',
#         'description': "Updates the user's email address",
#         'parameters': {
#             'type': 'object',
#             'required': ['email_id'],
#             'properties': {
#                 'symbol': {'type': 'string', 'description': 'email id of the user'},
#             },
#         },
#     },
# }

# available_functions: Dict[str, Callable] = {
#     'get_stock_price': get_stock_price, 
#     'get_bank_balance': get_bank_balance,
#     'update_users_emailid': update_users_emailid,
# }


##############################################################################################################

update_users_emailid_tool = {
    'type': 'function',
    'function': {
        'name': 'update_email',
        'description': "Updates the user's email address",
        'parameters': {
            'type': 'object',
            'required': ['user_id', 'email_id'],
            'properties': {
                'user_id': {'type': 'string', 'description': 'Unique identifier of the user'},
                'email_id': {'type': 'string', 'description': 'New email ID of the user'},
            },
        },
    },
}

update_mobile_number_tool = {
    'type': 'function',
    'function': {
        'name': 'update_mobile_number',
        'description': "Updates the user's mobile number",
        'parameters': {
            'type': 'object',
            'required': ['user_id', 'mobile_number'],
            'properties': {
                'user_id': {'type': 'string', 'description': 'Unique identifier of the user'},
                'mobile_number': {'type': 'string', 'description': 'New mobile number of the user'},
            },
        },
    },
}

view_nominee_tool = {
    'type': 'function',
    'function': {
        'name': 'view_nominee',
        'description': "Displays the nominee details for an account",
        'parameters': {
            'type': 'object',
            'required': ['account_number'],
            'properties': {
                'account_number': {'type': 'string', 'description': 'Account number to view the nominee'},
            },
        },
    },
}

add_update_nominee_tool = {
    'type': 'function',
    'function': {
        'name': 'add_update_nominee',
        'description': "Adds or updates a nominee for an account",
        'parameters': {
            'type': 'object',
            'required': ['account_number', 'nominee_name', 'relationship'],
            'properties': {
                'account_number': {'type': 'string', 'description': 'Account number for nominee update'},
                'nominee_name': {'type': 'string', 'description': 'Name of the nominee'},
                'relationship': {'type': 'string', 'description': 'Relationship of the nominee to the account holder'},
            },
        },
    },
}

# fix_appointment_with_rm_tool = {
#     'type': 'function',
#     'function': {
#         'name': 'fix_appointment_with_rm',
#         'description': "Schedules an appointment with the Relationship Manager",
#         'parameters': {
#             'type': 'object',
#             'required': ['user_id', 'date_time'],
#             'properties': {
#                 'user_id': {'type': 'string', 'description': 'Unique identifier of the user'},
#                 'date_time': {'type': 'string', 'description': 'Requested date and time for the appointment'},
#             },
#         },
#     },
# }

# get_rm_details_tool = {
#     'type': 'function',
#     'function': {
#         'name': 'get_rm_details',
#         'description': "Fetches details of the user's Relationship Manager",
#         'parameters': {
#             'type': 'object',
#             'required': ['user_id'],
#             'properties': {
#                 'user_id': {'type': 'string', 'description': 'Unique identifier of the user'},
#             },
#         },
#     },
# }

# balance_inquiry_tool = {
#     'type': 'function',
#     'function': {
#         'name': 'balance_inquiry',
#         'description': "Fetches the balance for a CASA account",
#         'parameters': {
#             'type': 'object',
#             'required': ['account_number'],
#             'properties': {
#                 'account_number': {'type': 'string', 'description': 'Account number for balance inquiry'},
#             },
#         },
#     },
# }

# rupay_offers_tool = {
#     'type': 'function',
#     'function': {
#         'name': 'rupay_offers',
#         'description': "Retrieves available RuPay offers",
#         'parameters': {
#             'type': 'object',
#             'required': ['card_number'],
#             'properties': {
#                 'card_number': {'type': 'string', 'description': 'RuPay debit card number'},
#             },
#         },
#     },
# }

# download_fd_advice_tool = {
#     'type': 'function',
#     'function': {
#         'name': 'download_fd_advice',
#         'description': "Provides a download link for FD Advice",
#         'parameters': {
#             'type': 'object',
#             'required': ['fd_account_number'],
#             'properties': {
#                 'fd_account_number': {'type': 'string', 'description': 'Fixed Deposit account number'},
#             },
#         },
#     },
# }

# view_15g_15h_status_tool = {
#     'type': 'function',
#     'function': {
#         'name': 'view_15g_15h_status',
#         'description': "Allows the user to submit, view, or download the 15G/H form",
#         'parameters': {
#             'type': 'object',
#             'required': ['user_id'],
#             'properties': {
#                 'user_id': {'type': 'string', 'description': 'Unique identifier of the user'},
#             },
#         },
#     },
# }

# get_fd_rd_rates_tool = {
#     'type': 'function',
#     'function': {
#         'name': 'get_fd_rd_rates',
#         'description': "Fetches the latest Fixed Deposit and Recurring Deposit rates",
#         'parameters': {},
#     },
# }

# find_nearest_branch_atm_tool = {
#     'type': 'function',
#     'function': {
#         'name': 'find_nearest_branch_atm',
#         'description': "Finds the nearest bank branch or ATM",
#         'parameters': {
#             'type': 'object',
#             'required': ['location'],
#             'properties': {
#                 'location': {'type': 'string', 'description': 'User-provided location'},
#             },
#         },
#     },
# }

# apply_for_debit_card_tool = {
#     'type': 'function',
#     'function': {
#         'name': 'apply_for_debit_card',
#         'description': "Applies for a new debit card",
#         'parameters': {
#             'type': 'object',
#             'required': ['user_id', 'account_number'],
#             'properties': {
#                 'user_id': {'type': 'string', 'description': 'Unique identifier of the user'},
#                 'account_number': {'type': 'string', 'description': 'Account number linked to the debit card'},
#             },
#         },
#     },
# }

# set_reset_green_pin_tool = {
#     'type': 'function',
#     'function': {
#         'name': 'set_reset_green_pin',
#         'description': "Sets or resets the Green PIN for a debit card",
#         'parameters': {
#             'type': 'object',
#             'required': ['card_number'],
#             'properties': {
#                 'card_number': {'type': 'string', 'description': 'Debit card number'},
#             },
#         },
#     },
# }

# block_unblock_debit_card_tool = {
#     'type': 'function',
#     'function': {
#         'name': 'block_unblock_debit_card',
#         'description': "Blocks or unblocks a debit card",
#         'parameters': {
#             'type': 'object',
#             'required': ['card_number', 'action'],
#             'properties': {
#                 'card_number': {'type': 'string', 'description': 'Debit card number'},
#                 'action': {'type': 'string', 'enum': ['block', 'unblock'], 'description': "Action to perform (block/unblock)"},
#             },
#         },
#     },
# }

# apply_for_cheque_book_tool = {
#     'type': 'function',
#     'function': {
#         'name': 'apply_for_cheque_book',
#         'description': "Requests a new cheque book",
#         'parameters': {
#             'type': 'object',
#             'required': ['account_number'],
#             'properties': {
#                 'account_number': {'type': 'string', 'description': 'Account number for cheque book request'},
#             },
#         },
#     },
# }

# stop_cheque_payment_tool = {
#     'type': 'function',
#     'function': {
#         'name': 'stop_cheque_payment',
#         'description': "Stops payment for a specific cheque",
#         'parameters': {
#             'type': 'object',
#             'required': ['cheque_number'],
#             'properties': {
#                 'cheque_number': {'type': 'string', 'description': 'Cheque number to stop payment'},
#             },
#         },
#     },
# }

# cheque_leaf_status_tool = {
#     'type': 'function',
#     'function': {
#         'name': 'cheque_leaf_status',
#         'description': "Checks the status of a specific cheque",
#         'parameters': {
#             'type': 'object',
#             'required': ['cheque_number'],
#             'properties': {
#                 'cheque_number': {'type': 'string', 'description': 'Cheque number to check status'},
#             },
#         },
#     },
# }


personal_functions: Dict[str, Callable] = {    
    'update_email': update_email,
    'update_mobile_number': update_mobile_number,
    'view_nominee': view_nominee,
    'add_update_nominee': add_update_nominee,
}

personal_tools = [update_users_emailid_tool,update_mobile_number_tool, view_nominee_tool, add_update_nominee_tool]
