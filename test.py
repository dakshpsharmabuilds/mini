# messages is the list while message is dictionary
import json
messages=[]

def show_msg(messages):
    for m in messages:
        print(m["content"])

def call_api(message):
    ###calling api here, passing it the message dictionary formatted into json. then taking its reply and 
    ###making it back into a dict, then return that to main, store it in messages
    


def main():
    while True:
        print("hi, do you want to ask anything or quit or do you wanna see the message history?")
        print("type history to see it, quit to do it, or ask to start chatting")
        choice=input()
        if(choice=="ask"):
            print("what u wanna ask then")
            q=input()
            message={
                    "role":"user",
                    "content": q
                }   
            llm_dict={
                "role":"assistant",
                "content":""
            }     

            messages.append(message)
            messages.append(llm_dict)

        elif(choice=="history"):
            show_msg(messages)
            break
        elif(choice=="quit"):
            break
            

main()