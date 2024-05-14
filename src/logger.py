from console import *

def log_function(fn,parameters=None):
    printf(f"RUNNING ")
    printf(f"{fn.__name__} ",FOREGROUND.yellow)
    printf("AT ")
    printf(f"{fn.__module__} ",FOREGROUND.blue)
    printf("|")
    try:
        if parameters is not None:  
            out = fn(*parameters)
        else:
            out = fn()
        printf(f"TASK COMPLETED\n",FOREGROUND.white,BACKGROUND.green)
    except:
        out = -1
        printf(f"TASK FAILED\n",FOREGROUND.yellow,BACKGROUND.red)
    return out

