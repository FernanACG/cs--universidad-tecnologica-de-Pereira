import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:6666")

while True:
    name, bt = socket.recv_multipart()
    print ("Llega {}".format(name)
    with open("down-" + name.decode("ascii"), "ab")as f:
        f.write(bt)
        f.close()

    socket.send(b'Done')
