import sys
from reader import *
from logger import log_function
from console import *

import warnings
warnings.filterwarnings("ignore")

def check(fn,parameters,msg):
    st = fn(*parameters)
    printf("|",FOREGROUND.cyan)
    if st:
       printf(msg,FOREGROUND.black,BACKGROUND.green) 
    else:
        printf(msg,FOREGROUND.black,BACKGROUND.red)
    printf("|",FOREGROUND.cyan)
    return st

def main(image_path:str) -> None:
    img = log_function(LoadImage,[image_path])
    print("\n")
    if check(has_nth_order,[img,6],"HAS SIXTH ORDER ROTATION"):
        if check(has_reflection,[img],"HAS REFLECTION"):
            printf("WALLPAPER BELONGS TO P6M",FOREGROUND.cyan,BACKGROUND.purple)
            
        else:
            printf("WALLPAPER BELONGS TO P6",FOREGROUND.cyan,BACKGROUND.purple)
        return
        
    print("\n")
    if check(has_nth_order,[img,4],"HAS FOURTH ORDER ROTATION "):
        if check(has_reflection,[img],"HAS REFLECTION"):
            pass
        else:
            printf("WALLPAPER BELONGS TO P4",FOREGROUND.cyan,BACKGROUND.purple)
        return
    print("\n")
    if check(has_nth_order,[img,3],"HAS THIRD ORDER ROTATION "):
        if check(has_reflection,[img],"HAS REFLECTION"):
            pass
        else:
            printf("WALLPAPER BELONGS TO P3",FOREGROUND.cyan,BACKGROUND.purple)
        return
    print("\n")
    if check(has_nth_order,[img,2],"HAS SECOND ORDER ROTATION "):
        if check(has_reflection,[img],"HAS REFLECTION"):
            pass
        else:
            if check(has_glidereflection,[img],"HAS GLIDE REFLECTION"):
                printf("WALLPAPER BELONGS TO PGG",FOREGROUND.cyan,BACKGROUND.purple)
            else:
                printf("WALLPAPER BELONGS TO P2",FOREGROUND.cyan,BACKGROUND.purple)
        return
    print("\n")
    if check(has_axis_reflection,[img],"HAS REFLECTION "):
        if check(has_glidereflection,[img],"HAS GLIDE REFLECTION"):
            printf("WALLPAPER BELONGS TO CM",FOREGROUND.cyan,BACKGROUND.purple)
        else:
            printf("WALLPAPER BELONGS TO PM",FOREGROUND.cyan,BACKGROUND.purple)
        return
    if check(has_glidereflection,[img],"HAS GLIDE REFLECTION"):
        printf("WALLPAPER BELONGS TO PG",FOREGROUND.cyan,BACKGROUND.purple)
    else:
        printf("WALLPAPER BELONGS TO P1",FOREGROUND.cyan,BACKGROUND.purple)
    

if __name__ == "__main__":
    log_function(EnableAnsi)
    if(len(sys.argv)>1):
        main(sys.argv[1])
    else:
        printf("NO IMAGES PROVIDED",fgcolor=FOREGROUND.yellow,bgcolor=BACKGROUND.red)
        input()

input()