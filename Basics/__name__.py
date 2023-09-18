''' idiom in Python used to determine whether a Python script is being run as 
    1. the main program (set to "__main__" in this case) or 
    2. if it's being imported as a module into another script (set to the name of the script importing this script)
'''

# Calling this script directly
if __name__ == "__main__":
    print("This script is being ran directly")

if __name__ == "NameOfAScript":
    print("This script is being imported in another script and that script is calling this one")