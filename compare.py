
import random
import math
import matplotlib.pyplot as plt
from pathlib import Path

# 设置四组不同的随机点数量
point_counts = [100, 1000, 10000, 100000]

# 创建2行2列的图形
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 保存实验结果
results = []

# 依次进行四组实验
for ax, n in zip(axes.flat, point_counts):

    inside_x = []
    inside_y = []
    outside_x = []
    outside_y = []
    inside_count = 0

    # 生成随机点
    for i in range(n):
        x = random.random()
        y = random.random()

        # 判断是否在四分之一圆内部
        if x*x + y*y <= 1:
            inside_count += 1
            inside_x.append(x)
            inside_y.append(y)
        else:
            outside_x.append(x)
            outside_y.append(y)

    # 估算圆周率和绝对误差
    pi_estimate = 4 * inside_count / n
    error = abs(pi_estimate - math.pi)

    results.append((n, pi_estimate, error))

    # 绘制圆内、圆外随机点
    ax.scatter(inside_x, inside_y, s=2, c="blue")
    ax.scatter(outside_x, outside_y, s=2, c="red")

    # 绘制四分之一圆边界
    circle_x = [i / 1000 for i in range(1001)]
    circle_y = [
        math.sqrt(max(0, 1 - x*x))
        for x in circle_x
    ]

    ax.plot(circle_x, circle_y, color="black", linewidth=1.5)

    # 设置每张子图的标题
    ax.set_title(
        f"N={n}, Pi={pi_estimate:.5f}\nError={error:.5f}"
    )

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("equal")

# 调整图形间距
plt.tight_layout()

# 保存对比图
Path("images").mkdir(exist_ok=True)
plt.savefig("images/monte_carlo_comparison.png", dpi=200)

# 输出实验结果
print("===== 蒙特卡罗方法对比实验 =====")
print("随机点数量\t估算圆周率\t绝对误差")

for n, pi_estimate, error in results:
    print(f"{n}\t\t{pi_estimate:.6f}\t{error:.6f}")

print("\n对比图保存成功！")
print("文件名称：images/monte_carlo_comparison.png")

# 显示图形
plt.show()
