import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")  # GUI를 사용하지 않음

# distance 값을 설정
distance = 10  # 원하는 거리 값을 입력하세요

# theta 값을 설정 (0부터 360도까지)
theta = np.linspace(0, 2 * np.pi, 360)  # 라디안 값으로 설정

# x와 y 값 계산
x = distance * np.cos(theta)
y = distance * np.sin(theta)

# 그래프에 점 찍기
plt.figure(figsize=(8, 8))

# 4분면 배경 추가
plt.axhline(0, color='black', linewidth=1)  # X축
plt.axvline(0, color='black', linewidth=1)  # Y축

# 4분면 라벨 추가
plt.text(distance / 2, distance / 2, "1사분면", fontsize=12, color='red')
plt.text(-distance / 2, distance / 2, "2사분면", fontsize=12, color='green')
plt.text(-distance / 2, -distance / 2, "3사분면", fontsize=12, color='blue')
plt.text(distance / 2, -distance / 2, "4사분면", fontsize=12, color='purple')

# 점 플로팅
plt.scatter(x, y, c='blue', s=10, label=f'Distance = {distance}')
plt.grid(color='lightgray', linestyle='--', linewidth=0.5)

# 그래프 설정
plt.legend()
plt.title("2D Point Plot with 4 Quadrants")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.axis('equal')  # X, Y 축 비율 동일하게
plt.xlim(-distance - 5, distance + 5)  # 약간 여유 공간 추가
plt.ylim(-distance - 5, distance + 5)

# 그래프 저장
plt.savefig("output.png")
print("Graph saved as output.png")
