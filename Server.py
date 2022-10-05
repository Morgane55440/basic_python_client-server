# Server
import cython

from pymathfun import fibo_c
import query_struct

import socket
import asyncio
import pickle


HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 55555
MAX_DATA_SIZE = 1024
CLIENT_NB = 1



async def async_exec(query : query_struct.Query) -> None:
    if (query.type == query_struct.Query_type.COMPUTE_FIBO):
        res = fibo_c(query.value) # Where there is potentially a long exectution time
        print(query.value)
        query.value = res
        query.status = query_struct.Query_Status.DONE




async def run_server(client_socket):
    task_list = []
    result_list = []
    running = True
    while running:
        query = pickle.load(client_socket.recv(MAX_DATA_SIZE))
        if query.type == query_struct.Query_type.COMPUTE_FIBO:
            query.status = query_struct.Query_Status.SCHEDULED
            task_list.append(async_exec(query))
            result_list.append(query)
        if query.type == query_struct.Query_type.LIST:
            for res in result_list:
                client_socket.send(pickle.dump(res))
            client_socket.send(pickle.dump(query_struct.Query(query_struct.Query_type.LIST_END)))
    for task in task_listl:
        await task.status



server_socket = socket.socket()         
server_socket.bind((HOST, PORT))        


while True:
    server_socket.listen(CLIENT_NB)
    client, addr = server_socket.accept()
    asyncio.run(run_server(client))
        
