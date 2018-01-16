# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/15 0015 上午 11:31'

# 模拟掷骰子
import random


def roll_dice():
    """
    模拟掷骰子
    :return:
    """
    roll = random.randint(1, 7)
    return roll


def main():
    """
    主函数
    :return:
    """
    total_times = 10000

    result_list = [0] * 6
    for i in range(total_times):
        roll = roll_dice()
        for j in range(1, 7):
            if roll == j:
                result_list[j-1] += 1

    for i, result in enumerate(result_list):
        print('点数{}的次数：{},频率：{}'.format(i + 1, result, result/total_times))


if __name__ == '__main__':
    main()
