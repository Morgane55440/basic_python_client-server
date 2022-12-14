# Client
import query_struct

import socket
import pickle

HOST = "127.0.0.1"
PORT = 55557
MAX_DATA_SIZE = 65536
CLIENT_PROMPT = "$ my_client "


def fibo_query(index,server_socket):
    """
    sends a query to compute fibo(index)
    """
    server_socket.send(pickle.dumps(query_struct.Query(query_struct.Query_type.COMPUTE_FIBO, value = index)))


def list_query(server_socket):
    """
    sends a query to get the list of computations
    """
    server_socket.send(pickle.dumps(query_struct.Query(query_struct.Query_type.LIST)))
    for query in pickle.loads(server_socket.recv(MAX_DATA_SIZE)):
        print(query)



def exec_query(server_socket):
    """
    gets a command, parses it and send the appropriate qury to the server
    """
    request = input(CLIENT_PROMPT).split()
    if len(request) == 2 and request[0] == "send":
        try:
            index = int(request[1])
        except:
            print(request[1] + " : not a valid number")
        else:
            fibo_query(index,server_socket)
    if len(request) == 1 and request[0] == "list":
        list_query(server_socket)


def main():
    server_socket = socket.socket()   
    server_socket.connect((HOST, PORT))
    while True:
        exec_query(server_socket)

if __name__ == "__main__":
    main()
