#!/usr/bin/env python

import re
import Connection

class Bot:
    def __init__(self, host, port, nick):
        self.connection = Connection.Connection(host, port, nick)
        self.buffer_line = ''
        self.running = False
        pass

    def start(self):
        self.connection.connect()
        self.login()
        self.running = True
        self.run()

    def stop(self):
        self.running = False
        self.connection.disconnect()

    def run(self):
        while(self.running):
            line = self.connection.get_line()

            if line:
                self.handle_line(line)

    def login(self):
        self.send('NICK %s' % self.connection.nick)
        self.send('USER %s' % self.connection.user)

    def handle_line(self, line):
        self.keep_alive(line)
        print line
        pass

    def keep_alive(self, line):
        ping_expression = re.compile('^PING :.+$')
        if ping_expression.match(line):
            print 'PING FOUND'
            pass

    def send(self, x):
        self.connection.send(x)
        print '>>> %s' % x

