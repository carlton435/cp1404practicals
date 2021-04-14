"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"ALICEBLUE": "#f0f8ff", "ANTIQUEWHITE": "#faebd7", "ANTIQUEWHITE1": "#ffefdb",
                "ANTIQUEWHITE2": "#eedfcc", "ANTIQUEWHITE3": "#cdc0b0", "ANTIQUEWHITE4": "#8b8378",
                "AQUAMARINE1": "#7fffd4", "AQUAMARINE2": "#76eec6", "AQUAMARINE4": "#458b74", "AZURE1": "#f0ffff"}
print(CODE_TO_NAME)

state_code = input("Enter the name of color: ")
state_code = state_code.upper()
while state_code != "":
    if state_code in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter the name of color: ")