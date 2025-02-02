#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import base64
import os

from PIL import Image, ImageGrab
from io import BytesIO
from pyautogui import screenshot

def image_to_data_url(image_path):
    with Image.open(image_path) as img:
        buffer = BytesIO()
        img.save(buffer, format=img.format)

        img_bytes = buffer.getvalue()

        img_base64 = base64.b64encode(img_bytes).decode('utf-8')

        mime_type = f"image/{img.format.lower()}"
        data_url = f"data:{mime_type};base64,{img_base64}"

        return data_url

sock = socket.socket()

sock.connect(('127.0.0.1', 9090))

screen = ImageGrab.grab()
data = image_to_data_url(screen)

sock.send(data)

data = sock.recv(1024)
sock.close()

print(data)
