import multiprocessing
import queue


def download_from_web(q):
    """下载数据"""
    # 模拟网上下载数据
    data = [11, 22, 33, 44]

    # 向队列中写入数据
    for temp in data:
        q.put(temp)
    print("---下载完成，并存入数据到队列中---")


def analysis_data(q):
    """数据处理"""
    waitting_anlaysis_data = list()
    # 从队列中获取数据
    while True:
        data = q.get()
        waitting_anlaysis_data.append(data)

        if q.empty():
            break

    # 模拟数据的处理
    print("获取的数据是：%s" % waitting_anlaysis_data)


def main():
    # 1.创建一个队列,Queue()中数值的大小表示可放数量，不写将默认最大值
    q = multiprocessing.Queue()
    # 2.创建多个进程，将队列的引用当做实参进行传递到里面

    p1 = multiprocessing.Process(target=download_from_web, args=(q,))
    p2 = multiprocessing.Process(target=analysis_data, args=(q,))
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()
