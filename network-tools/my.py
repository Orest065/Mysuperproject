import subprocess

def ping_sweep(network):
    for i in range(1, 255):
        ip = f"{network}.{i}"
        result = subprocess.run(["ping", "-n", "1", "-w", "100", ip], stdout=subprocess.DEVNULL)
        if result.returncode == 0:
            print(f"{ip} is online")

if __name__ == "__main__":
    subnet = input("Enter the first three octets of the subnet (e.g., 192.168.1): ")
    ping_sweep(subnet)
