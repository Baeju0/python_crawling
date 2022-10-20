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


# ? 기호 (한 번만 존재하는 것을 뽑고 싶다!)
s_txt = re.compile("py?n") # 찾고 싶은 패턴 지정
s_txt.search("pyn") # ? 앞에 있는 y문자가 1회 나오고 ?뒤의 n 문자가 나옴
# >> <re.Match object; span=(0, 3), match='pyn'>
s_txt.search("pyyn") # ? 앞에 있는 y 문자가 2번 있고 ? 뒤의 n 문자 있음
# >> 결과 x
s_txt.search("pn") # ? 앞에 있는 y 문자가 없고 ? 뒤의 n 문자는 있음
# >> <re.Match object; span=(0, 2), match='pn'>
s_txt.search("pin")
# >> 결과 x


# * 기호 (여러 번 존재하는 것을 뽑고 싶다!)
s_txt = re.compile("py*n") # 찾고 싶은 패턴 지정
s_txt.search("pyn") # * 앞에 있는 y 문자가 1회 나오고 * 뒤의 n문자 나옴
# >> <re.Match object; span=(0, 3), match='pyn'>
s_txt.search("pyyn") # * 앞에 있는 y 문자가 2번 나오고 * 뒤의 n문자 나옴
# >> <re.Match object; span=(0, 4), match='pyyn'>
s_txt.search("pn") # * 앞에 있는 y 문자가 없고 * 뒤의 n 문자 나옴
# >> <re.Match object; span=(0, 2), match='pn'>
s_txt.search("pin") # * 앞에 있는 y 문자 대신 i 문자 나오고 * 뒤의 n 문자 나옴
# >> 결과 x


# + 기호
s_txt = re.compile("py+n")
s_txt.search("pyn") # + 앞에 있는 y문자가 1회 나오고 + 뒤의 n문자 나옴
# >> <re.Match object; span=(0, 3), match='pyn'>
s_txt.search("pyyn") # + 앞에 있는 y문자가 2회 나오고 + 뒤의 n문자 나옴
# >> <re.Match object; span=(0, 4), match='pyyn'>
s_txt.search("pn") # + 앞에 있는 y 문자가 없고 + 뒤의 n 문자 나옴
# >> 결과 x 
s_txt.search("pin") # + 앞에 있는 y 문자 대신 i가 있으며 + 뒤에는 n 문자 나옴
# >> 결과 x


# ^ 기호 (시작되는 글자를 지정 가능!)
s_txt = re.compile("^p") # 소문자 p로 시작되는 단어나 문장 추출해라!
s_txt.search("python")
# >> <re.Match object; span=(0, 1), match='p'>
s_txt.search("sython")
# >> 결과 x


# $ 기호 (끝나는 글자를 지정 가능!)
s_txt = re.compile("n$") # 소문자 n으로 끝나는 단어나 문장 추출해라!
s_txt.search("python")
# >> <re.Match object; span=(5, 6), match='n'>
s_txt.search("apple")
# >> 결과 x


# [문자1, 문자2...] 기호 (해당 글자나 숫자가 포함이 되면 다 출력 가능!)
s_txt = re.compile("[pa]") # pa이라는 단어를 찾아라!가 아님! p나 a가 들어가 있는 것 다 추출해라!
s_txt.search("python")
# >> <re.Match object; span=(0, 1), match='p'>
s_txt.search("pineapple")
# >> <re.Match object; span=(0, 1), match='p'>
s_txt.search("banana")
# >> <re.Match object; span=(1, 2), match='a'>
s_txt.search("mouse")
# >> 결과 x


# [^문자1,문자2...] 기호 (^기호 뒤 문자를 제외한 모든 글자 출력!)
s_txt = re.compile("[^pa]") # 소문자 p나 소문자 a를 제외한 나머지 글자를 출력해라!
s_txt.search("python") # 소문자 p는 제외를 함! 근데 그뒤에 값 y가 나오는데 소문자 p나 a가 아닌 글자라서 결과가 나옴
# >> <re.Match object; span=(1, 2), match='y'>
s_txt.search("p")
# >> 결과 x 
s_txt.search("pineapple") # 소문자 p나 소문자 a는 안 되는데 다른 값 때문에 출력
# >> <re.Match object; span=(1, 2), match='i'>
s_txt.search("a")
# >> 결과 x


# [] 범위 검색
s_txt = re.compile("[0-9]") # 0~9까지의 숫자 포함 단어,문장 찾기
s_txt.search("abc123")
# >> <re.Match object; span=(3, 4), match='1'>

s_txt = re.compile("[a-d]") # a~d까지의 소문자 포함 단어,문장 찾기
s_txt.search("abc123")
# >> <re.Match object; span=(0, 1), match='a'>

s_txt = re.compile("[A-D]") # A~D까지의 대문자 포함 단어,문장 찾기
s_txt.search("abc123")
# >> 결과 x

s_txt = re.compile("[가-사]") # 가~사까지의 한글 포함 단어,문장 찾기
s_txt.search("강원도")
# >> <re.Match object; span=(0, 1), match='강'>


# meta character
# \t와 \n
# \t는 tab 기능
# \n은 줄바꿈 기능
# 근데 \t나 \n을 그대로 출력하고 싶어
# ↓

# escape character
# meta character의 기능을 취소하는 것


# findall() 함수 (포함되는 것 다 출력)
s_txt = "제 생일은 2000년 1월 5일 입니다"
re.findall("\d",s_txt) # 숫자 골라내기, 근데 한 글자씩?
# >> ['2', '0', '0', '0', '1', '5']

re.findall("\d+",s_txt) # 숫자 패턴에 맞는 것 전부 다 골라내기
# >> ['2000', '1', '5']


# split() 함수 (주어진 문자열을 기준으로 분리함)
s_txt = "https://blog.naver.com/abc1234"
re.split("/",s_txt) # / 을 기준으로 분리
# >> ['https:', '', 'blog.naver.com', 'abc1234']

re.split("//",s_txt) # // 을 기준으로 분리
# >> ['https:', 'blog.naver.com/abc1234']


# sub() (주어진 패턴과 일치하는 문자를 변경, 필요없는 문자열 제거할 때 사용)
s_txt = "https://blog.naver.com/abc1234"
re.sub("https://"," ", s_txt) # https://이 나오면 " "(공백)으로 바꿔라!
# >> ' blog.naver.com/abc1234'