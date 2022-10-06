# Server
from pymathfun import fibo_c
import query_struct
import async_socket

import socket
import asyncio
import pickle


HOST = "127.0.0.1"
PORT = 55555
MAX_DATA_SIZE = 1024
CLIENT_NB = 1



async def async_exec(query : query_struct.Query) -> None:
    print("start")
    if (query.type == query_struct.Query_type.COMPUTE_FIBO):
        res = fibo_c(query.value) # Where there is potentially a long exectution time
        print(query.value)
        query.result = res
        query.status = query_struct.Query_Status.DONE


async def run_server(client_socket):
    task_list = []
    result_list = []
    client_socket.setblocking(False)
    while True:
        try:
            query = await async_socket.async_recv(client_socket)
        except:
            break
        if query.type == query_struct.Query_type.COMPUTE_FIBO:
            query.status = query_struct.Query_Status.SCHEDULED
            print("should start")
            task_list.append(asyncio.create_task(async_exec(query)))
            result_list.append(query)
        if query.type == query_struct.Query_type.LIST:
            await async_socket.async_send(client_socket, result_list)
    print("disconnected")
    for task in task_list:
        await task


def main():
    server_socket = socket.socket()         
    server_socket.bind((HOST, PORT))        
    while True:
        server_socket.listen(CLIENT_NB)
        client, addr = server_socket.accept()
        asyncio.run(run_server(client))
        
main()