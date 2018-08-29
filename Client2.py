import zmq

Canal = zmq.Context()

print ("Conectando al servidor...")
socket = Canal.socket(zmq.REQ) # REQ = Request
socket.connect("tcp://localhost:5555")

info = {'operacion':'resta', 'arg1':1, 'arg2':3}

socket.send_json(info)
Mensaje = socket.recv_json()
print ("Respuesta recibida [ %s ]" % (Mensaje))
