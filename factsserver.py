import socket
import random

cat_facts = ["Cats have five toes on their front paws, but only four on their back paws.",
             "Cats have a third eyelid called a haw.",
             "A cat's nose is ridged with a unique pattern, just like a human fingerprint",
             "Cats have a specialized collarbone that allows them to always land on their feet.",
             "Cats are better than dogs.",]

dog_facts = ["Dogs have a sense of time. It's been proven that they know the difference between a hour and five.",
             "Dogs can see in the dark.",
             "Dogs have three eyelids. The third lid, called a nictitating membrane or haw, keeps the eye lubricated and protected.",
             "Dogs have about 1,700 taste buds.",
             "Some saliva of dogs have healing properties."]

sloth_facts = ["Sloths are the world's slowest mammal.",
               "Sloths are so slow that algae grows on their fur.",
               "Sloths are solitary animals.",
               "Sloths only urinate/defecate once a week.",
               "Sloths are pretty good at swimming."]

film_facts = ["Michelle Yeoh is the first Asian woman to win the Academy Award for Best Actress.",
              "Parasite (2019) is the first non-English language film to win the Academy Award for Best Picture.",
              "Moonlight (2016) is the first film with an all-black cast and the first LGBTQ film to win the Academy Award for Best Picture.",
              "Oppenheimer (2023) was shot all on 65mm film.",
              "Director Wong Kar-Wai completed In the Mood for Love (2000) without a finished script and finalized editing a week before its debut at Cannes Film Festival."]

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 8888))
server.listen(1)

print("Waiting for a connection...")

while True:
    try:
        client, address = server.accept()
        print(f"Connection from {address} has been established!")

        while True:
            data = client.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode('utf-8')}")

            if data.decode("utf-8") == "cat":
                client.send(bytes("> " + random.choice(cat_facts), "utf-8"))
            elif data.decode("utf-8") == "dog":
                client.send(bytes("> " + random.choice(dog_facts), "utf-8"))
            elif data.decode("utf-8") == "sloth":
                client.send(bytes("> " + random.choice(sloth_facts), "utf-8"))
            elif data.decode("utf-8") == "film":
                client.send(bytes("> " + random.choice(film_facts), "utf-8"))
            elif data.decode("utf-8") == "quit" or data.decode("utf-8") == "exit" or data.decode("utf-8") == "peace":
                client.send(bytes("> Peace.", "utf-8"))
                client.close()
                break
            else:
                client.send(bytes("> Not sure what that is. Ask me again.", "utf-8"))
        
        print("Connection closed. Shutting down server.")
        server.close()
    except:
        print("Server has been shut down.")
        break