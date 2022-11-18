from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <h1> 장바구니
    </head>
    <body>
        <h1> 구매할 목록
            <div> <p id='fruits1' class='name1' title='바나나'> 바나나
                    <span class= 'price'> 3000원 </span>
                    <span class= 'count'> 10개 </span>
                    <span class= 'store'> 노브랜드 </span>
                    <a href = 'https://www.nobrand.com'>nobrand.com </a>
                </p>
            </div>
            <div> <p id='fruits2' class='name2' title='사과'> 사과
                    <span class= 'price'> 1000원 </span>
                    <span class= 'count'> 30개 </span>
                    <span class= 'store'> 예산사과 </span>
                    <a href = 'https://www.yesanSG.com'>yesanSG.com </a>
                </p>
            </div>
            <div> <p id='fruits3' class='name3' title='귤'> 귤
                    <span class= 'price'> 500원 </span>
                    <span class= 'count'> 50개 </span>
                    <span class= 'store'> 제주귤 </span>
                    <a href = 'https://www.jejuG.com'>jejuG.com </a>
                </p>
            </div>
"""

soup = BeautifulSoup(html,'html.parser')

# select() 함수
# find()랑 find_all()도 있는데 select()를 왜 써요?
# 웹사이트 마다 find가 유용할 수도 있고 select가 유용할 수도 있음

# 태그 골라내기
print(soup.select('p'))
# >> 모든 p태그 출력

# 태그를 사용하지 않고 범위를 좁힐 수 있는 클래스 사용 방법
# select('태그 이름')이 아닌
# select('.클래스')
soup.select('.name1')
# >> class 이름이 'name1'인 것만 추출


# 상위태그>하위태그>하위태그
soup.select('div > p > span') # ★★★ 태그 사이에 공백 꼭!!!!! 넣어줘야 됨 ★★★
# >> span 태그들 출력
# 첫 번째 값만 추출하고 싶어요 [0]
print(soup.select('div > p > span' ) [0])
# 두 번째 값만 추출 [1]
print(soup.select('div > p > span' ) [1])
# 세 번째 값만 추출 [2]
print(soup.select('div > p > span' ) [2])
# 위와 같이 추출하고 싶은 위치값 []리스트 입력


# 상위태그.클래스이름 > 하위태그.클래스이름
# 바나나 가게 이름만 출력하고 싶어요
print(soup.select('p.name1 > span.store'))


# 아이디명으로도 추출 가능
# soup.select('#아이디명')
print(soup.select('#fruits1')) # 아이디명으로 추출할 때는 #아이디명


# 아이디명으로 찾은 값에서 더 상세하게 추출하는 방법
# soup.select('#아이디명'>태그명.클래스명)
print(soup.select('#fruits1 > span.store'))
# >> 바나나 가게만 추출됨


# 속성값만 추출하고 싶어요
# soup.select('태그명[속성1=값1]')
# ex) img태그 + src속성 / a태그 + hrep속성
print(soup.select('a[href]')) # >> 모든 a[href] 값 출력
print(soup.select('a[href]')[0]) # >> 그 중 첫 번째 값만 추출