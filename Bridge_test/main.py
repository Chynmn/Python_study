def dfs(now, parent):           # dfs 함수
    global cnt                  # 노드 방문 순서 변수(전역)
    cnt += 1
    visited[now] = True         # 이미 방문한 노드를 구별하기 위한 변수
    order[now] = cnt            # 노드 방문 순서
    mos = order[now]            # 주변 최소 순번 변수

    for child in graph[now]:    # 현재 노드와 간선으로 연결된 child 노드 탐색
        if child == parent:     # parent 노드로 돌아가는 경우 제거
            continue

        if visited[child] == True:        # 이미 방문한 노드
            mos = min(mos, order[child])  # 주변 최소 순번을 최소값으로 초기화
            continue

        subtree = dfs(child, now)   # recursion 서브트리 dfs
        mos = min(subtree, mos)     # parent 노드와 주변 최소 순번을 비교해 최소값으로 초기화

        # 현재간선을 제외하고 subtree의 값이 parent 노드의 순번보다 크면 브리지이다.
        if subtree > order[now]:
            bridge.append([now, child])

    return mos

if __name__ == '__main__':
    V, E = map(int, input("정점의 개수와 간선의 개수를 입력해 주세요 : ").split())

    graph = [[]for _ in range(0, V+1)]  # 그래프 생성
    visited = [False] * (V+1)           # dfs를 위한 방문여부 확인 bool리스트
    order = [-1] * (V+1)                # 순회를 체크하기 위한 배열을 -1로 초기화

    # 인접 리스트 → 두 정점을 연결
    for i in range(0, E):
        A, B = map(int, input("간선의 양 끝 점을 입력해 주세요 : ").split())
        graph[A].append(B)
        graph[B].append(A)

    bridge = []     # 브릿지 array
    cnt = 0         
    dfs(1, None)    # 정점 1부터 시작

    # 브리지 판단할 때, 두 정점을 오름차순 정렬해서 판단 
    for i in range(0, len(bridge)):
        bridge[i].sort()

# 그래프 생성 후 실행
while (1):
    print("---------------- 브리지 테스트 ----------------\n")
    print("생성된 그래프에서 브리지를 확인 할 옵션의 번호를 입력하세요.\n")
    print("1. 전체 브리지 확인하기")
    print("2. 두 정점을 입력해 브리지 여부 판별하기")
    print("-1. 프로그램 종료 \n")

    option = int(input("옵션 번호를 입력하세요 : "))

    if option == 1:
        print("------------- 전체 브리지 확인 -------------\n")
        if len(bridge) == 0:
            print("이 그래프에서는 브리지가 존재하지 않습니다.\n")
        else:
            for v1, v2 in bridge:
                print("정점 %d 와 정점 %d 를 잇는 간선은 브리지입니다.\n" %(v1, v2))
    elif option == 2:
        # while (1):
            print("------------- 브리지 여부 판별 -------------\n")
            print("브리지 여부를 판별할 두 정점을 입력해주세요.")
            print("입력 예 : 1 2 ")
            v1, v2 = map(int, input("두 정점 입력 : ").split())
            edge = [v1, v2]
            edge.sort()

            if edge in bridge:
                print("정점 %d 와 정점 %d 를 잇는 간선은 브리지입니다.\n" %(v1, v2))
            else:
                print("정점 %d 와 정점 %d 를 잇는 간선은 브리지가 아닙니다.\n" %(v1, v2))

    elif option == -1:
        print("------------ 브리지 프로그램 종료 ------------\n")
        exit(1)
    else:
        print("잘못된 번호를 입력하셨습니다! 다시 입력해주세요.\n")
