import threading
from pynput import keyboard
import winsound

# Flag to manage the playing state
playing = False
current_thread = None

def play_sound(frequency):
    global playing
    while playing:
        winsound.Beep(frequency, 500)  # 100 ms duration

def on_press(key):
    global playing, current_thread
    if not playing:
        playing = True
        if key == keyboard.Key.up:
            current_thread = threading.Thread(target=play_sound, args=(523,))
        elif key == keyboard.Key.down:
            current_thread = threading.Thread(target=play_sound, args=(587,))
        elif key == keyboard.Key.left:
            current_thread = threading.Thread(target=play_sound, args=(659,))
        elif key == keyboard.Key.right:
            current_thread = threading.Thread(target=play_sound, args=(698,))
        elif hasattr(key, 'char') and key.char == 'a':
            current_thread = threading.Thread(target=play_sound, args=(784,))
        elif hasattr(key, 'char') and key.char == 's':
            current_thread = threading.Thread(target=play_sound, args=(880,))
        elif hasattr(key, 'char') and key.char == 'd':
            current_thread = threading.Thread(target=play_sound, args=(987,))
        elif hasattr(key, 'char') and key.char == 'f':
            current_thread = threading.Thread(target=play_sound, args=(1046,))
        
        # Start the thread if a valid key was pressed
        if current_thread:
            current_thread.start()

def on_release(key):
    global playing, current_thread
    playing = False
    if current_thread and current_thread.is_alive():
        current_thread.join()

# Set up the keyboard listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
