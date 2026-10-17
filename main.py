
import random
import math
from pathlib import Path
import matplotlib.pyplot as plt

# 设置随机点数量
n = 10000

# 记录落在圆内的点数
inside_count = 0

# 保存圆内和圆外的随机点
inside_x = []
inside_y = []
outside_x = []
outside_y = []

# 随机生成10000个点
for i in range(n):
    x = random.random()
    y = random.random()

    # 判断是否在四分之一圆内部
    if x * x + y * y <= 1:
        inside_count += 1
        inside_x.append(x)
        inside_y.append(y)
    else:
        outside_x.append(x)
        outside_y.append(y)

# 计算圆周率的估算值
pi_estimate = 4 * inside_count / n

# 计算绝对误差
error = abs(pi_estimate - math.pi)

print("===== 蒙特卡罗方法估算圆周率 =====")
print("随机点总数：", n)
print("落在圆内的点数：", inside_count)
print("估算圆周率：", pi_estimate)
print("实际圆周率：", math.pi)
print("绝对误差：", error)

# 开始绘制图形
plt.figure(figsize=(7, 7))

# 蓝色表示圆内的点
plt.scatter(inside_x, inside_y, s=2, c="blue",
            label="Inside Circle")

# 红色表示圆外的点
plt.scatter(outside_x, outside_y, s=2, c="red",
            label="Outside Circle")

# 绘制四分之一圆的边界
circle_x = [i / 1000 for i in range(1001)]
circle_y = [math.sqrt(max(0, 1 - x*x)) for x in circle_x]

plt.plot(circle_x, circle_y, c="black", linewidth=2)

# 图形设置
plt.title(f"Monte Carlo Pi Estimation = {pi_estimate:.6f}")
plt.xlabel("X")
plt.ylabel("Y")
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.axis("equal")
plt.legend()

# 创建 images 文件夹并保存图片
Path("images").mkdir(exist_ok=True)
plt.savefig("images/monte_carlo.png", dpi=300)

print("随机撒点图已保存：images/monte_carlo.png")

# 显示图形
plt.show()
