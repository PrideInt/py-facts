import socket
import random

# Written by Pride

cat_facts = ["Cats have five toes on their front paws, but only four on their back paws.",
             "A tiger is a cat. It's the biggest species of the cat family. Therefore, if you have a pet tiger, you have a pet cat. Maybe go do battle with a friend who has a pet silver wolf. We know which one would win.",
             "A cat does not indeed have nine lives. They have one.",
             "Cats have a specialized collarbone that allows them to always land on their feet.",
             "Cats are better than dogs.",]

dog_facts = ["Dogs have a sense of time; they can tell the difference between an hour and five hours.",
             "Dogs can see in the dark.",
             "Dogs have three eyelids. The third lid, called a nictitating membrane or haw, keeps the eye lubricated and protected.",
             "Dogs are from a long line of canids that have been domesticated. They were once wolves!",
             "Some saliva of dogs have healing properties."]

sloth_facts = ["Sloths are the world's slowest mammal.",
               "Sloths move so slowly that algae grows on their fur.",
               "Sloths are solitary animals.",
               "Sloths use nature's bathroom once a week.",
               "Sloths are pretty good at swimming."]

film_facts = ["Michelle Yeoh is the first Asian woman to win the Academy Award for Best Actress.",
              "Parasite (2019) is the first non-English language film to win the Academy Award for Best Picture.",
              "Moonlight (2016) is the first film with an all-black cast and the first LGBTQ film to win the Academy Award for Best Picture.",
              "Oppenheimer (2023) was shot all on 65mm film.",
              "Director Wong Kar-Wai completed In the Mood for Love (2000) without a finished script and finalized editing a week before its debut at Cannes Film Festival."]

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 8888))
server.listen(1)

# I'm going to limit the server to only one client at a time
# since I don't want to implement multithreading. And I don't have to.

print("Waiting for a connection...")

while True:
    try:
        connection, address = server.accept()
        print(f"Connection from {address} has been established!")

        while True:
            data = connection.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode('utf-8')}")

            if data.decode("utf-8") == "cat":
                connection.send(bytes("> " + random.choice(cat_facts), "utf-8"))
            elif data.decode("utf-8") == "dog":
                connection.send(bytes("> " + random.choice(dog_facts), "utf-8"))
            elif data.decode("utf-8") == "sloth":
                connection.send(bytes("> " + random.choice(sloth_facts), "utf-8"))
            elif data.decode("utf-8") == "film":
                connection.send(bytes("> " + random.choice(film_facts), "utf-8"))
            elif data.decode("utf-8") == "quit" or data.decode("utf-8") == "exit" or data.decode("utf-8") == "peace":
                connection.send(bytes("> Peace.", "utf-8"))
                connection.close()
                break
            else:
                connection.send(bytes("> Not sure what that is. Ask me again.", "utf-8"))
        
        # Because I limited the connection to one client, I'll close the server after the client disconnects.
        print("Connection closed. Shutting down server.")
        server.close()
    except:
        print("Server has been shut down.")
        break