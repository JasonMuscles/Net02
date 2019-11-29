import socket
import threading


def recv(udp_socket):
    # 接收数据
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print("来自%s的消息：%s" % (recv_data[1], recv_data[0].decode("GBK")))


def send(udp_socket, dest_ip, dest_port):
    # 发送数据
    while True:
        send_data = input("请输入你要发送的数据：")
        udp_socket.sendto(send_data.encode("GBK"), (dest_ip, dest_port))


def main():
    """完成UDP聊天器的整体控制"""
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定本地信息
    udp_socket.bind(("", 7788))

    # 获取对方的IP
    dest_ip = input("请输入你要访问的IP：")
    dest_port = int(input("请输入你需要访问的PORT："))

    # 关闭套接字
    # udp_socket.close()

    # 调用接收数据
    # recv(udp_socket)

    # 调用发送数据
    # send(udp_socket, dest_ip, dest_port)

    # 创建两个线程
    r = threading.Thread(target=recv, args=(udp_socket,))
    s = threading.Thread(target=send, args=(udp_socket, dest_ip, dest_port))

    r.start()
    s.start()


if __name__ == '__main__':
    main()
