#! python3
# assertions shouldn't be in the try-except block
    # they should just terminate the program, if the given condition is a fallocy

# assertions are for programmer errors and not to handle user errors

# using assertions in your code makes it to fail faster, shorten the time between original cause of the bug and when
    # you actually notice the bug
        # this reduces the amount of code that needs to be checked for bugs, because you are using safeguards to ensure
            # the sanity is maintained in the code

#
# a, b = 3, 0
#
# assert b != 0, "Can't divide by zero"
#
# print(a // b)


list_of_temperatures = [40, 26, 39, 30, 25, 21]

for temp in list_of_temperatures:
    assert temp >= 26, "Whole batch has been rejected"
    print(f"{temp} means hot")