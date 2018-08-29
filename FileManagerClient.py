import zmq
import sys
from collections import namedtuple

partSize = 1024 * 1024 * 10

def uploadFile(filename, socket):
    with open(filename , "rb") as f:
        finished = False
        part = 0
        while not finished:
            print("Uploading part {}".format(part))
            f.seek(part*partSize)
            bt = f.read(partSize)
            socket.send_multipart([filename, bt])
            response = socket.recv()
            print ("Server response %s" % response)
            part = part + 1
            if len(bt) < partSize:
                finished = True

def main():
    if len(sys.argv) != 4:
        print("Must be called with a filename")
        print ("Sample call: python FileManagerClient <username> <operation> <filename>")
        exit()


    username = sys.argv[1]
    operation = sys.argv[2]
    filename = sys.argv[3].encode('ascii')

    context = zmq.Context()

    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    if operation == 'upload':
        uploadFile(filename, socket)

    elif operation == 'share':
        print ("Not implemented yet")

    elif operation == 'download':
        print ("Not implemented yet")


if __name__ == '__main__':
    main()
