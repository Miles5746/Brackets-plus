# Brackets-plus
By Miles5746 and ChatGPT

This is my first every script on Github! The point of this is to make life a tiny bit easier, by automating brackets. it automaticly completes brackets whenever you type (. Sadly, I ran into
an error when making this, where it selects the second bracket, so I made two versions: Brackets Plus and Brackets Pro. 

Brackets Plus: Pretty straight forward. Generates the ) when you type ( but won't move your cursor in between them.

Brackets Pro: When you type (, it will wait for you to type a lower-case letter to ensure shift isn't being hold, and then completes the operation. This can glitch out when you are typing to fast, so if you are fine with moving your cursor I would recommend Brackets Plus insteed.

Please note that the first time you use this, it glitches and generates a 0 insteed of a ), but it is only the first time you run it.

This requires macOS, unless you find a way to do it on windows or linux, as the files are in python.
How to run correctly:
1. Open terminal (Cmd+space, then type terminal)
2. Download or create a python with the script of your choice in it, and move it to documents.
3. Download Homebrew (Unless you already have) at https://brew.sh/ and set it up.
4. Type in terminal: Brew install python3 (Unless you already have python3 in terminal)
5. Type in terminal: pip install pynput
6. Type in terminal: pip install pyautogui
7. Make sure terminal has accesibility (Settings > Privacy & Security > Accessibility > Add terminal with the + at the bottem of the list.)
8. Type in terminal: cd /user/yournamehere/documents/
9. Type in terminal: python3 BracketsPlus (or BracketsPro if you got that)
10. It will be running now!
11. To exit, go to terminal and press cntrl+c

Thank you for using this script, you are free to edit/reupload it how ever you like, as it isn't that big!

-Miles5746, Thank you for looking at this!
