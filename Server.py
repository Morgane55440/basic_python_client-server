# Server
from pymathfun import fibo_c
import query_struct

import socket
import asyncio
import pickle


HOST = "127.0.0.1"
PORT = 55557
MAX_DATA_SIZE = 1024
CLIENT_NB = 1



async def async_exec(query : query_struct.Query) -> None:
    print("start")
    if (query.type == query_struct.Query_type.COMPUTE_FIBO):
        res = fibo_c(query.value) # Where there is potentially a long exectution time
        print(query.value)
        query.result = res
        query.status = query_struct.Query_Status.DONE


async def run_server(client_socket, result_list):
    try:
        query = pickle.loads(client_socket.recv(MAX_DATA_SIZE))
    except:
        print("client disconnected")
        return 
    print('new query : {0}'.format(query.type))
    if query.type == query_struct.Query_type.COMPUTE_FIBO:
        query.status = query_struct.Query_Status.SCHEDULED
        result_list.append(query)
        return await asyncio.gather(run_server(client_socket, result_list), async_exec(query))
    if query.type == query_struct.Query_type.LIST:
        client_socket.send(pickle.dumps(result_list))
    return await run_server(client_socket, result_list)

def server_start(client_socket):
    result_list = []
    asyncio.run(run_server(client_socket, result_list))



def main():
    server_socket = socket.socket()         
    server_socket.bind((HOST, PORT))        
    while True:
        server_socket.listen(CLIENT_NB)
        client, _ = server_socket.accept()
        print("client connected")
        server_start(client)
        
if __name__ == "__main__":
    main()