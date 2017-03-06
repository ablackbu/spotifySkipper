import spotilib
import time
import ssGeneric


#TODO: test me & error handling ? 
def startSkipper():

    while True:
        artist = spotilib.artist()
        track = spotlib.song()

        if ssGeneric.shouldSkip(artist, track):
            spotlib.next()
            time.sleep(1)

if __name__ == '__main__':
    # ssWin.py executed as script
    # do something
    startSkipper()
    #http://stackoverflow.com/questions/1186789/what-is-the-best-way-to-call-a-python-script-from-another-python-script
