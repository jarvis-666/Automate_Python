try:
    list1 = [1, 2, 3]
    print(list1[0])
    print(list1[3])
except IndexError as i:
    print(f"Error Code: {i}")
    
try:  
    raise NameError("Hi there")  # Raise Error
except NameError:
    print("An exception")
    raise  # To determine whether the exception was raised or not