# ------------------------------------------------------------------------
# 문자열 str 데이터 다루기
# - 문자열 원소/요소 변경 체크
# ------------------------------------------------------------------------
msg='pithon'

# [1] 원소/요소 값 변경 ==> 불가능
# msg[1]='y'


# [2] 원소/요소 값 삭제 ==> 명령어 del(), del : 불가능
# del(msg[1])
# del msg([1])

# 명령어 del(), del
# 변수 msg 삭제
del(msg)

# 삭제 후 변수 msg 접근 ERROR
print(msg)