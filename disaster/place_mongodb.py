import pandas as pd
import json

############ csv 파일 to json 파일 ###################
def csv_to_json(csv_path, json_path):
    # CSV 파일을 읽어옵니다.
    df = pd.read_csv(csv_path, encoding='cp949')

    # 데이터프레임을 JSON 형식으로 변환합니다.
    json_data = df.to_json(orient='records', lines=True)

    # JSON 파일로 저장합니다.
    with open(json_path, 'w') as f:
        f.write(json_data)

# 드라이브에 있는 CSV 파일의 경로와 JSON 파일로 저장할 경로를 지정합니다.
csv_file_path = 'C:/Users/sport/OneDrive/바탕 화면/visualcode/seoul_place.csv'
json_file_path = 'C:/Users/sport/OneDrive/바탕 화면/visualcode/seoul_place.json'

# 함수를 호출하여 CSV 파일을 JSON 파일로 변환합니다.
csv_to_json(csv_file_path, json_file_path)

############ 콤마 빠진 손상된 json 복구 함수 ##################
def fix_json_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        data = file.read()

    # 파일 내의 여러 JSON 객체를 배열로 묶기
    fixed_data = "[" + data.replace('}\n{', '},\n{') + "]"

    # 새로운 JSON 파일로 저장
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(fixed_data)

# 만든 함수를 이용해 손상된 json 복구
# input 및 output 경로는 google drive 연동 후 지정할것.
if __name__ == "__main__":
    input_file_path = 'C:/Users/sport/OneDrive/바탕 화면/visualcode/seoul_place.json'
    output_file_path = 'C:/Users/sport/OneDrive/바탕 화면/visualcode/seoul_place.json'

    try:
        fix_json_file(input_file_path, output_file_path)
        print("정상적으로 JSON 파일을 저장했습니다.")
    except Exception as e:
        print("오류가 발생하여 JSON 파일을 저장하지 못했습니다.")
        print(f"오류 내용: {str(e)}")


# 파일 출력해서 확인해보기
file_path = 'C:/Users/sport/OneDrive/바탕 화면/visualcode/seoul_place.json'

json_data = []
with open(file_path, 'r') as f:
  json_data = json.load(f)

# indent를 기준으로 결과를 출력합니다.
print(json.dumps(json_data, indent=4, ensure_ascii=False))


############### json 파일 불러와서 mongodb에 저장하기 ############

import pymongo
import json

# MongoDB 연결 정보
uri = 'mongodb://localhost:27017'  # MongoDB 서버 주소와 포트
dbName = 'disaster'  # 데이터베이스 이름
collectionName = 'place'  # 컬렉션 이름

# JSON 파일 경로
json_file_path = 'C:/Users/sport/OneDrive/바탕 화면/visualcode/seoul_place.json'

# JSON 파일 불러오기
json_data = []
with open(json_file_path, 'r') as file:
    json_data = json.load(file)


# MongoDB에 데이터 삽입
def insert_data_to_mongodb():
    try:
        # MongoDB 클라이언트 연결
        client = pymongo.MongoClient(uri)
        print('Connected to MongoDB')

        # 데이터베이스와 컬렉션 참조
        db = client[dbName]
        collection = db[collectionName]

        # 데이터 삽입
        result = collection.insert_many(json_data)
        print(f"{len(result.inserted_ids)} documents inserted")

        # 연결 닫기
        client.close()
        print('Disconnected from MongoDB')
    except Exception as e:
        print('Error during data insertion:', e)

# 데이터 삽입 함수 호출
insert_data_to_mongodb()
