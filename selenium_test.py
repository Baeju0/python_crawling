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
# from webdriver_manager.chrome import ChromeDriverManager # 크롬 드라이버 자동 최신

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time # time 모듈은 페이지가 열릴 때까지 기다리기 위해 사용함

import sys # sys모듈은 웹페이지 조회 결과 수집할 때 사용

query_txt = input('크롤링할 키워드 검색 : ')
f_name = input('저장할 파일 경로와 이름 입력 : ')

# 크롬 드라이버 불러온 후 웹 브라우저 실행
path = "C:\Temp\sel\chromedriver.exe" # 크롬 드라이버 설치 경로(불러오기)
driver = webdriver.Chrome(path) # 예시:c:\\Temp\\test.txt
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
# time.sleep(3) # 페이지가 열릴 때 까지 3초동안 기다림

# 브라우저가 계속 켜져있는 것이 아닌 함수 종료시 브라우저도 같이 종료됨

# time.sleep()과 다른 방법, implicity_wait()의 차이
# time.sleep()은 ()에 입력한 시간동안 기다림(무조건 기다리기 때문에 지연됨)
# implicity_wait()은 엔진 자체에서 파싱되는 시간을 기다려줌(페이지가 다 열리면 다음 동작 시랭)
# 따라서 implicity_wait()를 사용하는 것이 더 효율적이다!
driver.implicitly_wait(5)


# 브라우저 꺼짐 방지 → 안 먹힘ㅠㅡㅠ
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)


# 검색창의 이름을 찾아서 검색어 입력하기
# driver.find_element_by_class_name("search").click()
driver.find_element(By.CLASS_NAME,"search").click()

# element = driver.find_element_by_id("inp_search")
element = driver.find_element(By.ID,"inp_search")

element.send_keys(query_txt)

# driver.find_element_by_link_text("검색").click()
driver.find_element(By.LINK_TEXT, "검색").click()

# 기존에 있던 코드가 자꾸 에러가 발생한다!?
# ↑해결, selenium이 version update에 따라 구문이 변경됐다.

# ＊ 검색 후 자동으로 브라우저가 종료됨
# 해결 방법 찾기

# ------------------------------------------------------
# 검색 후 결과 목록의 text 추출하기
time.sleep(1)

html = driver.page_source # 페이지의 모든 소스를 가져와라!
soup = BeautifulSoup(html,'html.parser')
list = soup.find('ul',class_='list_thumType type1') # soup.find는 해당 정보를 찾아줌(게시글 class 입력함, 정보 가져와라!)

for i in list :
    print(i.text.strip()) # text만 골라내라! strip함수는 문장의 좌우 공백 제거
    print("\n")

# ------------------------------------------------------
# 추출한 텍스트를 txt 형식으로 저장하기
# write 함수도 있지만
# sys.stdout 사용(모니터가 아닌 다른 곳으로 출력 방향 바꾸기)
stdout_test = sys.stdout
f = open(f_name, 'a', encoding='UTF-8') # 저장할 때 encoding은 확실하게!(안 하면 다 깨질 수도 있음)
                # 파일열기모드 'a'는 추가모드, 파일의 마지막에 새로운 내용을 추가 시킬 때 사용한다!(원래 있던 값 + 새로운 값 추가)
sys.stdout = f
# 위의 3줄 코드는 모니터에 출력하지 말고 지정된 파일에 저장하게 만듦

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
list = soup.find('ul',class_='list_thumType type1')

for i in list :
    print(i.text.strip())
    print("\n")

sys.stdout = stdout_test
f.close()
# 위에서 했던 검색 후 결과 목록 추출처럼 화면에 결과가 추출되지 않고
# 지정한 곳으로 출력(저장) 됨(위에 f_name변수에 입력한 파일 경로에 저장!)

print("데이터 수집 완료!")

# ------------------------------------------------------
# stackoverflow에서 찾은 해결 방법 (브라우저 종료에 대한)
while(True) :
    pass
# 위와 같은 코드를 추가해주니 자동으로 브라우저가 종료되지 않는다!!!예!