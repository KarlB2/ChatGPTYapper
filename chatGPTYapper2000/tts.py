# Import necessary libraries
import requests  # Used for making HTTP requests
import playingAudio #Used strictally for testing the file

def createTtsMp3(text: list[str], key: list[str], outputPath: list[str] = "output.mp3", voiceId: list[str] = "pNInz6obpgDQGcFmaJgB", chunksize: list[int] = 1024):
    # Define constants for the script

    # The url with the voice ID
    tts_url = f"https://api.elevenlabs.io/v1/text-to-speech/{voiceId}/stream"

    # Headers for the API request with the API key for authentication
    headers = {
        "Accept": "application/json",
        "xi-api-key": key
    }

    # Data payload for the API request with the text and voice settings
    data = {
        "text": text, #This is what the program will say
        "model_id": "eleven_multilingual_v2", #
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.8,
            "style": 0.0,
            "use_speaker_boost": True
        }
    }

    print("Creating response");
    # Make the POST request to the TTS API with headers and data, enabling streaming response
    response = requests.post(tts_url, headers=headers, json=data, stream=True)


    # Check if the request was successful
    if response.ok:
        # Open the output file in write-binary mode
        with open(outputPath, "wb") as f:
            # Read the response in chunks and write to the file
            for chunk in response.iter_content(chunk_size=chunksize):
                f.write(chunk)
            f.close();
        
        # Inform the user of success
        print("\nAudio stream saved successfully\n")
    else:
        # Print the error message if the request was not successful
        print(response.text);



#Test Code
def main() -> None:
    text = input("Enter Input: "); #Asking for user to imput text to be turned into an mp3 file
    key = "sk_9ba5f1b7ae48a8ec0b63c84295fc12b311e8873da4d2153e" #The key "Temporary filler"
    output = "output.mp3" #The testing output
    createTtsMp3(text, key, output); #Creates the tts
    playingAudio.playMp3PyGame(output); #Plays the file for testing purposes
    
#Runs program on it's own
if __name__ == "__main__":
    while True:
        main();