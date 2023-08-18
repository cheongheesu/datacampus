import pandas as pd

txt_path = "C:/Users/sport/OneDrive/바탕 화면/visualcode/project/voicephishing/personate/script43.txt"
df = pd.read_table(txt_path)

new_row = pd.Series(df.columns.tolist(), index=df.columns)
df = pd.concat([pd.DataFrame([new_row]), df], ignore_index=True)
df.columns = ['text']
df['text'] = df['text'].str.replace('피해자 : ', '').str.replace('사기범 : ','').str.strip()

print(df)

output_path = "C:/Users/sport/OneDrive/바탕 화면/visualcode/project/voicephishing/personate/script43.csv"
df.to_csv(output_path)