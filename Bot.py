import re
import threading
import time
from Connection import Connection
from Input import Input
from Output import Output

class Bot(threading.Thread):
    def __init__(self, host, port, nick):
        threading.Thread.__init__(self)

        self.connection = Connection(host, port, nick)
        self.input = Input(self.connection)
        self.output = Output(self.connection)

        self.buffer_line = ''
        self.running = False

    def start(self):
        self.connection.start()
        self.input.start()
        self.output.start()

        print('before')
        time.sleep(2.5)
        print('after')
        self.login()

    def stop(self):
        self.running = False
        self.connection.disconnect()

    def login(self):
        self.input.send('NICK %s' % self.connection.nick)
        self.input.send('USER %s' % self.connection.user)

    def handle_line(self, line):
        self.keep_alive(line)
        print line

    def keep_alive(self, line):
        ping_expression = re.compile('^PING :.+$')
        if ping_expression.match(line):
            print 'PING FOUND'

