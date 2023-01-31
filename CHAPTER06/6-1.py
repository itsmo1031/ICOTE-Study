# 위에서 아래로

""" Input Example
3
15
27
12
"""

# 입력 받을 배열 선언
arr = []

# 입력받은 N개의 수만크 배열에 입력
for __ in range(int(input())):
    arr.append(int(input()))

# 출력
print(*sorted(arr, reverse=True))

""" Output Example
27 15 12
"""
