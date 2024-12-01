import threading
from pynput import keyboard
import winsound
import wave
import numpy as np
import os


WAV_DIR = "sound_files"
if not os.path.exists(WAV_DIR):
    os.makedirs(WAV_DIR)


pressed_keys = set()

def generate_wave_file(frequency, duration=10, sample_rate=44100):
  
    file_path = os.path.join(WAV_DIR, f"{frequency}Hz.wav")
    if not os.path.exists(file_path):
        t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
        wave_data = (0.5 * np.sin(2 * np.pi * frequency * t) * 32767).astype(np.int16)

        with wave.open(file_path, "w") as wav_file:
            wav_file.setnchannels(1)  
            wav_file.setsampwidth(2)  
            wav_file.setframerate(sample_rate)
            wav_file.writeframes(wave_data.tobytes())
    return file_path

def play_sound(frequency):
 
    file_path = generate_wave_file(frequency)
    winsound.PlaySound(file_path, winsound.SND_FILENAME | winsound.SND_ASYNC)

def on_press(key):
    
    if key == keyboard.Key.up and keyboard.Key.up not in pressed_keys:
        pressed_keys.add(keyboard.Key.up)
        threading.Thread(target=play_sound, args=(523,)).start()  
    elif key == keyboard.Key.down and keyboard.Key.down not in pressed_keys:
        pressed_keys.add(keyboard.Key.down)
        threading.Thread(target=play_sound, args=(587,)).start() 
    elif key == keyboard.Key.left and keyboard.Key.left not in pressed_keys:
        pressed_keys.add(keyboard.Key.left)
        threading.Thread(target=play_sound, args=(659,)).start()  
    elif key == keyboard.Key.right and keyboard.Key.right not in pressed_keys:
        pressed_keys.add(keyboard.Key.right)
        threading.Thread(target=play_sound, args=(698,)).start()  
    elif hasattr(key, 'char'):
        if key.char == 'a' and 'a' not in pressed_keys:
            pressed_keys.add('a')
            threading.Thread(target=play_sound, args=(784,)).start() 
        elif key.char == 's' and 's' not in pressed_keys:
            pressed_keys.add('s')
            threading.Thread(target=play_sound, args=(880,)).start()  
        elif key.char == 'd' and 'd' not in pressed_keys:
            pressed_keys.add('d')
            threading.Thread(target=play_sound, args=(987,)).start()  
        elif key.char == 'f' and 'f' not in pressed_keys:
            pressed_keys.add('f')
            threading.Thread(target=play_sound, args=(1046,)).start()  

def on_release(key):
 
    if key in pressed_keys:
        pressed_keys.remove(key)
    
    if len(pressed_keys) == 0:
        winsound.PlaySound(None, winsound.SND_ASYNC)


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
