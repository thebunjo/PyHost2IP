import socket

while True:
    try:
        web_address = input("Enter the host address (e.g., www.example.com): ")

        if not web_address:
            print("Host address cannot be empty.")
            continue

        socket.setdefaulttimeout(1)
        address = socket.gethostbyname(web_address)
        print(f"Host IP: {address}")
    except socket.gaierror:
        print("Invalid host or host is unreachable.")
    except KeyboardInterrupt:
        print("Program terminated by user.")
        break
    except ValueError:
        print("ValueError for host.")
