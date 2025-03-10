import webbrowser
import os
import sys

YOUTUBE_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
CORRECT_ANSWER = 1
EXIT_COMMAND = "exit"

def ask_math_question():
    while True:
        try:
            user_input = input("1 times 1 = ? ").strip()
            if user_input.isdigit() and int(user_input) == CORRECT_ANSWER:
                open_video()
                break
            elif user_input.lower() == EXIT_COMMAND:
                sys.exit()
            else:
                print("Wrong! Try again.")
        except Exception as e:
            print(f"發生錯誤: {e}")

def open_video():
    webbrowser.open(YOUTUBE_URL)
    os.system("echo 'Playing video...'")

if __name__ == "__main__":
    ask_math_question()
