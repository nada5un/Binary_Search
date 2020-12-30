# 재귀 함수 사용 
def binary_search(arr,target,start,end):
  if start>end:
    return None
  mid = (start+end)//2
  if arr[mid]==target:
    return mid
  ##중간점의 값보다 타겟이 작은 경우 왼쪽 확인 
  elif arr[mid]>target:
    return binary_search(arr,target,start,mid-1)
  #중간점의 값보다 타겟이 큰 경우 오른쪽 확인 
  else:
    return binary_search(arr,target,mid+1,end)

def binary_search2(arr,target,start,end):
  while start <=end:
    mid = (start+end)//2
    if arr[mid] == target:
      return mid
    elif arr[mid]>target:
      end = mid-1
    else:
      start = mid+1
  return None

n, target = list(map(int,input().split()))
arr = list(map(int,input().split()))

result = binary_search(arr,target,0,n-1)
result2 = binary_search2(arr,target,0,n-1)

if result == None:
  print("원소가 존재 하지 않습니다")
else:
  print("재귀:",result+1)
  print("반복:",result2+1)