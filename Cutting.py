n,m =list(map(int,input().split()))
arr = list(map(int,input().split()))
arr.sort()

start = 0
end = max(arr)

result = 0
while(start<=end):
  total = 0 
  # mid -> 자를 길이 
  mid = (start+end)//2
  for x in arr:
    if x>mid:
      total += x-mid
  # 더 잘라야 함 -> 끝 점 감소 : mid 감소 
  if total < m:
    end = mid - 1
  # 덜 잘라야 하는 경우 -> 시작 점 증가 : mid 증가 
  else:
    result = mid
    start = mid + 1
    
print(result)
