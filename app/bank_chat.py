import ollama
import json
# import yfinance as yf

# from bank_tools import get_stock_price_tool, get_bank_balance_tool, update_users_emailid_tool, available_functions

# prompt = 'Can you give my bank balance? my account number is 1234'
# print('Prompt:', prompt)


# response = ollama.chat(
#     'llama3.2',
#     messages=[{'role': 'user', 'content': prompt}],
#     tools=[get_stock_price_tool, get_bank_balance_tool, update_users_emailid_tool],
# )

# if response.message.tool_calls:
#     for tool in response.message.tool_calls:
#         if function_to_call := available_functions.get(tool.function.name):
#             print('Calling function:', tool.function.name)
#             print('Arguments:', tool.function.arguments)
#             print('Function output:', function_to_call(**tool.function.arguments))
#         else:
#             print('Function', tool.function.name, 'not found')
            
            
from openai import OpenAI
from  config import OPENAI_API_KEY
client = OpenAI(api_key=OPENAI_API_KEY)

def categorize_request(user_input):
    system_prompt = """
    You are an AI assistant that categorizes banking-related user requests into predefined categories.
    Given the user request, classify it into one of these categories:
    
    1. Personal (e.g., email update, mobile number update, retrieve or update nominee details,fetch nominee details)
    2. Relationship Manager (e.g., book appointment with RM, get RM details)
    3. Account Info (e.g., balance inquiry, FD advice, 15G/H status)
    4. Banking Info (e.g., FD/RD rates, nearest branch/ATM)
    5. Debit Card (e.g., apply for debit card, reset Green PIN, block card)
    6. Cheque Book (e.g., apply for cheque book, stop cheque payment, check cheque status)
     
    
     Respond strictly in JSON format:
    {
        "category": "<category name>",
        "task": "<specific task>"
    } 
    """

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )
    return json.loads(response['message']['content'])
    #return response['message']['content']


user_input = "I want to know who is my nominee and my account number is 1234"
result = categorize_request(user_input)
print(result)


from tools.personal_tools import  personal_functions,personal_tools

from tools.relation_manager_tools import relationship_functions, relationship_tools

if result['category'] == 'Personal':
    print("Personal")
    available_functions = personal_functions
    available_tools = personal_tools
elif result['category'] == 'Relationship Manager':
    available_functions = relationship_functions
    available_tools = relationship_tools
    print("Relationship Manager")
elif result['category'] == 'Account Info':
    print("Account Info")
elif result['category'] == 'Banking Info':
    print("Banking Info")
elif result['category'] == 'Debit Card':
    print("Debit Card")
elif result['category'] == 'Cheque Book':
    print("Cheque Book")
else:
    print("Unknown category")




response = ollama.chat(
    'llama3.2',
    messages=[{'role': 'user', 'content': user_input}],
    tools= available_tools,
)

#print("Avialable tools", available_tools)
#print("Available functions", available_functions)
print(response)
if response.message.tool_calls:
    for tool in response.message.tool_calls:
        if function_to_call := available_functions.get(tool.function.name):
            print('Calling function:', tool.function.name)
            print('Arguments:', tool.function.arguments)
            print('Function output:', function_to_call(**tool.function.arguments))
        else:
            print('Function', tool.function.name, 'not found')
            