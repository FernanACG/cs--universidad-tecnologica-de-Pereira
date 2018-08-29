import zmq

Canal = zmq.Context()

print ("Conectando al servidor...")
socket = Canal.socket(zmq.REQ)
socket.connect("tcp://192.168.60.102:5555")

for solicitud in range(10):
    print ("Enviando solicitud %s ..." % solicitud)
    socket.send(b"David")

    Mensaje = socket. recv()
    print ("Respuesta % recibida [ %s ]" % (solicitud, Mensaje))
