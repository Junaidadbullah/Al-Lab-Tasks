import pandas as pd
import numpy as np
import os
import librosa
import librosa.display
from IPython.display import Audio
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report
import pickle

paths = []
labels = []
for dirname, _, filenames in os.walk('Tess'):
    for filename in filenames:
        paths.append(os.path.join(dirname, filename))
        label = filename.split('_')[-1]
        label = label.split('.')[0]
        labels.append(label.lower())

df = pd.DataFrame()
df['speech'] = paths
df['label'] = labels

def extract_features(file_path):
    y, sr = librosa.load(file_path, sr=None)
    
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    
    mfcc_mean = np.mean(mfcc, axis=1)
    
    return mfcc_mean


data = []
for path in df['speech']:
    data.append(extract_features(path))

data = np.array(data)


df_features = pd.DataFrame(data)
df_features['label'] = df['label'].values



X = df_features.drop('label', axis=1).values
y = df_features['label'].values


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = SVC(kernel='linear')
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


print(classification_report(y_test, y_pred))


with open('emotion_speech_recognition_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print(f"Total number of audio files: {len(df)}")
print(f"Number of samples used for training: {len(X_train)}")
