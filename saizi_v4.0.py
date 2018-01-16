# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/15 0015 上午 11:31'

# 模拟掷骰子
# 模拟掷两个骰子
# 可视化投掷两个骰子的结果
# 直方图可视化结果
import random
import matplotlib.pyplot as plt

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def roll_dice():
    """
    模拟掷骰子
    :return:
    """
    roll = random.randint(1, 6)
    return roll


def main():
    """
    主函数
    :return:
    """
    total_times = 10000

    # 记录骰子的结果
    roll_list = []

    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()

        roll_list.append(roll1+roll2)

    # 数据可视化

    plt.hist(roll_list, bins=range(2, 14), normed=1, edgecolor="black", linewidth=1)
    plt.title("骰子点数统计")
    plt.xlabel("点数")
    plt.ylabel("概率")
    plt.show()


if __name__ == '__main__':
    main()
