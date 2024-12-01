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
sound_threads = {}

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

def play_sound(frequency, stop_event):
  
    file_path = generate_wave_file(frequency)
    while not stop_event.is_set():
        winsound.PlaySound(file_path, winsound.SND_FILENAME | winsound.SND_ASYNC)
        stop_event.wait(0.1)  

def on_press(key):
    
    if key == keyboard.Key.up and keyboard.Key.up not in pressed_keys:
        pressed_keys.add(keyboard.Key.up)
        stop_event = threading.Event()
        sound_thread = threading.Thread(target=play_sound, args=(523, stop_event))
        sound_threads[keyboard.Key.up] = stop_event
        sound_thread.start()
    elif key == keyboard.Key.down and keyboard.Key.down not in pressed_keys:
        pressed_keys.add(keyboard.Key.down)
        stop_event = threading.Event()
        sound_thread = threading.Thread(target=play_sound, args=(587, stop_event))
        sound_threads[keyboard.Key.down] = stop_event
        sound_thread.start()
    elif key == keyboard.Key.left and keyboard.Key.left not in pressed_keys:
        pressed_keys.add(keyboard.Key.left)
        stop_event = threading.Event()
        sound_thread = threading.Thread(target=play_sound, args=(659, stop_event))
        sound_threads[keyboard.Key.left] = stop_event
        sound_thread.start()
    elif key == keyboard.Key.right and keyboard.Key.right not in pressed_keys:
        pressed_keys.add(keyboard.Key.right)
        stop_event = threading.Event()
        sound_thread = threading.Thread(target=play_sound, args=(698, stop_event))
        sound_threads[keyboard.Key.right] = stop_event
        sound_thread.start()
    elif hasattr(key, 'char'):
        if key.char == 'a' and 'a' not in pressed_keys:
            pressed_keys.add('a')
            stop_event = threading.Event()
            sound_thread = threading.Thread(target=play_sound, args=(784, stop_event))
            sound_threads['a'] = stop_event
            sound_thread.start()
        elif key.char == 's' and 's' not in pressed_keys:
            pressed_keys.add('s')
            stop_event = threading.Event()
            sound_thread = threading.Thread(target=play_sound, args=(880, stop_event))
            sound_threads['s'] = stop_event
            sound_thread.start()
        elif key.char == 'd' and 'd' not in pressed_keys:
            pressed_keys.add('d')
            stop_event = threading.Event()
            sound_thread = threading.Thread(target=play_sound, args=(987, stop_event))
            sound_threads['d'] = stop_event
            sound_thread.start()
        elif key.char == 'f' and 'f' not in pressed_keys:
            pressed_keys.add('f')
            stop_event = threading.Event()
            sound_thread = threading.Thread(target=play_sound, args=(1046, stop_event))
            sound_threads['f'] = stop_event
            sound_thread.start()

    elif key == keyboard.Key.space:
  
        for stop_event in sound_threads.values():
            stop_event.set()

def on_release(key):
   
    if key in pressed_keys:
        pressed_keys.remove(key)
      
        if key in sound_threads:
            stop_event = sound_threads.pop(key)
            stop_event.set()  


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
