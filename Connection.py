import socket

class Connection:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket()
        self.stringbuffer = ''

    def connect(self):
        self.socket.connect((self.host, self.port))

    def disconnect(self):
        self.socket.disconnect()

    def start(self):
        self.connect()

    def get_line(self):
        self.stringbuffer += self.socket.recv(1024)

        if self.stringbuffer.find('\r\n'):
            partitioned_line = self.stringbuffer.partition('\r\n')
            output = partitioned_line[0]
            self.stringbuffer = partitioned_line[2]
            return output

    def send(self, line):
        self.socket.send('%s\r\n' % line)

