# SWEA 14037
def 깊이우선탐색(행위치, 게시):
    global 정답
    if 행위치 == 크기:
        정답 += 1
        return
    for 열 in range(크기):
        if 게시[행위치][열] == 0:
            임시 = []
            for 행이동, 열이동 in [[1,1],[1,-1],[-1,1],[-1,-1],[1,0],[-1,0],[0,1],[0,-1]]:
                for 이동거리 in range(크기):
                    행확인, 열확인 = 행위치 + 이동거리 * 행이동, 열 + 이동거리 * 열이동
                    if 행확인 in range(크기) and 열확인 in range(크기):
                        if 게시[행확인][열확인] == 0:
                            게시[행확인][열확인] = 1
                            임시.append([행확인,열확인])
                    else:
                        break
            깊이우선탐색(행위치+1, 게시)
            for 행, 열 in 임시:
                게시[행][열] = 0
사례수 = int(input())
for 사례 in range(1, 사례수+1):
    크기 = int(input())
    게시 = [[0]*크기 for _ in range(크기)]
    정답 = 0
    깊이우선탐색(0, 게시)
    print(f'#{사례} {정답}')