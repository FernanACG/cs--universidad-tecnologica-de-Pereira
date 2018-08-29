import zmq
import sys

context = zmq.Context()
servers = context.socket(zmq.REP)
servers.bind("tcp://*:5555")

clients = context.socket(zmq.REP)
clients.bind("tcp://*:6666")

poller = zmq.Poller()
poller.register(servers.zmq.POLLIN)
poller.register(clients.zmq.POLLIN)

while True:
    socks = dict(poller, poll()))
    if client in socks:
        print ("message from client")
        msg = client.recv_multipart()
        print(msg)

    if server in socks:
        print ("message from server")
        operation, *rest = server.recv_multipar()
        print(msg)
