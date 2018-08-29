import zmq
import sys
from collections import namedtuple

def main():
    if len(sys.argv) != 2:
        print("Must be called with an identity")
        exit()
    context = zmq.Context()
    socket = context.socket(zmq.DEALER)
    identity = sys.argv[1].encode('ascii')
    socket.identity = identity
    socket.connect("tcp://192.168.60.102:4444")
    print("Started client with id {}".format(identity))
    poller = zmq.Poller()
    poller.register(sys.stdin, zmq.POLLIN)
    poller.register(socket, zmq.POLLIN)

    while True:
        socks = dict(poller.poll())
        if socket in socks:
            sender, m = socket.recv_multipart()
            print("[{}]: {}".format(sender, m))

        elif sys.stdin.fileno() in socks:
            print("?")
            command = input()
            dest, msg = command.split(' ', 1)
            socket.send_multipart([bytes(dest, 'ascii'), bytes(msg, 'ascii')])
def map():
    
if __name__ == '__main__':
    main()
