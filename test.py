# messages is the list while message is dictionary
import json
from dotenv import load_dotenv
import os
from pathlib import Path
from google import genai
from google.genai import types


load_dotenv(Path(__file__).with_name(".env"))
api_key = os.getenv("GEMINI_API_KEY")
print("Key loaded:", api_key is not None)  # checks presence; doesn't reveal it
client = genai.Client()
messages=[]

def stats():
     print("the amount of messages combined by user and AI is ", len(messages))

def show_msg(messages):
    for m in messages:
        if(m["role"]=="user"):
            print("USER: ")
            print(m["content"])
        elif(m["role"]=="model"):
            print("GEMINI: ")
            print(m["content"])

   
def save_history(messages):
    with open("history.json", "w") as file:
        json.dump(messages, file, indent=2)

def loadup():
    try:
        with open("history.json", "r", encoding="utf-8") as file:
            loaded_messages = json.load(file)
    except FileNotFoundError:       #if file doesnt exist, return a fresh []. basically the case when we start using for the first time
        return []
    except json.JSONDecodeError:    #if file is damaged
        raise SystemExit("history.json is damaged. Fix it before starting the chat.")

    return loaded_messages

    
message={}
prev_msg=[]     #prev_msg is the list, we will loop thru the list, change each item (the dict), change the key  
def main():
    prev_msg=loadup()
    for i in range(len(prev_msg)):
        prev_msg[i]["parts"]= [{"text":prev_msg[i].get("content")}]
        prev_msg[i].pop("content", None)
    chat = client.chats.create(model="gemini-3.5-flash-lite" history=prev_msg)

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
            llm_resp = {
                "role":"model",
                "content": response.text
            }

            messages.append(message)
            messages.append(llm_resp)
            save_history(messages)
            
        elif(choice=="history"):
            show_msg(messages)
            
        elif(choice=="quit"):
            save_history(messages)
            break
        elif(choice=="stats"):
            stats()
            

main()