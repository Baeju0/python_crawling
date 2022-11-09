no1 = int(input("숫자만 입력: "))
# 숫자만 입력: 2
# no1
# >>2


no1 = int(input("숫자만"))
# 숫자만
# 숫자가 아닌 A 입력 → 오류

# 예외처리
try :
	no1 = int(input("숫자만: "))
except ValueError :
	print("숫자만 입력하세요!")
# >> 숫자만: dd
# 숫자만 입력하세요!

	
no1 = 10
no2 = 0
print(no1 / no2)
# 오류 발생! 0으로 나눌 수 없으니 예외처리
try :
	print(no1/no2)
except ZeroDivisionError :
	print("0으로 나눌 수 없습니다")


# 예외처리, 또는 결괏값 출력
try :
	no1 =int(input("숫자만 입력: "))
except ValueError :
	print("숫자가 아닙니다")
else :
	print(no1 * 3)
# >> 숫자만 입력: 3
# >> 9


# 두 가지 예외처리
try :
	print(no1/no2)
except ValueError :
	print("숫자를 입력하세요!")
except ZeroDivisionError :
	print("0으로 나눌 수 없습니다")
	

# finally, 예외처리 상관없이 무조건 출력
try :
	no1 = int(input("숫자만 입력: "))
except ValueError :
	print("숫자가 아닙니다")
else :
	print(no1*1)
finally :
	print("무조건 실행되는 문장")

	
# >> 숫자만 입력: 4
# >> 4
# >> 무조건 실행되는 문장