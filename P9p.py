import os
import re
import threading

def is_valid_ip(ip):
    """Validate the IP address format."""
    pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    return pattern.match(ip) is not None

def print_banner():
    """Print the banner."""
    print(''' 
░▒▓███████▓▒░ ░▒▓██████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓███████▓▒░ ░▒▓███████▓▒░ 
░▒▓█▓▒░             ░▒▓█▓▒░ 
░▒▓█▓▒░             ░▒▓█▓▒░ 
░▒▓█▓▒░       ░▒▓██████▓▒░                                                                                                                                              
    ''')

def ping_host(host):
    """Function to ping the host."""
    while True:
        print(f"Pinging {host}...")
        send_ping = os.system("ping -c 1 " + host)  # Use -c 1 for Unix/Linux, -n 1 for Windows
        if send_ping == 0:
            print("Ping successful")
        else:
            print("Ping failed")

def main():
    print_banner()
    host = input('Enter IP address to ping: ')

    if not is_valid_ip(host):
        print("Invalid IP address format. Please enter a valid IP.")
        return

    # Number of threads to use for sending pings
    num_threads = 10  # Adjust this number based on your needs

    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=ping_host, args=(host,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete (they won't in this infinite loop, but you can manage it as needed)
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()

