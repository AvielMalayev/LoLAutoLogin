import pyautogui
import keyboard as k
import time


if "__main__" == __name__:
    # searching the game application
    k.press_and_release('win')
    time.sleep(0.15)
    k.write("League of Legends", delay=0.02)
    k.press_and_release('enter')

    # waiting until the game is loaded
    image1 = pyautogui.locateOnScreen(r'c:\MyPythonScripts\Lol_bot\client.png', confidence=0.9)
    image2 = pyautogui.locateOnScreen(r'c:\MyPythonScripts\Lol_bot\client1.png', confidence=0.9)
    count = 0
    while image1 is None and image2 is None:
        time.sleep(0.1)
        image1 = pyautogui.locateOnScreen(r'c:\MyPythonScripts\Lol_bot\client.png', confidence=0.9)
        image2 = pyautogui.locateOnScreen(r'c:\MyPythonScripts\Lol_bot\client1.png', confidence=0.9)
        count += 1
        if count == 70:
            if image1 is None and image2 is None:
                print("Too much time to load client")
                exit(0)
            else:
                break

    # take from a given file the password and username
    client = open(r"c:\MyPythonScripts\Lol_bot\client.txt")
    userName, Password = client.readlines()
    client.close()

    # enter user name and pass and pressing on the sign in button
    k.write(userName, delay=0.01)
    k.press_and_release('tab')
    k.write(Password, delay=0.01)

    button = pyautogui.locateOnScreen(r'c:\MyPythonScripts\Lol_bot\sign_in.png', confidence=0.5)
    pyautogui.click(button)


