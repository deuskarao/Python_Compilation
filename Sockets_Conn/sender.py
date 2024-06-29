import os
import socket

ip = ""
port = ""
file_to_send = ""  # full path if not in the same folder as this code
ext = file_to_send.split(".")[:-1]

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((ip, port))

file = open(file_to_send, "rb")

file_size = os.path.getsize(file_to_send)

client.send(f"received_file.{ext}".encode())

client.send(str(file_size).encode())

data = b"file.read"

client.sendall(data)

client.send(b"-END-")

file.close()
