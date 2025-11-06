import serial.tools.list_ports

def detectBoardPort():
    import serial
    ports = serial.tools.list_ports.comports()

    for port in ports:
        if "Arduino" in port.description or "CH340" in port.description:
            #print(f"Board description: {port.description}")
            #print(f"Board port: {port.device}")
            #print(f"Port name: {port.name}")
            #print(f"HWID: {port.hwid}")
            #print(f"Vendor ID: {port.vid}")
            #print(f"Manufacturer: {port.manufacturer}")
            #print(f"Location: {port.location}")
            return port.device
    return None

port = detectBoardPort()

if port:
    print(f"Board port detected: {port}")
else :
    print("No board port detected")