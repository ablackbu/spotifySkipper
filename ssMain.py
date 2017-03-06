import sys
import ssLinux
import ssMac
import ssWin

#TODO: Maybe combine ssMac/ssLinux/ssWindows into a single file with 3 functions ?
#

if 'linux' in sys.platform:
    ssLinux.startSkipper2()
elif 'dawrin' in sys.platform:
    ssMac.startSkipper()
elif 'windows' in sys.platform:
    #ssWin.startSkipper()
    print ('dafaq: ' + sys.platform)

else:
    print ('Unsupported platform: ' + sys.platform)
