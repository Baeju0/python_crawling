# 텍스트 파일 내용 불러와서
# 리스트에 담기

import os
import pandas as pd

f = open('c:\\temp\\url_list.txt','r')

txt = f.readlines() # 여러 줄의 데이터를 한꺼번에 읽어 오기
print(txt)

naver = []
daum = []
tistory = []

for i in range(0, len(txt)) :
    txt2 = txt[i].split('/')
    txt3 = txt2[2].replace("\n","")

    if txt3 == 'blog.naver.com' :
        naver.append(txt[i])

    elif txt3 == 'blog.daum.net' :
        daum.append(txt[i])

    else :
        tistory.append(txt[i])

url = pd.DataFrame() # DataFrame은 데이터 프레임을 생성하는 것으로, 표를 생성할 수 있다

url['Naver url 주소'] = naver
url['Daum url 주소'] = daum
url['Tistory url 주소'] = tistory

os.makedirs('c:\\temp\\temp4') # temp4 폴더 생성

# csv 파일, excel 파일 생성
url.to_csv('c:\\temp\\temp4\\url_list.csv', encoding='utf-8-sig', index=True)
url.to_excel('c:\\temp\\temp4\\url_list.xls') # 엑셀 파일은 최신 확장자인 .xlsx 사용하기(xls는 구버전이라 에러 뜰 수 있음)