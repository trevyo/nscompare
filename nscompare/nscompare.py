import socket
import dns.resolver
from prompt_toolkit import PromptSession
from prompt_toolkit.history import InMemoryHistory

def get_ip_address(hostname):
    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror:
        return None

def query_dns(nameserver, record_type, domain):
    ip_address = get_ip_address(nameserver)
    if not ip_address:
        return f"Error: Could not resolve IP address for nameserver {nameserver}"

    resolver = dns.resolver.Resolver()
    resolver.nameservers = [ip_address]
    try:
        return sorted([str(answer) for answer in resolver.resolve(domain, record_type)])
    except Exception as e:
        return str(e)

def interactive_mode():
    session = PromptSession(history=InMemoryHistory())
    server1 = server2 = record_type = None

    while True:
        try:
            cmd_input = session.prompt("> ").strip()
            if not cmd_input:
                continue
            if 'set type=' in cmd_input:
                cmd_parts = cmd_input.split('=', 1)
                command = cmd_parts[0].strip().lower()
                if len(cmd_parts) > 1 and command == 'set type':
                    record_type = cmd_parts[1].strip().upper()
                    continue

            cmd_parts = cmd_input.split()
            command = cmd_parts[0].lower()

            if command == "server1" and len(cmd_parts) > 1:
                server1 = cmd_parts[1]
            elif command == "server2" and len(cmd_parts) > 1:
                server2 = cmd_parts[1]
            elif command == "set" and len(cmd_parts) >= 3:
                if cmd_parts[1].lower() == "type":
                    record_type = cmd_parts[2].upper()
            elif server1 and server2 and record_type and command != "server1" and command != "server2" and command != "set":
                domain = cmd_input
                response1 = query_dns(server1, record_type, domain)
                response2 = query_dns(server2, record_type, domain)
                if response1 == response2:
                    print("Match")
                else:
                    print("Do not match")
                    print(f"Response from {server1}: {response1}")
                    print(f"Response from {server2}: {response2}")
            else:
                print("Invalid command or missing information")
        except KeyboardInterrupt:
            print("\nExiting interactive mode.")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    print("DNS Comparison Tool")
    print("Use commands: 'server1 [IP/hostname]', 'server2 [IP/hostname]', 'set type=[TYPE]', '[domain]'")
    interactive_mode()