# SWEA 5648

읽다 = print
사례수 = int(input())
for 사례 in range(1, 사례수 + 1):
    원자들수 = int(input())
    에너지총합 = 0
    위치사전 = {}
    for _ in range(원자들수):
        가로, 세로, 이동방향, 보유에너지 = map(int, input().split())
        위치사전[(가로, 세로)] = [[이동방향, 보유에너지]]
    for _ in range(4002):
        충돌한곳들 = []
        if len(위치사전) <= 1:
            break
        임시위치사전 = {}
        for (현재가로, 현재세로) in 위치사전:
            현재이동방향, 현재보유에너지 = 위치사전[(현재가로, 현재세로)][0]
            if 현재이동방향 == 0:
                가로이동, 세로이동 = 0, 0.5
            elif 현재이동방향 == 1:
                가로이동, 세로이동 = 0, -0.5
            elif 현재이동방향 == 2:
                가로이동, 세로이동 = -0.5, 0
            else:
                가로이동, 세로이동 = 0.5, 0
            현재가로, 현재세로 = 현재가로 + 가로이동, 현재세로 + 세로이동
            if -1000 > 현재가로 or 현재가로 > 1000 or -1000 > 현재세로 or 현재세로 > 1000:
                continue
            if (현재가로, 현재세로) in 임시위치사전:
                임시위치사전[(현재가로, 현재세로)] += [[현재이동방향, 현재보유에너지]]
                if (현재가로, 현재세로) not in 충돌한곳들:
                    충돌한곳들.append((현재가로, 현재세로))
            else:
                임시위치사전[(현재가로, 현재세로)] = [[현재이동방향, 현재보유에너지]]

        for 충돌한곳 in 충돌한곳들:
            for _, 보유에너지 in 임시위치사전[충돌한곳]:
                에너지총합 += 보유에너지
            del 임시위치사전[충돌한곳]
        위치사전 = 임시위치사전
    읽다(f'#{사례} {에너지총합}')