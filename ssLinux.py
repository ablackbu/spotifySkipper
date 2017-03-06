#Note to future self. For more information on dbus use d-feet tool!
import dbus
import time
import ssGeneric

def startSkipper2():
    try:
        startSkipper();
    except Exception:
        print ('It appears spotify is not : ' + sys.platform)
        time.sleep(10);
        startSkipper();

#TODO: add exception handling if spotify isn't loaded mpris is upset. maybe
# try catch and retry every 10s ? 
def startSkipper():

    session_bus = dbus.SessionBus()
    spotify_bus = session_bus.get_object("org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")

    #This alows us interface with the methods
    spotify_player = dbus.Interface(spotify_bus, "org.mpris.MediaPlayer2.Player")

    #This lets us interface with the properties.
    spotify_properties = dbus.Interface(spotify_bus, "org.freedesktop.DBus.Properties")
    metadata = spotify_properties.Get("org.mpris.MediaPlayer2.Player", "Metadata")

    while True:
        metadata = spotify_properties.Get("org.mpris.MediaPlayer2.Player", "Metadata")
        artist = metadata.get(dbus.String(u'xesam:artist'))[0]
        track = metadata['xesam:title']

        if ssGeneric.shouldSkip(artist, track):
            spotify_player.Next();

        time.sleep(1)

if __name__ == '__main__':
    # ssLinux.py executed as script
    # do something
    startSkipper()
    #http://stackoverflow.com/questions/1186789/what-is-the-best-way-to-call-a-python-script-from-another-python-script
