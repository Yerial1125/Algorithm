## 함수 선언부


## 전역 변수부
katok = ['다현','정연','쯔위','사나','지효']

## 메인 코드부
print(katok)

# 데이터 추가 : 모모에게 카톡 1회
katok.append(None) #빈칸추가
katok[5] = '모모'
print(katok)

# 데이터 삽입 : 미나를 3등으로 삽입
# 1단계 : 빈칸 추가
katok.append(None)
# 2단계 : 한칸씩 오른쪽으로 이동
katok[6] = katok[5]
katok[5] = None
katok[5] = katok[4]
katok[4] = None
katok[4] = katok[3]
katok[3] = None
# 3단계 : 데이터 삽입
katok[3] = '미나'
print(katok)

# 데이터 삭제 : 4등 사나를 제거
# 1단계
katok[4] = None
# 2단계 : 한칸식 왼쪽으로 이동
katok[4] = katok[5]
katok[5] = None
katok[5] = katok[6]
katok[6] = None
# 3단계 : 빈칸 삭제
del(katok[6])
print(katok)