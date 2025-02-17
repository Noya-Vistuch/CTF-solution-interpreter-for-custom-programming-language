import socket

def main():
    # Define the IP address and port number of the server to connect to
    server_ip = "" # Fill here Ex. "8.8.8.8"
    server_port = "" # Fill here Ex. 53

    # Create a TCP socket for the client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Attempt to connect to the server
        client_socket.connect((server_ip, server_port))

        # Read the contents of a text file to send as a message to the server
        with open(r"C:\Users\Mamriot_User\Downloads\test22.txt", "r") as file:
            message = file.read()

        # Send the message to the server
        client_socket.sendall(message.encode())

        # Receive data from the server
        data = client_socket.recv(1024)

        # Print the received data from the server
        print("Received from server:", data.decode())

    except ConnectionRefusedError:
        # Handle the case where the connection is refused by the server
        print("Connection was refused.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        # Close the client socket
        client_socket.close()


if __name__ == "__main__":
    main()