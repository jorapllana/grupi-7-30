#from ollama import chat
#def chat_loop():
    #history=[]
    #print("Welcome to your chatbot! Type quit to exit. \n")

    #while True:
        #user_input = input("You: ")
        #if user_input.strip().lower() == "quit":
            #break
        
        #history.append({"role": "user", "content" : user_input})

        #response = chat(
           #model = "llama3:8b",
            #message = history
        #)

        #reply = response.message.content
        #print("Bot: ", reply)
        #history.append({"role": "assistant", "content": reply})


        #if __name__ == "_main_":
            #chat_loop()
#