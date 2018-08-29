import zmq

Canal = zmq.Context()
socket = Canal.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    Mensaje = socket.recv()
    if Mensaje == 'Asdas':
        print ("Solicitud recibida: %s" % Mensaje)

    socket.send(b"Mundo")
