from operator import truediv
import requests
from bs4 import BeautifulSoup
import datetime
from pymongo import MongoClient
from pymongo.cursor import CursorType

mongo = MongoClient("localhost", 20000)

def mongo_save(mongo, datas, db_name=None, collection_name=None):
    result = mongo[db_name][collection_name].insert_many(datas).inserted_ids
    return result

list = []
aid = 1  
result = 0

while True:
    
    aid_string = format(aid, '010')

    try:
        html = requests.get(
            f"https://entertain.naver.com/read?oid=005&aid={aid_string}&sid=100")

        if html.status_code == 200:

            soup = BeautifulSoup(html.text, 'html.parser')

            title = soup.select_one(".end_tit").text
            company = soup.select(".press_logo > img")[0]["alt"]
            createdAt = datetime.datetime.now()

            dict = {"title": title, "company": company, "createdAt": createdAt}
            list.append(dict)
            print(len(list))

            result += 1

        if result == 20:
            print("다운로드 종료")
            break

        aid += 1

    except Exception as e:
        print("문제발생")
        pass

aaa = mongo_save(mongo, list, "greendb", "navers")  # List안에 dict을 넣어야 함
print(aaa)