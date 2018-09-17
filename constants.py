#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
    constants.py
    Definição de constantes utilizadas no socket
"""
OK = b'200 OK'
NOT_FOUND = b'404 Not Found'
FORB = b'403 Forbidden'
NOT_IMPL = b'501 Not Implemented'
BAD_REQ = b'400 Bad Request'

# Menores que 1024 são restritos ao SO
SOCK_PORT = 1026
MAX_SIZE_MSG = 1500

HTML_GEN_BEGIN = b'<html lang="en"><head><meta charset="utf8"></head><body>'
HTML_GEN_END = b'</body></html>'
