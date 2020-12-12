
# # # 구현 - p322 문자열 재정렬
# # 강의 코드
# str_input = input()
# apb_list = []
# value = 0
#
# # str_input을 하나씩 검사한다.
# for i in str_input:
#     # 알파벳인 경우를 그 값을 리턴하는 isalpha()
#     if i.isalpha():
#         apb_list.append(i)
#     else:
#         value += int(i)
# apb_list.sort()
#
# # value가 0이 아닐 때만 apb_list에 append 한다.
# if value != 0:
#     apb_list.append(str(value))
# # list를 문자열로 변환하여 출력하는 join, 앞의 ''는 빈 칸 없이 출력
# print(''.join(apb_list))
#
# # 나의 코드 ===========================================================================
# str_input = input()
#
# number = 0
# apb_list = []
# # 사실상 없어도 되는 코드. 최대한 short coding.
# # for num in str_input:
# #     if '0' <= num <= '9':
# #         number += int(num)
# for x in str_input:
#     if 'A' <= x <= 'Z':
#         apb_list.append(x)
#     else:
#         number += int(x)
#
# apb_list.sort()
#
# # 이걸 빼뜨렸었다. 0이 아닐 때만 append 하자.
# if number != 0:
#     apb_list.append(str(number))
#
# print(''.join(apb_list))
















# # 그리디 알고리즘 - p311 모험가 길드
# n = int(input())
# x = list(map(int, input().split()))
# g_member_count = 0  # 현재 그룹의 그룹원의 수
# g_count = 0  # 그룹의 수
#
# if len(x) > n:
#     print("x는 n보다 클 수 없습니다. n의 범위까지 Slice 처리 합니다.")
#     x = x[0:n]
#     x.sort()
#
# for i in x:  # x로 입력받은 데이터를 하나씩 x에 읽힌다
#     g_member_count += 1  # 그룹원의 수를 1 증가시킴
#     if g_member_count >= i:  # 현재 그룹의 그룹원의 수가 공포도가 크거나 같으면
#         g_count += 1  # 그룹을 추가시킨다.
#         g_member_count = 0  # 현재 그룹의 그룹원 수를 초기화시켜 새로운 그룹
#
# print(g_count)


















# import sys
# import heapq

# input = sys.stdin.readline

# def heapsort(iterable):
#   h = []
#   result = []

#   for value in iterable:
#     heapq.heappush(h, -value)
#   print("h는 >> ", h)
#   for i in range(len(h)):
#     result.append(heapq.heappop(h)*(-1))
#     print("h pop >> ", h)
#   return result

# n = int(input())
# arr = []

# for i in range(n):
#   arr.append(int(input()))

# res = heapsort(arr)

# for i in range(n):
#   print(res[i])




















# # 구현 실전 문제 - 왕실의 나이트 P115
# pos = input()
# row = int(pos[1])
# col = int(ord(pos[0]) - ord('a') + 1)
# count = 0

# # 나이트가 움직일 수 있는 경우 셋
# move_set = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

# for move in move_set:
#   nrow = row + move[0]
#   ncol = col + move[1]
#   if nrow >= 1 and nrow <=8 and ncol >= 1 and ncol <= 8:
#     count += 1

# print(count)




















# # 구현 예제 4-1 상하좌우 이동 P110
# # 맵 크기를 나타내는 n 입력
# n = int(input())
# # 이동 방향을 입력받는 move
# movings = input().split()

# x, y = [1, 1]

# # Left, Right, Up, Down
# dx = [0, 0, 1, -1]
# dy = [-1, 1, 0, 0]
# moving_set = ['L', 'R', 'D', 'U']

# for moving in movings:
#   for i in range(len(moving_set)):
#     if moving == moving_set[i]:
#       nx = x + dx[i]
#       ny = y + dy[i]

#   if nx < 1 or ny < 1 or nx > n or ny > n:
#     continue

#   x, y = nx, ny
# print(x, y)


















# # 구현 - 예제 4-2 시각 P113
# # str에서 문자의 존재 여부를 검사할 때는 in으로 한다.
# # int 등 값을 비교할 때는 ==를 사용
# # 밑의 경우는 시 분 초를 다 더한 000000에서 nn5959까지 다 검사.
# n = int(input())
# count = 0

# for h in range(n + 1):
#   for m in range(60):
#     for s in range(60):
#       if '3' in str(h) + str(m) + str(s):
#         count += 1

# print(count)


















# # 그리디 알고리즘 - 곱하기 혹은 더하기로 제일 큰 수 만들기
# # 조건 1 <= S의 길이 <= 20

# # 방법 1 - 내가 한 것 ==========================================================================================
# number_list = list(map(int, str(s)))
# value = 1

# if 1 <= len(s) and len(s) <= 20:
#   for i in number_list:
#     if i == 0:
#       value += i
#     elif i > 0:
#       value *= i
#   print(value)
# else :
#   print("S의 길이는 1이상 20 이하입니다.")


# # 방법 2 - 강의 코드
# s = input()

# value = 1

# for i in range(len(s)):
#   if int(s[i]) == 0:
#     value += int(s[i])
#   else:
#     value *= int(s[i])
# print(value)




















# # 그리디 알고리즘 - 1이 될 때까지의
# # 방법 1 - 강의 코드
# import time
# n, k = map(int, input().split())
# count = 0
# startTime = time.time()
#
# while n >= k:
#   while n % k != 0:
#     n = n - 1
#     count += 1
#   n = n // k
#   count += 1
#
# while n >= 2:
#   n = n - 1
#   count += 1
# endTime = time.time()
#
# print(endTime - startTime)
# print(n, k, count)
#
# # 방법 2 - 내가 한 것==========================================================================================
# import time
# n, k = map(int, input().split())
# count = 0
#
# startTime = time.time()
#
# while 1:
#   if n >= k:
#     if n % k == 0:
#       n //= k
#       count += 1
#     elif n % k != 0:
#       n -= 1
#       count += 1
#
#   if n == 1:
#     break
#
# endTime = time.time()
# print("실행 시간", endTime - startTime)
# print(n, k, count)


















# # 그리디 알고리즘 - 동전 개수 구하기
# money = eval(input())
# count = 0

# coins = [500, 100, 50, 10]

# for coin in coins:
#   count += money // coin
#   money %= coin

# print(count)
