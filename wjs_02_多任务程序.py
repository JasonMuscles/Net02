import time
import threading

def sing():
    for i in range(5):
        print("————————正在唱歌————————")
        time.sleep(1)


def dance():
    for i in range(5):
        print("————————正在跳舞————————")
        time.sleep(1)


def main():
    s = threading.Thread(target=sing)
    d = threading.Thread(target=dance)
    s.start()
    d.start()


if __name__ == "__main__":
    main()