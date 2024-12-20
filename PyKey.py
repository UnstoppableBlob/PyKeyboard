from pynput import keyboard
import pyaudio
import numpy as np
import threading

rate1 = 44100*3


p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32, channels=1, rate=rate1, output=True)

playing = False

def play_sound(frequency):
    global playing
    phase = 0
    while playing:
        length = 0.1 
        samples = (np.sin(2 * np.pi * np.arange(rate1 * length) * frequency / rate1 + phase)).astype(np.float32)
        stream.write(0.5 * samples)
        phase += 2 * np.pi * frequency / rate1 * rate1 * length



def on_press(key):
    global playing
    if not playing:
        playing = True
        if key == keyboard.Key.up:
            threading.Thread(target=play_sound, args=(523,)).start()   
        elif key == keyboard.Key.down:
            threading.Thread(target=play_sound, args=(587,)).start()  
        elif key == keyboard.Key.left:
            threading.Thread(target=play_sound, args=(659,)).start() 
        elif key == keyboard.Key.right:
            threading.Thread(target=play_sound, args=(698,)).start() 
        elif key == keyboard.KeyCode(char='a'):
            threading.Thread(target=play_sound, args=(784,)).start() 
        elif key == keyboard.KeyCode(char='s'):
            threading.Thread(target=play_sound, args=(880,)).start() 
        elif key == keyboard.KeyCode(char='d'):
            threading.Thread(target=play_sound, args=(987,)).start() 
        elif key == keyboard.KeyCode(char='f'):
            threading.Thread(target=play_sound, args=(1046,)).start() 

def on_release(key):
    global playing
    playing = False


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


stream.stop_stream()
stream.close()
p.terminate()