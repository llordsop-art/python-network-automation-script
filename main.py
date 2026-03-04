import netmiko
from netmiko import ConnectHandler

def configure_network_device(device_ip, username, password):
    """
    Connects to a network device via SSH and retrieves its status.
    Designed for Cisco IOS devices, but can be adapted for others.
    """
    
    # Device connection parameters
    device = {
        'device_type': 'cisco_ios',
        'host': device_ip,
        'username': username,
        'password': password,
    }

    try:
        print(f"[*] Attempting to connect to {device_ip}...")
        
        # Establishing SSH connection
        with ConnectHandler(**device) as ssh_conn:
            print(f"[+] Successfully connected to {device_ip}")
            
            # Sending a basic command to check device status
            output = ssh_conn.send_command("show ip interface brief")
            
            print("--- Device Output ---")
            print(output)
            print("----------------------")
            
    except Exception as e:
        print(f"[!] Connection failed to {device_ip}: {str(e)}")

if __name__ == "__main__":
    print("=== Python Network Automation Tool Started ===")
    
    # Placeholder values for demonstration
    TARGET_IP = "192.168.1.1"
    USER = "admin"
    PWD = "secretpassword"
    
    configure_network_device(TARGET_IP, USER, PWD)
