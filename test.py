# messages is the list while message is dictionary
import json
from dotenv import load_dotenv
import os
from pathlib import Path
from google import genai
load_dotenv(Path(__file__).with_name(".env"))
api_key = os.getenv("GEMINI_API_KEY")
print("Key loaded:", api_key is not None)  # checks presence; doesn't reveal it
client = genai.Client()
messages=[]


def show_msg(messages):
    for m in messages:
        print(m["content"])

def call_api(message):
    ###calling api here, passing it the message dictionary formatted into json. then taking its reply and 
    ###making it back into a dict, then return that to main, store it in messages
    
    response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=message["content"]
)
    return {
        "role": "assistant",
        "content": response.text
    }
   
def save_history(messages):
    with open("history.json", "w") as file:
        json.dump(messages, file, indent=2)

def main():
    chat = client.chats.create(model="gemini-3.5-flash-lite")

    while True:
        print("hi, do you want to ask anything or quit or do you wanna see the message history?")
        print("type history to see it, quit to do it, or ask to start chatting")
        choice=input()
        
        if(choice=="ask"):
            print("what u wanna ask then")
            q=input()
            response = chat.send_message(q)
            print(response.text)
            message={
                    "role":"user",
                    "content": q
                }   
            
            llm_dict=call_api(message)

            messages.append(message)
            messages.append(llm_dict)
            
        elif(choice=="history"):
            show_msg(messages)
            
        elif(choice=="quit"):
            save_history(messages)
            break
            

main()