import os
import webbrowser

# Specify the path to the folder you want to open in VS Code
question = input('What do you want to open: 1.Boards, 2.Chrome, 3.VS Code \n Please enter the repsective number: ')

if int(question) == 1:
    url = "https://schouw.visualstudio.com/Foodware%20365%20BC/_boards/board/t/Customer%20Success%20Team/Stories"
    webbrowser.open(url)

if int(question) == 3:
    folder_name = input("Enter the folder name: ")
    folder_path = os.path.abspath('C:\Aptean'+'\\'+folder_name)
# Use the appropriate command to open the folder in VS Code based on the operating system
    if os.name == 'posix':  # Unix-based systems (Linux, macOS)
        os.system(f'code {folder_path}')
    elif os.name == 'nt':  # Windows
        os.system(f'code "{folder_path}"')
    else:
        print("Unsupported operating system")
if int(question) == 2:
    url = "https:://www.Google.com"
    webbrowser.open(url)
