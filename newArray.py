import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([10, 20])
#크기가 다른 행렬 두가지를 계산할 수 있게 해주는 기능 -> 브로드캐스트
#행렬의 크기를 확장해서 계산할 수 있게 해줌
print(a * b)

print(a[0])
print(a[0][1])
#flatten()을 사용하면 2*2 행렬을 평탄화 해서 1차원 배열로 바꿔줌
a = a.flatten()
print(a)
#인덱스가 0, 2 인 부분을 출력
print(a[np.array([0, 2])])
