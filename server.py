#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import select
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Menores que 1024 são restritos ao SO
s.bind(('', 1026))
s.listen(5)
c_inputs = []
requests = {}

while True:
    rlist, wlist, xlist = select.select(c_inputs + [s], [], [])
    print(rlist)
    for client in rlist:
        if client == s:
            client, addr = s.accept()

            client.setblocking(False)
            c_inputs.append(client)
            requests[client] = b''
        else:
            requests[client] += client.recv(1500)
            request = requests[client]
            if b'\r\n\r\n' in request or b'\n\n' in request:
                method, path, lixo = request.split(b' ', 2)

                if method == b'GET':
                    print(path)
                    if path == b'/':
                        response_content = open('index.html', 'rb').read()
                        status = '200 OK'
                    else:
                        response_content = open('generic_error.html','rb').read()
                        status = '404 Not Found'
                elif method == b'POST':
                    print(method, path,"\n", lixo)
                    response_content = b'Arquivo recebido com sucesso xD'
                    status = '200 OK'
                else:
                    response_content = open('generic_error.html', 'rb').read()
                    status = '400 Bad Request'

                response = b'HTTP/1.0 %s\r\nContent-Length: %d\r\n\r\n' % status, len(response_content)
                response += response_content
                client.send(response)
                client.close()
                del requests[client]
                c_inputs.remove(client)
