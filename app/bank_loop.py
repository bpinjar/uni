
import ollama
import json
import os

from vector_db.vector_db_functions import create_vector_db,load_vector_db
from tools.personal_tools import  personal_functions,personal_tools
from tools.relation_manager_tools import relationship_functions, relationship_tools

import sys
sys.path.append("C:/Users/babas/OneDrive/Desktop/Multiagent/KireapGenie")
# In-memory storage for farmers' previous conversations
farmers_memory = {}

def load_farmer_context(farmer_name):
    """Load farmer's previous conversation from memory if available."""
    if farmer_name in farmers_memory:
        return farmers_memory[farmer_name]
    return []

def save_farmer_context(farmer_name, messages):
    """Save farmer's conversation context in memory."""
    farmers_memory[farmer_name] = messages



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
        "category": "<category name>"       
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


 
# Create a vector database
create_vector_db()
load_vector_db()
# Ask user for their name
farmer_name = input("Enter your name: ")

# Load previous context for the farmer
conversation_history = load_farmer_context(farmer_name)
 
 
while True:
    user_input = input("\nAsk your question (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break

    # Orchestrator to categorize the user's request
    result = categorize_request(user_input) 
    print(result)


    
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
        
    ##############################
    # Add the user's query to conversation history
    conversation_history.append({'role': 'user', 'content': user_input})

    # Get AI response
    response = ollama.chat(
        model='llama3.2',
        messages=conversation_history,
        tools=available_tools,
    )

    print("\nAI Response:", response['message']['content'])

    # Check if any function needs to be called
    if response['message'].get('tool_calls'):
        for tool in response['message']['tool_calls']:
            function_name = tool['function']['name']
            arguments = tool['function']['arguments']

            if function_to_call := available_functions.get(function_name):
                print('Calling function:', function_name)
                print('Arguments:', arguments)
                function_output = function_to_call(**arguments)
                print('Function output:', function_output)

                # Save AI response to context
                conversation_history.append({'role': 'assistant', 'content': function_output})
            else:
                print('Function', function_name, 'not found')

    # Save conversation context for the farmer
    save_farmer_context(farmer_name, conversation_history)