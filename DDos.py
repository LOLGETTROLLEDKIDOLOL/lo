import socket
import random
import threading

def send_packets(ip, port, packet_size, num_packets, thread_id):
    """Function to send packets in a separate thread."""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        data = random._urandom(packet_size)  # Generate random packet data
        for i in range(num_packets):
            s.sendto(data, (ip, port))
            if i % 1000 == 0:  # Print status every 1000 packets
                print(f"Thread {thread_id}: Sent {i} packets", end='\r')

def main():
    ip = input("Enter target IP (server IP): ")
    port = int(input("Enter target port (server port): "))
    packet_size = int(input("Enter packet size (bytes, max 65507 for UDP): "))
    num_packets = int(input("Enter total number of packets to send: "))
    num_threads = int(input("Enter number of threads to use: "))

    threads = []
    packets_per_thread = num_packets // num_threads

    for i in range(num_threads):
        thread = threading.Thread(target=send_packets, args=(ip, port, packet_size, packets_per_thread, i + 1))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("\nAll packets sent.")

if __name__ == "__main__":
    main()