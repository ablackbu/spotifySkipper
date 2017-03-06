#TODO: finish me & test me & error handling
def startSkipper():
    print('osx !' )

    #AppleScript Spotify Commands
    Track = """osascript -e 'tell application "Spotify" to name of current track as string'"""
    Artist = """osascript -e 'tell application "Spotify" to artist of current track as string'"""
    Next = """osascript -e 'tell application "Spotify" to next track'"""

    while True:
        #We aren't concerned with the "security" risk associated with this because the commands
        #we have are not external inputs by the user.
        #[:-1] is required to strip away the new line character that is returned
        artist = subprocess.check_output(Artist, shell=True)[:-1]
        track = subprocess.check_output(Track, shell=True)[:-1]

        if ssGeneric.shouldSkip(artist, track):
            artist = subprocess.check_output(Next, shell=True)[:-1]
            time.sleep(1)


if __name__ == '__main__':
    # ssMac.py executed as script
    # do something
    startSkipper()
    #http://stackoverflow.com/questions/1186789/what-is-the-best-way-to-call-a-python-script-from-another-python-script
