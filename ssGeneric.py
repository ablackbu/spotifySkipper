import json

def shouldSkip(artist, track):
    banDictionary = json.load(open("ban.json"))

    if artist in banDictionary:
        bannedArtistSongs = banDictionary[artist]
        #TODO: test the wildcard functionality 
        if track in bannedArtistSongs or bannedArtistSongs == "*":
                print('Skipping banned track: ' + track);
                return True
    print('Not skipping: ' + track);
    return False


if __name__ == '__main__':
    # ssGeneric.py executed as script
    # do something
    shouldSkip("Bruno Mars", "24K Magic")
    #http://stackoverflow.com/questions/1186789/what-is-the-best-way-to-call-a-python-script-from-another-python-script
