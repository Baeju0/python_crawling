def plus(a,b) :
	return(a+b) # def 사용자 지정함수는 return으로 받기

plus(2,3)
# >> 5

def plus(a,b) :
	print(a+b) # print으로 출력할 수도 있지만 return으로 받는 것을 추천

plus(2,3)
# >> 5


# 인수를 얼마나 입력받을지 모를 때
def plus(*no) :
	total = 0
	for i in no :
		total += i
	return total

# 입력받는 수 다 더해주기
plus(4,5,6)
# >> 15
plus(1,2,4,5,6)
# >> 18


# 입력 받은 수 차례대로 출력하기
def pr_num(*no) :
	for i in no :
		print(i)
		
pr_num(4,5,6,7,8)
# >>
# 4
# 5
# 6
# 7
# 8


# 첫번째 인수 c가 0일 때, no1+no2 실행
# 첫번째 인수 c가 1일 때, no1-no2 실행
def calculator(c, no1, no2) :
	if c == 0 :
		return(no1 + no2)
	elif c == 1 :
		return(no1 - no2)
	
calculator(1,6,3)
# >> 3
calculator(0,6,3)
# >> 9


# 클래스
class bread :
	m = "단팥"

# bread()라는 클래스를 복사해서 bread_1이라는 클래스를 복사한 인스턴스를 생성
bread_1 = bread()
bread_1.m
# >> '단팥'

bread_2 = bread()
bread_2.m
# >> '단팥'

# '단팥 말고 치즈로 바꾸고 싶어!'
bread_2.m = "치즈"
bread_2.m
# >> '치즈'


# module
import module1
module1.hello()
# >> 모듈 함수에옹

# 파이썬이 알고 있는 경로 외의 모듈 불러오기
import sys
sys.path

# ↓ 파이썬이 알고 있는 모듈 경로
# >> ['', 'C:\\Python\\Lib\\idlelib', 'C:\\Python\\python39.zip', 'C:\\Python\\DLLs', 'C:\\Python\\lib', 'C:\\Python', 'C:\\Python\\lib\\site-packages']
sys.path.append("c:\\test") # module2의 경로 추가

import module2

module2.hello()
# >> 다른 폴더에 모듈 저장하기!!


# module3으로 다시 저장하기, module2에 있는 4개의 함수 중에서 sleep과 end함수만 불러오기
# from module3 import sleep, end
# >> 에러!
# 찾아보니 module2.sleep() 모듈이름.모듈함수 처럼 쓰지 않고 함수 이름으로만 사용하고 싶을 때 사용하는 듯?
# 아래와 같이 입력함
from module2 import sleep,end
# 이렇게 입력하면 module2의 sleep함수와 end함수만 사용이 가능해진다!
sleep()
# >> '졸려옹'
end()
# >> '언제 쉬어옹'