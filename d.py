import socket

def start_udp_server(host='0.0.0.0', port=12345):
    """Start a UDP server that listens for incoming packets."""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((host, port))
        print(f"UDP server listening on {host}:{port}")

        while True:
            data, addr = server_socket.recvfrom(1024)  # Buffer size is 1024 bytes
            print(f"Received packet from {addr}: {data.hex()}")  # Print received data in hex format

if __name__ == "__main__":
    start_udp_server()