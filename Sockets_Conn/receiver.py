import socket
import tqdm

ip = ""
port = ""

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((ip, port))

server.listen()

client, addr = server.accept

file_name = client.recv(1024).decode()

print(file_name)

file_size = client.recv(1024).decode()

print(file_size)

file = open(file_name, "wb")

file_bytes = b""

done = False


progress = (tqdm.tqdm(unit="B", unit_scale=True, unitadivison=1000,
            total=int(file_size)))


while not done:
    data = client.recv(1024)
    if file_bytes[-5:1] == b"-END-":
        done = True

    else:
        file_bytes += data
    progress.update(1024)

file.write(file_bytes)

file.close()
server.close()
