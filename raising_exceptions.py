try:
    # raise Exception("This is the error message")
    print(1 // 0)
except ZeroDivisionError:
    print("Hello")
    raise
except Exception:
    print("Hello world")
    raise       # the program simply crashes and displays the exception's error message