#Importing azure's speech service as azrSpeech which wasn't a bad idea to name it that :\
import azure.cognitiveservices.speech as azrSpeech

def createSpeechRecognizer(key: list[str], region: list[str], initialSilenceTime: list[int] = 20, endSilenceTime: list[int] = 60, mic = True):
    #Assigning the speechConfiguration to specchConfig and establishes both the subscription and region
    speechConfig = azrSpeech.SpeechConfig(subscription=key, region=region);
    speechConfig.speech_recognition_language = "en-US"; #Configures the speech program to be english
    #Determines if the program should use the default microphone or a specified microphone
    if (mic == True):
        audioConfig = azrSpeech.audio.AudioConfig(use_default_microphone=True); #Assigning the audio configuration to audioConfig and set's the microphone to the default
    else:
        audioConfig = azrSpeech.audio.AudioConfig(device_name=mic); #Assigning the audio configuration to audioConfig and set's the microphone to the microphones ID

    #Assigning the speech recognizer program to speechRecognizer using speechConfig's and audioConfig's setting
    speechRecognizer = azrSpeech.SpeechRecognizer(speech_config=speechConfig, audio_config=audioConfig); 
    #Times out the program if the user hasn't given any input and remains silent for initialSilenceTime seconds
    speechRecognizer.properties.set_property(azrSpeech.PropertyId.SpeechServiceConnection_EndSilenceTimeoutMs, f"{1000 * initialSilenceTime}" );
    #Times out the program if the user has given input and remains silent for endSilenceTime seconds
    speechRecognizer.properties.set_property(azrSpeech.PropertyId.SpeechServiceConnection_InitialSilenceTimeoutMs, f"{1000 * endSilenceTime}"); 
    return speechRecognizer;

#Basically the entire program, that was copy and pasted with minor tweaks
def talkToMicrophone(key: list[str], region: list[str], initialSilenceTime: list[int] = 20, endSilenceTime: list[int] = 60, mic = True):
    #Creates the speech recognizer
    speechRecognizer = createSpeechRecognizer(key, region, initialSilenceTime, endSilenceTime, mic);
    #Waits for user to press enter, so that the user may take breaks and not worry about being timed out
    print("Starting program, say \"stop\" to stop")
    message = "" #This message will be what the program returns when called. Every recognized result will be added to this string
    #The listening loop, which recognizes the result of the microphone input, put's it into text format, and repeat's until the user says stop
    while True:
        #Exicutes the speech recognizer asynchronously (Text is not generated live it is only generated after the user pauses for a certain amount of time, after which the program is allowed to countinue through the loop)
        speechRecognitionResult = speechRecognizer.recognize_once_async().get(); 
        #The speechRecognizer's result's reason is basically what state the output is in, these if statments check what that state is to avoid any program errors
        if speechRecognitionResult.reason == azrSpeech.ResultReason.RecognizedSpeech: #The program recognizes the words!
            print("Recognize: {}".format(speechRecognitionResult.text));
            if "stop" in speechRecognitionResult.text.lower(): #If stop is in the result then the program stops (Temporary)
                print("Stopping program");
                break
            message += " {}".format(speechRecognitionResult.text); #Adds the text of the speech to the message
        if speechRecognitionResult.reason == azrSpeech.ResultReason.NoMatch: #The speech was not recognized
            print("Sorry didn't hear that")
        elif speechRecognitionResult.reason == azrSpeech.ResultReason.Canceled: #The program was cancled even before listening
            print("Program was cancled by the radical left");
    print(message);
    return(message); #Returns the message

#The Main Function
def main () -> None:
    key = "3dde722349a1473eb9bed1a0fae56c5c";
    region = "eastus";
    print(talkToMicrophone(key, region));

if __name__ == "__main__":
    main();
