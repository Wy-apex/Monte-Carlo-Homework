
import random
import math

# 设置随机点的数量
n = 10000

# 记录落在四分之一圆内的点数
inside_count = 0

# 循环生成随机点
for i in range(n):
    x = random.random()
    y = random.random()

    # 判断随机点是否落在圆内
    if x * x + y * y <= 1:
        inside_count += 1

# 使用蒙特卡罗方法估算圆周率
pi_estimate = 4 * inside_count / n

# 计算与真实圆周率的绝对误差
error = abs(pi_estimate - math.pi)

# 输出计算结果
print("===== 蒙特卡罗方法估算圆周率 =====")
print("随机点总数：", n)
print("落在圆内的点数：", inside_count)
print("估算的圆周率：", pi_estimate)
print("实际圆周率：", math.pi)
print("绝对误差：", error)
