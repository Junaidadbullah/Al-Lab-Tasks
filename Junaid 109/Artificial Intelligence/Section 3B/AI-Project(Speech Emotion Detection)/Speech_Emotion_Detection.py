import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np
import librosa
import pickle


with open('emotion_speech_recognition_model.pkl', 'rb') as f:
    model = pickle.load(f)


def extract_features_from_audio(file_path):
    y, sr = librosa.load(file_path, sr=None)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    mfcc_mean = np.mean(mfcc, axis=1)
    
    return mfcc_mean

def classify_audio_file(file_path):
    mfcc_features = extract_features_from_audio(file_path)

    mfcc_features = mfcc_features.reshape(1, -1)
    
    prediction = model.predict(mfcc_features)
    
    result_label.config(text=f"Predicted Emotion: {prediction[0]}")
    print(f"Predicted Emotion: {prediction[0]}")

def upload_audio_file():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav;*.mp3;*.flac")])
    
    if file_path:
        classify_audio_file(file_path)
    else:
        messagebox.showwarning("No File", "Please select a valid audio file.")

root = tk.Tk()
root.title("Emotion Recognition from Audio File")
root.geometry("400x300")


result_label = tk.Label(root, text="Predicted Emotion: ", font=("Helvetica", 14))
result_label.pack(pady=20)


upload_button = tk.Button(root, text="Upload Audio File", font=("Helvetica", 14), command=upload_audio_file)
upload_button.pack(pady=20)


root.mainloop()
