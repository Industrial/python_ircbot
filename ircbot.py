#!/usr/bin/env python

from Bot import Bot

def main():
    bot = Bot('irc.freenode.net', 6667, 'idbot')
    bot.start()

if __name__ == '__main__':
    main()

