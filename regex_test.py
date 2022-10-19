import re # 정규식을 사용할 수 있는 모듈

url = '<a href="https://blog.naver.com/abc1224"> 여행블로그</a>'

# 원하는 패턴이나 형태를 기호를 이용해 알려주는 방법
# 정규 표현식에서 사용되는 기호들. (.*?)
print(re.search('href="(.*?)">',url).group(1))
# >> https://blog.naver.com/abc1224

# 문법
# . 기호는 임의의 한 문자가 존재
# ? 바로 앞의 문자가 존재하거나 존재하지 않음
# * 바로 앞의 문자가 존재하지 않거나 무한대로 존대
# + 바로 앞의 문자가 한 번 이상 존재
# ^ 바로 뒤의 문자로 문자열이 시작
# $ 바로 앞의 문자로 문자열이 끝남
# {숫자} 숫자만큼 반복
# {숫자,} 숫자 이상만큼 반복
# {숫자1,숫자2} 숫자 1 이상, 숫자 2이하만큼 반복
# (문자열) 문자나 문자열을 묶음
# [문자1,문자2...] 대괄호 안에 있는 문자들이 존재하는지 검색
# [^] '^' 기호 바로 뒤에 문자가 존재하지 않음
# [:alpha:] 알파벳과 모든 글자 포함
# [:alnum:] 알파벳, 숫자만 검색
# \\(역슬래쉬) 글자 자체를 검색

# 정규식에서 search(), match() 함수 많이 사용함

# search()와 match()함수의 차이점
# search()는 지정한 패턴 중 일부만 일치해도 찾음
# match()는 지정한 패턴과 정확히 일치해야 찾음

# search 함수
re.search("[pP]","apPie") # 소문자 p나 대문자 P가 있으면 찾아라
# >> <re.Match object; span=(1, 2), match='p'>

# match 함수
re.match("[pP]","pP")
# >> <re.Match object; span=(0, 1), match='p'>


# . 기호
s_txt = re.compile("a.c") # re.compile은 어떤 패턴을 찾겠다 선언한 것
s_txt.search("aaa")
# >> 결과 x (.이라는 기호는 엑셀에서 ?과 같음)
s_txt.search("azc")
# >> <re.Match object; span=(0, 3), match='abc'>
s_txt.search("abdfac")
# >> 결과 x
s_txt.search("ac")
# >> 결과 x


# ? 기호
s_txt = re.compile("py?n") # 찾고 싶은 패턴 지정
s_txt.search("pyn") # ? 앞에 있는 y문자가 1회 나오고 ?뒤의 n 문자가 나옴
# >> <re.Match object; span=(0, 3), match='pyn'>
s_txt.search("pyyn") # ? 앞에 있는 y 문자가 2번 있고 ? 뒤의 n 문자 있음
# >> 결과 x
s_txt.search("pn") # ? 앞에 있는 y 문자가 없고 ? 뒤의 n 문자는 있음
# >> <re.Match object; span=(0, 2), match='pn'>
s_txt.search("pin")
# >> 결과 x


# * 기호
s_txt = re.compile("py*n") # 찾고 싶은 패턴 지정
s_txt.search("pyn") # * 앞에 있는 y 문자가 1회 나오고 * 뒤의 n문자 나옴
# >> <re.Match object; span=(0, 3), match='pyn'>
s_txt.search("pyyn") # * 앞에 있는 y 문자가 2번 나오고 * 뒤의 n문자 나옴
# >> <re.Match object; span=(0, 4), match='pyyn'>
s_txt.search("pn") # * 앞에 있는 y 문자가 없고 * 뒤의 n 문자 나옴
# >> <re.Match object; span=(0, 2), match='pn'>
s_txt.search("pin") # * 앞에 있는 y 문자 대신 i 문자 나오고 * 뒤의 n 문자 나옴
# >> 결과 x