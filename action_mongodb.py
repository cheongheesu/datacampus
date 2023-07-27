from bs4 import BeautifulSoup
import requests
import pymongo

url="https://www.safekorea.go.kr/idsiSFK/neo/sfk/cs/contents/prevent/prevent18.html?menuSeq=126"

response = requests.get(url)
response.encoding = 'utf-8'  # Set the response encoding to UTF-8
html = response.text

soup = BeautifulSoup(html, 'html.parser')

# 재난시 행동요령 text f를 dictionary 형태로 추출
details=soup.select('div > div > div > div > div > p')
text_data = [{"text": detail.get_text()} for detail in details] 

# MongoDB 연결 정보
uri = 'mongodb://localhost:27017'  # MongoDB 서버 주소와 포트
dbName = 'disaster'  # 데이터베이스 이름
collectionName = 'action'  # 컬렉션 이름

# MongoDB에 데이터 삽입
def insert_data_to_mongodb(data):
    try:
        # MongoDB 클라이언트 연결
        client = pymongo.MongoClient(uri)
        print('Connected to MongoDB')

        # 데이터베이스와 컬렉션 참조
        db = client[dbName]
        collection = db[collectionName]

        # 데이터 삽입
        result = collection.insert_many(data)
        print(f"{len(result.inserted_ids)} documents inserted")

        # 연결 닫기
        client.close()
        print('Disconnected from MongoDB')
    except Exception as e:
        print('Error during data insertion:', e)

# 데이터 삽입 함수 호출
insert_data_to_mongodb(text_data)