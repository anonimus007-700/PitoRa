#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

from PIL import Image, ImageFile
from io import BytesIO

ImageFile.LOAD_TRUNCATED_IMAGES = True

sock = socket.socket()

sock.bind(('127.0.0.1', 9090))

sock.listen(1)

print("Server is listening...")

conn, addr = sock.accept()

print(f"Connection established with {addr}")

while True:
    data = conn.recv(4096)
    if data:
        img = Image.open(BytesIO(data))
        #img = Image.open(BytesIO(data))
        #img = data.decode('utf-8')
        #img = eval(img)
        img.show()
    if not data:
        break
    conn.send(b'success')


