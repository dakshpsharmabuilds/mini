# messages is the list while message is dictionary
messages=[]
def main():
    while True:
        print("hi, do you want to ask anything or quit?")

        if(input()!="quit"):
            print("what u wanna ask then")
            q=input()
            message={
                "role":"user",
                "content": q
            }        
            messages.append(message)

        else:
            break

    print(messages)
