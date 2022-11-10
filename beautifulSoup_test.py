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
        <img src = "">
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