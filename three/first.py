__author__ = 'Mohamed_Ramadan_PC'
import termios, sys, time
if sys.version > "2.1" : TERMIOS = termios
else                   : import TERMIOS

def setSpecial () :
	"set keyboard to read single chars lookahead only"
	global oldSettings
	fd = sys.stdin.fileno()
	oldSettings = termios.tcgetattr(fd)
	new = termios.tcgetattr(fd)
	new[3] = new[3] & ~TERMIOS.ECHO    # lflags
	new[3] = new[3] & ~TERMIOS.ICANON  # lflags
	new[6][6] = '\000'    # Set VMIN to zero for lookahead only
	termios.tcsetattr(fd, TERMIOS.TCSADRAIN, new)

def setNormal () :
	"restore previous keyboard settings"
	global oldSettings
	fd = sys.stdin.fileno()
	termios.tcsetattr(fd, TERMIOS.TCSADRAIN, oldSettings)

def readLookAhead () :
	"read max 3 chars (arrow escape seq) from look ahead"
	return sys.stdin.read(3)
