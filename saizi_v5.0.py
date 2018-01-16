# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/15 0015 上午 11:31'

# 模拟掷骰子
# 模拟掷两个骰子
# 可视化投掷两个骰子的结果
# 直方图可视化结果
import random
import matplotlib.pyplot as plt
import numpy as np


# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def main():
    """
    主函数
    :return:
    """
    total_times = 10000

    # 记录骰子的结果
    roll1_arr = np.random.randint(1, 7, size=total_times)
    roll2_arr = np.random.randint(1, 7, size=total_times)
    result_arr = roll1_arr + roll2_arr

    hist, bins = np.histogram(result_arr, bins=range(2, 14))
    print(hist)
    print(bins)
    # 数据可视化

    plt.hist(result_arr, bins=range(2, 14), normed=1, edgecolor="black", linewidth=1, rwidth=0.8)

    tick_labels = ['2点', '3点', '4点', '5点',
                   '6点', '7点', '8点', '9点',
                   '10点', '11点', '12点']
    tick_pos = np.arange(2, 13)+0.5
    plt.xticks(tick_pos, tick_labels)
    plt.title("骰子点数统计")
    plt.xlabel("点数")
    plt.ylabel("概率")
    plt.show()


if __name__ == '__main__':
    main()
