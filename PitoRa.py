#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

from PIL import Image, ImageFile
from io import BytesIO

sock = socket.socket()

sock.bind(('127.0.0.1', 9090))

sock.listen(1)

print("Server is listening...")

conn, addr = sock.accept()

print(f"Connection established with {addr}")

inp = input('Write here: ')
conn.send(b'screen')

while True:
    data = conn.recv(99999999)
    if data:
        image = Image.open(BytesIO(data))
        image.show()
    if not data:
        break
    conn.send(b'success')

sock.close()

