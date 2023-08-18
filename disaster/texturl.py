import json
from textwrap import indent
import requests
import xmltodict
import pymongo

url = 'http://apis.data.go.kr/1741000/DisasterMsg3/getDisasterMsg1List'
params ={'serviceKey' : 'V7GqQuNPFr7BW9lTC/8+d6/8iu653AZHsgn/gKrciYV8AAEYM8yX1satHogBb5zNmjNP1VLo1xaHEEd9D4XckQ==', 'pageNo' : '1', 'numOfRows' : '', 'type' : 'xml' }

response = requests.get(url, params=params)

xmlData = response.text
jsonStr = json.dumps(xmltodict.parse(xmlData))
dict = json.loads(jsonStr)
print(json.dumps(dict, indent=4, ensure_ascii=False))

# 데이터 형태확인
print(jsonStr)

# 'row' 키에 해당하는 값들을 리스트로 변환
items = dict['DisasterMsg']['row']
if not isinstance(items, list):
    items = [items]

# MongoDB 연결 정보
uri = 'mongodb://localhost:27017'  # MongoDB 서버 주소와 포트
dbName = 'disaster'  # 데이터베이스 이름
collectionName = 'text'  # 컬렉션 이름

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
        result = collection.insert_many(items)
        print(f"{len(result.inserted_ids)} documents inserted")

        # 연결 닫기
        client.close()
        print('Disconnected from MongoDB')
    except Exception as e:
        print('Error during data insertion:', e)

# 데이터 삽입 함수 호출
insert_data_to_mongodb()
