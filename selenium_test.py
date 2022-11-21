# 환경 설정하기

# 1. python 버전 확인

# 2. BeautifulSoup 설치
# - pip install bs4

# 3. selenium 설치
# cmd창에 pip install selenium

# 4. selenium 크롬 드라이버 설치
# 버전 확인하기 (무조건 최신 버전 x / 검증된 버전 o)
# 다운로드 클릭 후 나오는 페이지에서 Parent Directory 클릭

# 이번에는 2.40 version 사용, window버전 설치
# ↑ 에러 발생, 너무 낮은 버전, 최근에 나온 버전으로 설치해봤더니 다시 오류
# webdriver-manager 설치(최신버전의 크롬 드라이버 자동으로 사용하게 해주는)
# pip install webdriver-manager

# 다운로드 후 압축풀기하면 cmd창과 같이 생긴 파일을 얻을 수 있음
# 셀레니움이 파일을 이용하여 특정 정보를 추출해냄


# 라이브러리와 모듈 불러오기
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager # 크롬 드라이버 자동 최신

import time # time 모듈은 페이지가 열릴 때까지 기다리기 위해 사용함

query_txt = input('키워드 검색 : ')

# 크롬 드라이버 불러온 후 웹 브라우저 실행
path = "C:\Temp\sel\chromedriver.exe" # 크롬 드라이버 설치 경로(불러오기)
driver = webdriver.Chrome(path)
# ↓ 최신 버전 자동 설치 시 오류 발생
# 크롬의 버전 확인하고 이에 맞는 크롬 드라이버 버전 설치(현재 ver.107)


# 크롬 드라이버 최신 버전 자동 설치
# driver = webdriver.Chrome(ChromeDriverManager().install())
# ↑ ※ 시스템에 부착된 장치가 작동하지 않습니다. 라는 오류가 발생한다

# 위의 오류 해결방법?
# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches",["enable-logging"])
# browser = webdriver.Chrome(options=options)

driver.get("https://korean.visitkorea.or.kr/main/main.do#home")
time.sleep(10) # 브라우저가 계속 켜져있는 것이 아닌 함수 종료시 브라우저도 같이 종료