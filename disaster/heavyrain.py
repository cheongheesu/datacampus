from bs4 import BeautifulSoup
import requests
import pymongo

url= 'https://terms.naver.com/entry.naver?docId=5830599&categoryId=42918&cid=42918'
response = requests.get(url)
response.encoding = 'utf-8'  # Set the response encoding to UTF-8
html = response.text

soup = BeautifulSoup(html, 'html.parser')

sections = [1, 2, 3, 4, 5, 7]

text_data = []

for section in sections:
    selector = f'#TABLE_OF_CONTENT{section}'
    title = soup.select_one(selector)
    print(title.get_text())

    if section == 1:
        start_range, end_range = 4, 10
    elif section == 2:
        start_range, end_range = 11, 17
    elif section == 3:
        start_range, end_range = 18, 22
    elif section == 4:
        start_range, end_range = 23, 27
    elif section == 5:
        start_range, end_range = 28, 39
    elif section == 7:
        start_range, end_range = 44, 47

    
    if section != 5 and section != 7:
        selector = f'#size_ct > div:nth-child({start_range})'
        detail = soup.select_one(selector)
        print(detail.get_text())
        
        if section != 5:
            section_content = {"title": title.get_text(), "text": detail.get_text()}
            for i in range(start_range + 1, end_range):
                selector = f'#size_ct > p:nth-child({i})'
                action = soup.select_one(selector)
                print(action.get_text())
                section_content["text"] += "\n" + action.get_text()
            text_data.append(section_content)
            
    elif section == 7:
        section_content = {"title": title.get_text(), "text": ''}
        for i in range(start_range, end_range):
            selector = f'#size_ct > p:nth-child({i})'
            action = soup.select_one(selector)
            print(action.get_text())
            section_content["text"] += "\n" + action.get_text()
        text_data.append(section_content)
    
    else:
        section_content = {"title": title.get_text(), "text": ''}
        for i in range(start_range, end_range, 2):
            selector = f'#size_ct > p:nth-child({i})'
            action = soup.select_one(selector)
            print(action.get_text())
            section_content["text"] += "\n" + action.get_text()
        text_data.append(section_content)
    

# MongoDB 연결 정보
uri = 'mongodb://localhost:27017'  # MongoDB 서버 주소와 포트
dbName = 'disaster'  # 데이터베이스 이름
collectionName = 'heavyrain'  # 컬렉션 이름

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
        print(f"{len(result.inserted_ids)} documents inserted successfully")

        # 연결 닫기
        client.close()
        print('Disconnected from MongoDB')
    except Exception as e:
        print('Error during data insertion:', e)

# 데이터 삽입 함수 호출
insert_data_to_mongodb(text_data)

