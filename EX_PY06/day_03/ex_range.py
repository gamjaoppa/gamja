# --------------------------------------------------------------------------
# 내장함수 range()
# - 숫자 범위를 생성하는 내장함수
# - 형식 : range(시작숫자, 끝숫자+1, 간격)
#         range(끝숫자+1)  
# --------------------------------------------------------------------------
# [실습1] 1~100 숫자를 저장하세요
nums=range(1,101)
print(f'nums 값 : {nums}\n타입 : {type(nums)}\n개수 : {len(nums)}')

#원소/요소 읽기 ===> 인덱싱
print(nums[0], nums[-1])

# 원소/요소 여러개 범위 읽기 ===> 슬라이싱
print(nums[:10], nums[30:41])

# 원소/요소 하나하나 보기 ===> list/tuple 형변환
print(list(nums[:10]), tuple(nums[30:41]))

# [실습2] 1~100 숫자 중 3의 배수만 저장하세요.
nums=range(3,101,3)
print(f'3의 배수 : {list(nums)}')

# 1.0 ~ 10.0 사이의 숫자 저장
datas=list(range(1,11))
datas=list(map(float, datas))
print(datas)