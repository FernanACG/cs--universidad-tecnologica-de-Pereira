import zmq

Canal = zmq.Context()
socket = Canal.socket(zmq.REP) #REP = Reply
socket.bind("tcp://*:5555")

while True:
    Mensaje = socket.recv_json()
    if Mensaje['operacion'] == 'suma':
        Respuesta = Mensaje['arg1'] + Mensaje['arg2']
        socket.send_json({'resultado':Respuesta})
    elif Mensaje['operacion'] == 'resta':
        Respuesta = Mensaje['arg1'] - Mensaje['arg2']
        socket.send_json({'resultado':Respuesta})
    else:
        print ("No entendi esto: %s" % Mensaje)
        socket.send_json({'resultado':'No entendi'})
