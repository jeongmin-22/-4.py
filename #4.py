# 첫번째 직사각형의 좌표 입력
xl1, yl1 = map(int, input("첫번째 직사각형의 왼쪽 상단 모서리 좌표 (x, y): ").split())
xr1, yr1 = map(int, input("첫번째 직사각형의 오른쪽 하단 모서리 좌표 (x, y): ").split())

# 두번째 직사각형의 좌표 입력
xl2, yl2 = map(int, input("두번째 직사각형의 왼쪽 상단 모서리 좌표 (x, y): ").split())
xr2, yr2 = map(int, input("두번째 직사각형의 오른쪽 하단 모서리 좌표 (x, y): ").split())

# 겹치는 영역 구하기
dx = min(xr1, xr2) - max(xl1, xl2)
dy = min(yr1, yr2) - max(yl1, yl2)

if dx < 0 or dy < 0:  # 겹치는 영역이 없는 경우
    overlap_area = 0
else:
    overlap_area = dx * dy

print("두 직사각형이 겹치는 영역의 넓이는 {}입니다.".format(overlap_area))
