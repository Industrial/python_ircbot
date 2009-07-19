from Connection import Connection

class Bot:
    def __init__(self, host, port, nick):
        self.nick = nick
        self.user = '%s %s 0 : %s' % (nick, host, nick)
        self.buffer_line = ''
        self.running = False

        self.connection = Connection(host, port)

    def start(self):
        self.connection.start()

        self.send('NICK %s' % self.nick)
        self.send('USER %s' % self.user)
        self.send('JOIN #idtest')
        self.send('PRIVMSG #idtest LULZ')

        self.running = True

        while self.running:
            line = self.connection.get_line()
            if line:
                self.handle_line(line)

    def stop(self):
        self.running = False
        self.connection.disconnect()

    def handle_line(self, line):
        self.keep_alive(line)
        print line

    def keep_alive(self, line):
        if line[0:4] == 'PING':
            self.connection.send('PONG %s' % line[5:])

    def send(self, x):
        self.connection.send(x)
        print '>>> %s' % x

