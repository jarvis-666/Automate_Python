import webbrowser
import sys
import pyperclip

def main():
    print("Google Maps Utility Tool")
    while(True):
        print('How do you want to give data?: 1. CLI args or 2. Clipboard')
        try:
            n = int(input())
            if n != 1 and n != 2:
                raise Exception
        except:
            print("Did not enter the right input... Do you want to quit?")
            choice = input()[0].lower()
            if choice == 'y':
                break
            else:
                print("Please enter the right option")
                continue
        else:
            template = "https://www.google.com/maps/place/"
            location = str()
            if n == 1:
                location = ' '.join(sys.argv[1:])
            elif n == 2:
                location = pyperclip.paste()
            print("Received location from CLI args as,", location, "... Processing")
            template += location.replace(' ', '%20')
            print(template)
            webbrowser.open(template)
        finally:
            print('Thanks for using the utility')

if __name__ == "__main__":
    main()