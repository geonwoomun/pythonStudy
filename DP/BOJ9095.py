# BOJ 9095 1,2,3 더하기
# dp는 역시 점화식을 잘 만들어야한다...
# 예제를 보면 4일 때 7이고 7일 때 44인걸 알 수 있는데 5, 6을 구해보면
# 7은 4 5 6 을 더한 값이라는 것을 알 수 있고, 1,2,3을 더하면 4인 것을 알 수 있다.
import sys

t = int(sys.stdin.readline());

dp = [0 for i in range(11)]
dp[0] = 0; # 0은 1,2,3으로 못만드니깐 0
dp[1] = 1; # 1은 1으로 만들 수 있다.
dp[2] = 2; # 2는 1+1, 2 2개로 만들 수 있다.
dp[3] = 4; # 3은 1+1+1, 1+2, 2+1, 3 으로 만들수있다 3

for i in range(4,11): # 4부터 10까지 한다. n이 양수이며 11보다 작다고 했기 때문에
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3] # i는 i-1, i-2, i-3을 더한것과 같다.

for i in range(t):
    n = int(sys.stdin.readline())
    print(dp[n])