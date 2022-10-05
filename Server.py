# Server
import cython

from pymathfun import fibo_c
import query_struct

import socket
import asyncio


HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 55555
MAX_DATA_SIZE = 256
CLIENT_NB = 1


query_struct.Query(query_struct.Query_type.COMPUTE)

"""
server = socket.socket()         
server.bind((HOST, PORT))        


while True:
    servers.listen(CLIENT_NB)
    client, addr = server.accept()
        
"""