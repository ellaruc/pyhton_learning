'''
    @author: ella
    @project: python集中学习_2019.06
    @file: python_learning_def.py
    @time: 2019-05-30 12:05
    @desc:python100days-函数与模块
    '''

#可变参数
#具体有多少个参数是未知的，由调用者决定

def add(*args):
    '''
    :param args: 可变的参数个数用*arg来表示，引用是用for循环
    :return:
    '''
    total =0
    for val in args:
        total += val
    return total


#返回函数：可以把函数作为返回结果值返回,这个时候调用lazy_sum，返回的就是求和函数，而不是求和结果

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1,2,3) #f是函数
f() #调用函数f时，才是真正求和的函数+

#实现判断1个数是不是素数的函数
def is_prime(num):
    if num==1:
        return 'illegal input'
    else:
        for i in range(2, num):
            if num % i == 0:  # 比num小的数，是不是都不能被num整除，也就是余数是不是为0，比如7，除了7/1和7/7，其余都有余数，因此是素数
                return '不是素数'
            else:
                return '素数'

#变量作用域
#pythonk可以在函数内部在定义函数
#b这个变量在foo里作用，foo的外部不能访问到他。c只在bar里作用，a写在了main函数里，全局作用

def foo():
    b='hello'

    def bar():
        c= True
        print(b)
        print(c)
    bar()


#map函数的用法(传入的第一个参数位f，即函数对象本身，第二个参数为函数作用的对象，返回函数作用后的对象）
#将输入的不规范的英文名字，变成全部小写
def normalize(name):
    return name.lower()

#reduce函数的用法(参数与map类似，作用为把结果继续和下一个元素带到函数里进行计算）reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from  functools import reduce
def sum(x, y):
  return x + y

#filter函数的用法（参数与map类似，fliter把传入的函数作用于每个元素，根据返回值是true或者是false决定保留还是丢弃）
# 注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list
def is_odd(n):
    return n%2 ==1

#sort函数接收一个key函数来实现自定义的排序(key中可以使用各种函数，reverse表示排序的顺序，如果为ture则表示从大到小）
print(sorted([36,5,-12,9,-21],key=abs))
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)

#匿名函数：不需要显式地定义函数，直接传入匿名函数（可以为了避免代码里有很多的单行函数）
#lambda x,y:x+y 等同于
# def sum(x, y):
#    return x + y
# 冒号前的x表示函数参数，不需要写返回值，返回值就是表达式的结果
list(map(lambda x,y:x+y ,[1,2],[3,4]))
list(filter(lambda x:x%2 ==0,range(6)))

#装饰器：为已经存在的函数添加额外的功能，一般有插入日志、性能测试、事务处理、缓存、权限校验等

def debug(func):
    def wrapper():
        print("[DEBUG]: enter {}()".format(func.__name__)) #在原来的函数上多做了一步'打印日志'
        return func()
    return wrapper

@debug
def say_hello():
    print("hello!")


##制定可变参数*args和关键参数**kwargs
def debug(func):
    def wrapper(*args, **kwargs):  # 指定宇宙无敌参数
        print("[DEBUG]: enter {}()".format(func.__name__))
        print ('Prepare and say...',)
        return func(*args, **kwargs)
    return wrapper  # 返回

@debug
def say(something):
    print ("hello {}!".format(something))


#偏函数：把一个函数的某些参数给固定住，返回一个新的函数，调用这个新函数会更加难
import functools
int2 = functools.partial(int, base=2)
int2('1000000')

#主函数
def main():
    a=100
    foo()
    print(add(1,2)) #3
    print(add(1,2,3)) #6
    print(is_prime(1)) #illegal input
    print(is_prime(4)) #不是素数
    print(is_prime(7)) #素数
    print(list(map(normalize,['adam', 'LISA', 'barT'])))
    print(reduce(sum, [1, 3, 5, 7, 9]))
    print(list(filter(is_odd,[1,2,3,4,5,6,7,8])))
    print(sorted([36, 5, -12, 9, -21], key=abs))



if __name__ == '__main__':
    print('start')
    main()
    print('end')

