import os

class FOREGROUND:
    black = 30
    red   = 31
    green = 32
    yellow = 33
    blue  = 34
    white = 37
    purple = 35
    cyan = 36

class BACKGROUND:
    black = 40
    red = 41
    green = 42
    yellow = 43
    blue = 44
    purple = 45
    white = 47

def EnableAnsi():
    os.system("")

def printf(msg:str,fgcolor=FOREGROUND.white,bgcolor=BACKGROUND.black) -> None:
    out = f"\033[{fgcolor};{bgcolor}m{msg}"
    print(out+"\033[0m",end="")