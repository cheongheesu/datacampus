# -*- coding: utf-8 -*-
"""mp4_to_text.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lrzaeOeJ0ERjWqQKiJpkiPGjP3eGGcCp

# mp4 파일에서 텍스트 추출
"""

! pip install git+https://github.com/openai/whisper.git -q

import whisper

model = whisper.load_model("large-v2")

def transcribe(audio):
  # input audio file name
  audio =  whisper.load_audio(audio)

  # transcribe the audio
  result = model.transcribe(audio)

  # extract the text and language information
  text = result["text"]
  language = result["language"]

  print(f"Detected language: {language}")
  return text

import os

folder_path = "/content/drive/MyDrive/Colab Notebooks/phishing_project/thisvoice"
num_files = 82  # 총 파일 개수

this_text_list=[]
for i in range(1, num_files + 1):
    file_name = f"this{i}.mp4"
    file_path = os.path.join(folder_path, file_name)

    if os.path.exists(file_path):
        print(f"Transcribing {file_name}...")
        this_text=transcribe(file_path)
        this_text_list.append(this_text)
    else:
        print(f"{file_name} not found.")

import pandas as pd
voice3 = pd.DataFrame({"Sentence":this_text_list})
voice3

os.chdir('/content/drive/MyDrive/Colab Notebooks/phishing_project')
voice3.to_csv('voice3.csv')

voice = pd.concat([voice,voice3])
voice

os.chdir('/content/drive/MyDrive/Colab Notebooks/phishing_project')
voice.to_csv('voice.csv')