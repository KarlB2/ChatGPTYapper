import os #Using the os to check if file paths exist
import time #For time stuff
import pygame #Using this one for it's mixer and time functions

#Checks to see if the file exists and if it can be accessed
def waitForFile(file: list[str], timeout: list[int]=60, checkInterval: list[int]=1):
    #If the file does not exist then we wait for it to exist
    start_time = time.time(); #Sets the start time to the current time
    while not os.path.exists(file):
        if time.time() - start_time > timeout: #Checks to see if the time has exceeded the timeout limit
            raise TimeoutError(f"Timeout waiting for file: {file}");  #Raises an error warning
        print(f"Waiting for {file} to exist")
        time.sleep(checkInterval) #Has the loop wait checkInterval seconds before continuing
    
    #If the file cannot be opened then we wait for it to be open
    while True:
        try:
            with open(file, 'rb') as f:
                f.read();
            print(f"{file} has been read");
            break;
        except IOError:
            print(f"Cannot read {file}");
            time.sleep(checkInterval);

def playMp3PyGame(file: list[str] = "output.mp3"):
    pygame.mixer.init() #Initializes the mixer, so that it can be used
    pygame.mixer.music.load(file); #Loads the mp3 file so that it can be played
    pygame.mixer.music.play(); #Plays the mp3 file
    while pygame.mixer.music.get_busy(): #Checks to see if the file is still playing
        pygame.time.Clock().tick(10) #Makes the while loop wait 10 miliseconds to check again
    #Stops the audio
    pygame.mixer.music.stop() #This stops playing the music and closes the file
    pygame.mixer.quit() #This quits out of the mixer saving ram

#This is the Main Function which runs on it's own (Note: that the function will produce an error if output.mp3 do not exist)
def main() -> None:
    output = "output.mp3" #The default mp3 file
    waitForFile(output); #Waits for the file to exist
    playMp3PyGame(output); #Plays the mp3 file

#If this program is being ran directally then main while run
if __name__ == "__main__":
    main();