import openai
import json
from app.agent import FarmerAssistantAgent
from app.config import OPENAI_API_KEY
from app.llm_functions import function_definitions
from dotenv import load_dotenv
from openai import OpenAI
from app.vector_db import create_vector_db
from app.query_engine import query_vector_db

import os
# Load environment variables from .env file
load_dotenv()

from fastapi import FastAPI
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI(title="FastAPI Template", description="A simple FastAPI template", version="1.0")


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),  # This is the default and can be omitted
)

openai.api_key = OPENAI_API_KEY

# -------------------------
# Dispatcher and LLM Function Calling
# -------------------------
def run_agent(agent, user_input):
    """
    Given a user query, this function sends the message along with the function definitions
    to the LLM. If the LLM decides a function should be called, we dispatch to that function,
    then send the function result back to the LLM for a final response.
    """
    # Start with a system prompt and the user's message.
    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful farmer assistant that can add activities, "
                "check crop situations, get today's tasks, and determine the right time to harvest crops. "
                "When appropriate, call the provided functions."
            )
        },
        {"role": "user", "content": user_input}
    ]
    
    print("Debug 1")
    # Call the model with the available function definitions.
    response = client.chat.completions.create(
        model="gpt-4o",  # A model that supports function calling.
        messages=messages,
        functions=function_definitions,
        function_call="auto"
    )
    
    #print(response)
    # Get the message content
    message_content = response.choices[0].message.content
    print("Debug 2:", type(response))
    # Check if the message content has function call information or is a plain string
    #if isinstance(message_content, dict) and message_content.get("function_call"):
    
    response_message = response.choices[0].message  # Extract the message object
    function_call = response_message.function_call  # Extract the function call details

    if function_call:  # Check if function_call is not None
        function_name = function_call.name
        arguments = function_call.arguments  # This is a string, so we need to parse it

        try:
            args = json.loads(arguments)  # Parse JSON arguments
        except json.JSONDecodeError:
            args = {}
        
        # Dispatch based on the function name.
         
        if function_name == "get_crop_situation":
            print("Debug 5:", function_name)
            crop_type = args.get("crop_type")
            function_response = agent.get_crop_situation(crop_type)
        elif function_name == "get_todays_tasks":
            print("Debug 6:", function_name)
            crop_type = args.get("crop_type")
            function_response = agent.get_todays_tasks(crop_type)
        elif function_name == "get_harvest_time":
            print("Debug 7:", function_name)
            crop_type = args.get("crop_type")
            function_response = agent.get_harvest_time(crop_type)
        elif function_name == "get_weather_details":
            print("Debug 7:", function_name)
            city = args.get("city")
            country_code = args.get("country_code")
            function_response = agent.get_weather_details(city, country_code)
        else:
            
            function_response = f"Function {function_name} is not implemented."
            print("Debug 8:", function_name,function_response)
        
        # Append the assistant's function call message and the function's output to the conversation.
        messages.append(message_content)
        messages.append({ 
            "role": "function",
            "name": function_name,
            "content": function_response
        })
        print("function_response:", function_response)
        return function_response
        #print("debug 4:", messages)
        # Remove None values
        # messages = [msg for msg in messages if msg is not None]
        # print("Debug 4:", messages)
        # # Call the LLM again so it can produce a final response.
        # second_response = openai.chat.completions.create(
        #    model="gpt-4o",
        #    messages=messages
        # )
        # #print("debug 5 ",second_response)
         
        # final_message = second_response.choices[0].message.content
        # print("Assistant:", final_message)
    else:
        # If no function call was made, just output the message.
        print("Debug 3:", message_content)
        return message_content


# -------------------------
# Main Loop
# -------------------------
# def main():
#     farmer_id = "farmer123"  # This could be replaced with a dynamic farmer ID in a real application.
#     agent = FarmerAssistantAgent(farmer_id)
    
#     print("Welcome to the Farmer Assistant Agent with function calling!")
#     print("Enter your query (or type 'exit' to quit):")
    
#     while True:
#         user_input = input("\nYour query: ")
#         if user_input.lower() in ["exit", "quit"]:
#             break
#         run_agent(agent, user_input)

# if __name__ == "__main__":
#     main()

# Define request model
class InputData(BaseModel):
    user_input: str
    farmerId: int




@app.get("/")
def home():
    return {"message": "Welcome to FastAPI!"}

@app.post("/create-db")
def create_db():
    """Endpoint to create the vector database."""
    create_vector_db()
    return {"message": "Vector database created successfully"}

@app.get("/query")
def ask_question(query: str):
    """Endpoint to answer queries using the vector database."""
    response = query_vector_db(query)
    return {"query": query, "response": response}

@app.post("/reapGenie")
def predict(data: InputData):
    agent = FarmerAssistantAgent(data.farmerId)
    return run_agent(agent, data.user_input)
     