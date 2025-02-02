#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()

sock.bind(('127.0.0.1', 9090))

sock.listen(1)

conn, addr = sock.accept()

while True:
    data = conn.recv(1024)
    print(data)
    if not data:
        break
    conn.send(data.upper())


