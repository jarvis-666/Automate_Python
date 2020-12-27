import traceback

def spam():
    bacon()

def bacon():
    raise Exception('This is the error message.')

try:
    spam()
except Exception:
    with open("log_traceback.txt", 'w') as f:
        f.write(traceback.format_exc())
    print("Traceback text was logged in to view later while debugging")

# traceback is generated whenever an exception is raised unhandled in try and except

# traceback.format_exc() is used in case when we want the traceback information but also want to handle the
    # exception gracefully, without terminating the program
# it prints a string of the complete traceback text


