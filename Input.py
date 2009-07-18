import threading

class Input(threading.Thread):
    def __init__(self, connection):
        threading.Thread.__init__(self)

        self.connection = connection

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def send(self, x):
        self.connection.send(x)
        print '>>> %s' % x
