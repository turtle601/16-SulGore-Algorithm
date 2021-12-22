import sys
input = sys.stdin.readline

N, M = map(int, input().split())
NUMS = sorted(list(map(int, input().split())))

def backtrack(seq, lastIndex):
  global N, M, NUMS
  if len(seq) == M:
    return print(' '.join(map(str, seq)))
  
  for i in range(lastIndex, N):
    backtrack(seq + [NUMS[i]], i)

backtrack([], 0)