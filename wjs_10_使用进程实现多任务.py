import threading
import time
import multiprocessing


def test1():
    while True:
        print("1-------")
        time.sleep(1)


def test2():
    while True:
        print("2-------")
        time.sleep(1)


def main():
    # 通过threading实现多线程的方式
    # t1 = threading.Thread(target=test1)
    # t2 = threading.Thread(target=test2)
    # t1.start()
    # t2.start()

    # 通过multiprocessing实现多进程的方式
    p1 = multiprocessing.Process(target=test1)
    p2 = multiprocessing.Process(target=test2)
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()