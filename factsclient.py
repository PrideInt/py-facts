import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 8888))

print("Connected to the server!")

take = input("Wanna hear a fact about a cat? Dog? Sloth? What, film? Tell me.\n")

if take == "quit":
    print("Peace.")
else:
    while take != "quit":
        client.send(take.encode())

        data = client.recv(1024)
        print(data.decode("utf-8"))

        take = input("Wanna hear another fact?\n")