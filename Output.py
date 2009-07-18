import threading

class Output(threading.Thread):
    def __init__(self, connection):
        threading.Thread.__init__(self)

        self.connection = connection

    def start(self):
        self.running = True

        while self.running:
            line = self.connection.get_line()
            if line:
                print(line)

    def stop(self):
        self.running = False
