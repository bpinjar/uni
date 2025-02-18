
from typing import Dict, Any, Callable
from bank_functons import get_stock_price, get_bank_balance, update_users_emailid

# Manual tool definition
get_stock_price_tool = {
    'type': 'function',
    'function': {
        'name': 'get_stock_price',
        'description': 'Get the current stock price for any symbol',
        'parameters': {
            'type': 'object',
            'required': ['symbol'],
            'properties': {
                'symbol': {'type': 'string', 'description': 'The stock symbol (e.g., AAPL, GOOGL)'},
            },
        },
    },
}

get_bank_balance_tool = {
    'type': 'function',
    'function': {
        'name': 'get_bank_balance',
        'description': 'Get the bank balance for a user',
        'parameters': {
            'type': 'object',
            'required': ['account_number'],
            'properties': {
                'symbol': {'type': 'string', 'description': ' The account number of the user'},
            },
        },
    },
}

update_users_emailid_tool = {
    'type': 'function',
    'function': {
        'name': 'update_users_emailid',
        'description': "Updates the user's email address",
        'parameters': {
            'type': 'object',
            'required': ['email_id'],
            'properties': {
                'symbol': {'type': 'string', 'description': 'email id of the user'},
            },
        },
    },
}

available_functions: Dict[str, Callable] = {
    'get_stock_price': get_stock_price, 
    'get_bank_balance': get_bank_balance,
    'update_users_emailid': update_users_emailid,
}