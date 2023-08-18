# -*- coding: utf-8 -*-
"""whisperSTT.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zy-ST3iYF82UWOb9YqqJvywrJyzg5yqd

# Whisper 설치
"""

! pip install git+https://github.com/openai/whisper.git -q

"""# 보이스피싱 오디오 출력 예시"""

from IPython.display import Audio
Audio("/content/drive/MyDrive/Colab Notebooks/phishing_project/NR6688_마스킹 완료_금융회사_.mp3")

"""# STT 자동화 코드 만들기

# Whisper 모델 로드
"""

import whisper

model = whisper.load_model("large-v2")

"""# 보이스피싱 음성 실험 데이터 STT 실행"""

import os

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

# STT 출력 예시
hard_text = transcribe("/content/drive/MyDrive/Colab Notebooks/phishing_project/NR6688_마스킹 완료_금융회사_.mp3")
print(hard_text)

folder_path = "/content/drive/MyDrive/Colab Notebooks/phishing_project/voise1"
num_files = 186  # 총 파일 개수

loan_text_list=[]
for i in range(1, num_files + 1):
    file_name = f"loan{i}.mp3"
    file_path = os.path.join(folder_path, file_name)

    if os.path.exists(file_path):
        print(f"Transcribing {file_name}...")
        loan_text=transcribe(file_path)
        loan_text_list.append(loan_text)
    else:
        print(f"{file_name} not found.")

loan_list = loan_text_list.copy()

import pandas as pd
voice1 = pd.DataFrame({"Sentence":loan_list})
voice1

os.chdir('/content/drive/MyDrive/Colab Notebooks/phishing_project')
voice1.to_csv('voice1.csv')

import os



folder_path = "/content/drive/MyDrive/Colab Notebooks/phishing_project/voise2"
num_files = 226  # 총 파일 개수

police_text_list=[]
for i in range(1, num_files + 1):
    file_name = f"police{i}.mp3"
    file_path = os.path.join(folder_path, file_name)

    if os.path.exists(file_path):
        print(f"Transcribing {file_name}...")
        police_text=transcribe(file_path)
        police_text_list.append(police_text)
    else:
        print(f"{file_name} not found.")

import pandas as pd
voice2 = pd.DataFrame({"Sentence":police_text_list})
voice2

os.chdir('/content/drive/MyDrive/Colab Notebooks/phishing_project')
voice2.to_csv('voice2.csv')

voice = pd.concat([voice1,voice2])
voice

os.chdir('/content/drive/MyDrive/Colab Notebooks/phishing_project')
voice.to_csv('voice.csv')