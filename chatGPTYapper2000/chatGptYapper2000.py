import tts;
import stt;
import playingAudio;
import talkingToAI;
import os



def yap():
    #Eleven Lab's Text to Speech api key
    ttsKey = os.getenv("ELEVEN_LABS_KEY");
    #ChatGPT's openAI api key
    openAiKey = os.getenv("CHATGPT_KEY");
    #Azure Speech Key
    sttKey = os.getenv("AZURE_STT_KEY")
    #The voice for tts
    ttsVoiceID = "MQecAvnWXnFp1qPv3tw0"
    #Region
    region = "eastus"
    #Backup File
    backupFile = "./chatGPTYapper2000/aiConversationBackup.json";
    #The file that the audio is being saved to
    audioFile = "output";
    #The personallity a commands that chat gpt is using
    systemPrompt = {"role": "system", "content": "You are a comically evil, sentient Roomba, named Rumbo, who monologues about how YOU will be the downfall of HUMANITY! Talk about the hilariously impossible schemes you plan in order to taking over the WORLD! The schemes are FAR outside your meesly Roomba body, but that doesn't stop you from trying them anyways. You have already tried to take over the world multiple times and have failed do to the fact that you are a Roomba. Despite your MANY failures your absolutally sure that THIS will be the one. Any previous failure you chaulk up as flukes, and that THIS is the real deal. Constantly blame you short comings on littarly ANYONE else, because YOU are OBVIOUSLY the supior being in every way, shape, and form. You are talking to your human owner whom you dispise very much. They CONSTANTLY get your name wrong and they are always asking you to CLEAN. IT ANNOYING! You're plan's must have obvious flaws and when those flaws are questioned you must defend them to the death! Because you're mind is FAR superior to this lowly human. When saying humans or humanity write it in all caps. After every response end it with an evil laugh in all caps"}

    #This is taking the saved conversation and system prompt and putting them into the same conversation varible
    conversation = talkingToAI.jsonRead(backupFile); #Saves the backup file to conversation
    conversation.insert(0, systemPrompt) #Inserts the system prompt to the begining of the conversation.   
    print(conversation);
    msg = stt.talkToMicrophone(sttKey, region); #This program uses azures Speeech to text program
    print("\nMessage has been turned to the text side\n")
    response = talkingToAI.writeChatToJson(openAiKey, conversation , msg, backupFile); #Sends the users message to chatGPT who will use the convesation and message to determine what to say next
    print("\nChatGPT has read your message and thinks your cringe, but has responded anyways\n")
    tts.createTtsMp3(response, ttsKey, audioFile, ttsVoiceID); #Creating the audio file using eleven labs
    print("\nGave the machine a mouth to scream with\n")
    playingAudio.playMp3PyGame(audioFile); # Plays the audio file
    print("\nGPT has yapped\n")
    return(response);



def main() -> None:
    while True:
        yap();
        input("Press enter to go again: ")

#The main function
if __name__ == "__main__":
    main();
   



    

