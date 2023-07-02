# -*- coding: utf-8 -*-


# =============================================================================
# 파이썬의 대표적인 데이터 컨테이너 자료형
# 
# 정수나 실수 등을 갖는 변수는 그 값이 하나이므로 많은 데이터 처리가 힘듬
# 
# 여러 값을 요소로 가져 하나의 변수에 많은 데이터를 담을 수 있음
# 
# 특징
# 대괄호 [] 안에 콤마로 구분해 요소 나열
# 어떠한 자료형도 요소로서 포함이 가능하고 중복될 수도 있음
# 요소가 순서를 가지므로 특정 위치의 요소나 범위의 요소 확인 가능
# 
# =============================================================================

lst = [60,30,"20"] # 숫자와 문자를 함께 넣을 수 있다.

score = [85, 90, 80, 75, 95]

max(score)
min(score)
sum(score)


# 연속된 규칙을 갖는 리스트를 만드는 함수 range()
# range(시작, 끝, 스텝)
# range(n): 0부터 n-1 까지 1씩 증가하는 정수 범위
# range(m, n): m부터 n-1 까지 1씩 증가하는 정수 범위
# range(m, n, x): m부터 n-1 까지 x 만큼씩 증가하는 정수 범위
# range 함수는 나중에 배울 for loop에서 주로 사용된다.
list(range(10))
list(range(0,10))
list(range(0,10,1))



# =============================================================================
# 리스트 인덱싱
# 리스트 안에서 특정 값을 찾을 때 사용하는 데이터를 인덱스 (Index) 라고 하며
# 인덱스로 특정 요소를 찾는 과정을 인덱싱 (Indexing) 이라고 함
# 대괄호 안에 인덱스를 지정함
# 파이썬의 정수는 0부터 시작, 0부터 시작하는 정수형 위치 인덱스를 사용
# 리스트의 크기를 벗어나는 인덱스는 에러 유발
# 인덱스의 역방향은 -1 부터
# 
# =============================================================================

# 시작은 항상 0부터
score = [85, 90, 80, 75, 95]
score[0]
score[1]
score[2]
score[3]
score[4]
score[-1]
score[-5]

# list[n:m]으로 리스트 전체중 일부만 추출할 수 있으며 n번째 포함~ m번째 미포함 이다.
score[1:2]
score[1:3]


# 시작하는 n을 생락가능하며 0번째부터 m 번째 미포함 까지
score[:3]

# 끝나는 m도 생략 가능하다. 2번째부터 끝까지
score[2:]

# 리스트 뒤에 추가하는 함수 .append()
score.append(100)
print(score)

# 리스트 안에 있는 요소를 지우는 함수 del
del score[5]
print(score)

# 리스트 내용을 범위로 지우는 방법 
score[2:] = []
print(score)


score = [85, 90, 80, 75, 95]
# append함수와 비슷하지만, append 함수는 리스트에 리스트 자체로 추가가 되는 반면
# extend 함수는 리스트를 추가해도 리스트가 풀리고 요소만 추가 된다.
score.append([100,100])
print(score) # 리스트 안에는 숫자, 문자, 리스트 등 모든것이 들어 갈 수 있기 때문에 리스트도 리스트로 들어간다
score.extend([99,99])
print(score)








# 과제
# 리스트를 다음과 같이 선언한 후에 lst1 = [1,2,3,4,5,6,7,8,9,10]
# lst2 = [6, 7, 8, 9, 10, 1, 2, 3, 4, 5] 의 결과가 나오도록 한줄 코딩을 해본다.
lst1 = [1,2,3,4,5,6,7,8,9,10]










#답안지






lst2 = lst1[5:] + lst1[:5]
