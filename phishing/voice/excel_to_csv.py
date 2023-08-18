import pandas as pd

excel_path = "C:/Users/sport/OneDrive/바탕 화면/visualcode/project/voicephishing/personate/script24.xlsx"
df = pd.read_excel(excel_path)

new_row = pd.Series(df.columns.tolist(), index=df.columns)
df = pd.concat([pd.DataFrame([new_row]), df], ignore_index=True)
df.columns = ['text']
df['text'] = df['text'].str.replace('피해자 : ', '').str.replace('사기범 : ','').str.strip()

print(df)

output_path = "C:/Users/sport/OneDrive/바탕 화면/visualcode/project/voicephishing/personate/script24.csv"
df.to_csv(output_path)
