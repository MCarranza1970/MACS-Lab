import socket

smtp_server = "smtp.mailtrap.io"
puertos = [25, 465, 587, 2525]

def test_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        result = sock.connect_ex((host, port))
        sock.close()
        
        if result == 0:
            print(f"✅ Puerto {port} - ABIERTO")
            return True
        else:
            print(f"❌ Puerto {port} - CERRADO (Código: {result})")
            return False
    except Exception as e:
        print(f"❌ Puerto {port} - Error: {e}")
        return False

print("🔍 Probando puertos de Mailtrap...")
print("="*30)

puertos_abiertos = []
for puerto in puertos:
    if test_port(smtp_server, puerto):
        puertos_abiertos.append(puerto)

print("\n" + "="*30)
if puertos_abiertos:
    print(f"✅ Puertos abiertos: {puertos_abiertos}")
    print(f"💡 Usa: {puertos_abiertos[0]}")
else:
    print("❌ Ningún puerto está accesible")
    print("🔍 Verifica tu firewall y conexión a Internet")