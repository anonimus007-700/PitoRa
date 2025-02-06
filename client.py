#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import base64
import os

from PIL import Image, ImageGrab
from io import BytesIO

def image_to_data_url(img):
    img.save(byte_io, format='PNG')

    img_bytes = buffer.getvalue()

    img_base64 = base64.b64encode(img_bytes).decode('utf-8')

    mime_type = f"image/{img.format.lower()}"
    data_url = f"data:{mime_type};base64,{img_base64}"

    return data_url

sock = socket.socket()
byte_io = BytesIO()

sock.connect(('127.0.0.1', 9090))

screen = ImageGrab.grab()
print(screen)
# data = image_to_data_url(screen)
screen.save(byte_io, 'JPEG')
data = byte_io.getvalue()

sock.sendall(data)

while True:
    data = sock.recv(4096)
    print(data)
    if not data:
        break
