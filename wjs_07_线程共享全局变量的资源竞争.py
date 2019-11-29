import threading
import time

# 定义一个全局变量
g_num = 0


def test1(num):
    global g_num
    for i in range(num):
        g_num += 1
    print("—————test1 g_num=%s—————" % g_num)


def test2(num):
    global g_num
    for i in range(num):
        g_num += 1
    print("—————test2 g_num=%s—————" % g_num)


def main():
    # target指定将来这个线程去哪个函数执行代码
    # args自定将来调用函数的时候传递什么数据过去

    t1 = threading.Thread(target=test1, args=(100000, ))
    t2 = threading.Thread(target=test2, args=(100000, ))

    t1.start()
    t2.start()

    # 等待上面执行完成
    time.sleep(2)

    print("----in main Thread g_nums = %s-----" % g_num)


if __name__ == '__main__':
    main()
