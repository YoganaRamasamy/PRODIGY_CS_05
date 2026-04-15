from scapy.all import sniff

def packet_callback(packet):
    print("\n--- Packet Captured ---")

    if packet.haslayer("IP"):
        ip_layer = packet["IP"]
        print(f"Source IP: {ip_layer.src}")
        print(f"Destination IP: {ip_layer.dst}")

    if packet.haslayer("TCP"):
        print("Protocol: TCP")
    elif packet.haslayer("UDP"):
        print("Protocol: UDP")

    if packet.haslayer("Raw"):
        print(f"Payload: {packet['Raw'].load}")

print("Starting packet capture... (Press Ctrl+C to stop)")
sniff(prn=packet_callback, count=10)
