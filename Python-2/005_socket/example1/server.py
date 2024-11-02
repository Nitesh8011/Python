import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 12345

server_socket.bind((host,port))
server_socket.listen(5)
print("Server listening at ",host,':',port)

client_socket, client_address = server_socket.accept()
print("Connection established with ", client_address)

data = client_socket.recv(1024).decode('utf-8')
print('Received: ',data)

client_socket.send(data.encode('utf-8'))

client_socket.close()
server_socket.close()