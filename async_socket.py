import socket
import asyncio
import pickle

MAX_DATA_SIZE = 1024

async def async_send(socket, obj):
    await asyncio.get_event_loop().sock_sendall(socket, pickle.dumps(obj))

async def async_recv(socket):
    return pickle.loads(await asyncio.get_event_loop().sock_recv(socket,MAX_DATA_SIZE)) 