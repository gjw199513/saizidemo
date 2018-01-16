# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/15 0015 上午 11:31'

# 模拟掷骰子
# 模拟掷两个骰子
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

    result_list = [0] * 11
    roll_list = list(range(2, 13))
    roll_dict = dict(zip(roll_list, result_list))
    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()
        for j in range(2, 13):
            if (roll1 + roll2) == j:
                roll_dict[j] += 1

    for i, result in roll_dict.items():
        print('点数{}的次数：{},频率：{}'.format(i, result, result/total_times))


if __name__ == '__main__':
    main()
