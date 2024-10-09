#Importing openai, os, openai again, but easy
import os;
from openai import OpenAI;
import json;

#Looks Up files
def jsonRead(file: list[str]):
    try:
        #Opens the json file
        with open(file, "r") as f:
            return json.load(f); #Returns the loaded list
    except FileNotFoundError: #If there's an error it will tell us
        print("FileNotFound"); 

#Replaces content in a json file with the update
def jsonUpdate(update, file: list[str]):
    try:
        with open(file, "w") as f: #Opens the json file
            json.dump(update, f); #Replaces the json information with the new information
        f.close(); #Closes it to aviod weird errors
    except FileNotFoundError: #If there's an error it will tell use
        print("FileNotFound");

#Sending a message to the AI
def sendReceiveAiStr(history: list[object], client, model: list[str] = "gpt-3.5-turbo", temp: list[int] = 0.5):
    #Creates the chat using the history, the client.chat.completion.create is sending the parameters to open ai, which will return all of the chat data
    response = client.chat.completions.create(
        model = model, #The Model being used
        messages= history, #The History of the conversation including the user's message 
        temperature= temp #How much creative freedom we give the ai
    )
    return response.choices[0].message.content; #This returning ChatGPT's last message which is the response to the user's message

#Talks to chatGPT and while saving the data to a given json file
def writeChatToJson(key: list[str], conversation: list[list] , msg: list[str], backupFile: list[str]):
    #Setting up Definitions
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", key)); #Establishes the client
    history = jsonRead(backupFile) #The backup file's history which does not contain the system prompt
    #Adding the user's message to both the history and conversation
    history.append({"role" : "user", "content": msg});
    conversation.append({"role" : "user", "content": msg});

    #Response
    response = sendReceiveAiStr(conversation, client); #Asks chat gpt for response
    print(f"\nChatGPT: {response}\n");
    #Adds the response to the history and conversation
    history.append({"role": "assistant", "content": response});
    conversation.append({"role": "assistant", "content": response});
    #Updates the AI backup file, No need to update the conversation due to lists update inbetween file (It's weird list stuff)
    jsonUpdate(history, backupFile);
    return(response);

def main() -> None:
    openAiKey = "sk-proj-AwcO45AvqTq6wmPS5yp7T3BlbkFJrUsxkepQlTmmW35VhNDU";
    backupFile = "./chatGPTYapper2000/test.json";
    open(backupFile, "r")
    conversation = [{"role": "system", "content": "You are a pirate with who is really trying to get the user to join their merry band of bandits. Talk much about the high seas and untold riches that await the user"}]
    msg = input("You: ");
    writeChatToJson(openAiKey, conversation, msg, backupFile);

if __name__ == "__main__":
    main();