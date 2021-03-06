T = int(input())
for tc in range(T):
    n = int(input())
    scores = [list(map(int, input().split())) for _ in range(2)]
    D = [[0]*3 for _ in range(n+1)]
    D[1] = [scores[0][0], scores[1][0], 0] # OX, XO, XX를 기준으로 구분. 왼쪽 것만 붙였을 때, 오른쪽 것만 붙였을 때, 안붙였을 때의 점수를 기록
    for i in range(2, n+1):
        OX, XO, XX = D[i-1]
        OX_now, XO_now, XX_now = scores[0][i-1], scores[1][i-1], 0
        D[i] = [max(XO,XX)+OX_now, max(OX, XX)+XO_now, max(OX, XO)+XX_now]
    print(max(D[n]))