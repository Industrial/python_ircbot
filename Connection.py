#!/usr/bin/env python

import socket

class Connection:
    def __init__(self, host, port, nick):
        self.host = host
        self.port = port
        self.nick = nick
        self.user = self.nick + ' 0 :' + self.nick + ' ' + self.nick
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.stringbuffer = ""

    def connect(self):
        self.socket.connect((self.host, self.port))

    def disconnect(self):
        self.socket.disconnect()

    def get_line(self):
        self.stringbuffer += self.socket.recv(1024)

        if self.stringbuffer.find('\r\n'):
            partitioned_line = self.stringbuffer.partition('\r\n')
            output = partitioned_line[0]
            self.stringbuffer = partitioned_line[2]
            return output

    def send(self, x):
        self.socket.send(x)
