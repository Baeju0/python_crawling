# beautifulSoup_test.py에서 사용한 텍스트 추출하기 위한 방법 2가지
# get_text()메소드와 string의 차이

from bs4 import BeautifulSoup
html = """
<html>
    <head>
        <title>get_string</title>
    </head>
    <body>
        <div class="item_num">
            <div class="a-num">
                <span>1</span>
            </div>
            <div class="b-num">
                <strong><span>2</span></strong>
            </div>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html,'html.parser')
# >> 그냥 BeautifulSoup(html)만 입력할 시 오류가 발생한다
# >> 'html.parser'를 추가해주면 오류 해결!

# get_text() 메소드
# 선택하고자 하는 텍스트를 추출
# 현재 태그 입력하면, 이 태그를 포함한 모든 하위 태그를 제거한 후 남은 텍스트만 추출
# ex)
print(soup.select_one('.item_num').get_text())
# >> 1 2 출력

# 나는 2만 출력하고 싶어요!
print(soup.select_one('.item_num > .b-num').get_text())
# >> 2 출력
# 이처럼 정확한 문자열을 추출하고 싶으면 항상 마지막 태그에 메서드를 사용해야 된다!

# -------------------------------------------------------------------------------------------

# string속성은 더 명확하게 추출해낼 수 있다
# ex)
print(soup.select_one('.b-num > strong > span').string)
# >> 2 출력
# 위는 태그 내에 있는 문자열을 반환한다

# 태그에 있는 자식 태그가 둘 이상일 때는 반환할 내용이 명확하지 않기 때문에 None 반환
print(soup.select_one('.b-num').string)
# >> None 

# 자식 태그가 하나이면서, 그 자식 태그가 string 값을 가지고 있다면 자식 태그 문자열 반환
print(soup.select_one('.b-num > strong').string)
# >> 2 출력