import zmq
import sys

def main():
	if len(sys.argv) != 1:
		print("Must be called with no arguments")
		exit()

	context = zmq.Context()
	socket = context.socket(zmq.ROUTER)
	socket.bind("tcp://*:4444")

	print("Started server")

	while True:
		ident, dest, msg = socket.recv_multipart()
		print("Message received from {}".format(msg))
		socket.send_multipart([dest , ident, msg])

if __name__ == '__main__':
	main()
