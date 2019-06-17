'''
    @author: ella
    @project: python集中学习_2019.06
    @file: python_learning_debug.py
    @time: 2019-06-11 11:21
    @desc:使用pycharm进行断点debug:
    '''

#断点（break point）是指在代码中指定位置，当程序运行到此位置时变中断下来，并让开发者可查看此时各变量的值。因断点中断的程序并没有结束，可以选择继续执行。

drink_price = {
     "橙汁": 3.5,
     "椰汁": 4,
     "矿泉水": 2,
     "早餐奶": 4.5
 }

def auto_fanmaiji(money, drink_name):
    if money <= 10:
        for drink, price in drink_price.items():
             if drink_name == drink:
                 if money > price:
                     print("请取出饮料: %s" % drink_name)
                     print("应找您%3.1f元" % (money - price))
                 elif money == price:
                     print("请取出饮料: %s" % drink_name)
                 else:
                     print("sorry, 您的金额不足以买:%s" % drink_name)
             else:
                 continue
    else:
       print("sorry, 本机最大金额不能超过10元，请重试！")

auto_fanmaiji(7.3, "橙汁")