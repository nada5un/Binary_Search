#집합 자료형 이용 -> set

n = int(input())
arr1 = set(map(int,input().split()))

m = int(input())
arr2 = list(map(int,input().split()))

for i in arr2:
  if i in arr1:
    print("yes",end= ' ')
  else :
    print("no",end =' ')