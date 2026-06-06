import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8080))
print("Connected to server")
print("You can start sending messages to the server. Type 'exit' to quit.")
while True:
    message = input("Enter message: ")
    if message == "exit":
        break
    client_socket.send(message.encode())
    response = client_socket.recv(1024)
    print("Message from server: ", response.decode())
client_socket.close()