# BeautifulSoup 다운로드 링크
# https://www.crummy.com/software/BeautifulSoup/bs4/download/

# 링크에서 다운 받는 방법 말고 pip 사용하여 훨씬 더 간단하게 설치 가능
# cmd창에서 pip install bs4 입력하면 설치 완! << 버전이 오래돼서
# python.exe -m pip install --upgrade pip 입력

# BeautifulSoup 크롤링 순서
# 1. 크롤링 할 html 문서 가져오기

# 2. BeautifulSoup 분석

# 3. 태그 찾기 명령

from bs4 import BeautifulSoup
html = """
<html>
    <head>
        <title> HTML 연습 </title>
    </head>
    <body>
        <p align="center"> 텍스트 내용1 </p>
        <p align="center"> 텍스트 내용2 </p>
        <p align="center"> 텍스트 내용3 </p>
        <img src = "c:\\Users\\test_img.png" width="250">
    </body>
</html>
"""

bs = BeautifulSoup(html,'html.parser') #여기서 html은 html문서가 들어 있는 변수 이름
                        # .parser는 html 문서를 분석하는 도구 이름
print(bs.find('title')) # bs에서 ''안에 있는 내용을 찾아라
# >> <title> HTML 연습 </title>


# find() 함수 - 하나의 결괏값 가져오기
bs.find('p', align="center") # p태그를 찾아라! 그러나, find()함수는 제일 먼저 나오는 한 건만 출력한다
# 태그와 같은 여러개가 있을 때, 구분하기 위해 align이라는 속성을 사용함(결과값을 구분하기 위해서 속성을 상세하게 적어줌)
# >> <p align="center"> text content 1 </p>

bs.find('p', align="right")
# >> <p align="right"> text content 1 </p>

bs.find('p', align="left")
# >> <p align="left"> text content 1 </p>


# all() 함수 - 모든 결괏값 가져오기
bs = BeautifulSoup(html,'html.parser')
bs.find_all('p') # 속성과 관계없이 ''에 해당되는 내용을 모두 가져옴


# p태그와 img태그 같이 찾고 싶을 때
body_tag = bs.find('body') # body태그 부분을 변수에 담기

list_1 = body_tag.find_all(['p','img']) # 태그 여러개 가져오기 → 리스트[] 사용
for tag in list_1 :
    print(tag)
# >> <p align="center"> 텍스트 내용1 </p>
# <p align="center"> 텍스트 내용2 </p>
# <p align="center"> 텍스트 내용3 </p>
# <img src="c:\Users\test_img.png"/>


# 특정 문자열만 가져오고 싶어!
bs.find_all('p') # >> p태그 가져와주세요
# >> [<p align="center"> 텍스트 내용1 </p>, <p align="center"> 텍스트 내용2 </p>, <p align="center"> 텍스트 내용3 </p>]
# 글자(내용)만 찾고 싶은데, 태그와 속성 이런 거 다 나옴 ↑
# 검색해보니 내부 항목만 결과로 얻어올 수 있게 .text 사용
print(bs.text)
# >> 텍스트 내용1 텍스트 내용2 텍스트 내용3

# 또한 limit 키워드 사용, 2개의 p태그를 불러옴
bs.find_all("p",limit=2)


# 또한
# 정규식으로 특정 문자열 가져오기!
import re # 정규식 모듈
bs.find_all(text=re.compile("text"))


# 찾고 싶은 패턴 지정, p로 시작하는 부분
tags = bs.find_all(re.compile("^p"))
tags
# >> [<p align="center"> 텍스트 내용1 </p>, <p align="center"> 텍스트 내용2 </p>, <p align="center"> 텍스트 내용3 </p>]


# 중복되는 태그 구분하기
bs.find_all(align="center")
# >> align속성이 "center"인 것만 불러옴

bs.find_all(width="250")
# >> width속성이 "250"인 것만 불러옴


# String 키워드를 이용해 문장 가져오기
body_tag = bs.find('body') # body 태그 안에 있는 모든 태그 가져오기
p_tag = body_tag.find('p')
p_tag.string #string만 가져옴(하나만 가져옴)

strings = body_tag.strings # string 다 보고 싶다! for문 이용
for string in strings :
    print(string)


# 많이 사용하는 함수 get_text()
# 특정 태그를 지정하면 그 태그 안에 있는 텍스트 추출
body_tag = bs.find('body')
body_tag.get_text('-',strip=True) # '-'텍스트를 구분해주는 기호, #strip은 출력되는 내용에서 \n(띄어쓰기) 기호를 지워줌
