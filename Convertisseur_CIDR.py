import ipaddress

def cidr_to_range(cidr):
    try:
        # Créer un objet réseau à partir de la notation CIDR
        network = ipaddress.ip_network(cidr, strict=False)
        
        # Obtenir la première et la dernière adresse de la plage
        first_ip = network.network_address
        last_ip = network.broadcast_address
        
        return first_ip, last_ip
    except ValueError as e:
        return str(e)

def main():
    cidr_input = input("Entrez une adresse IP en notation CIDR (ex: 192.168.1.0/24) : ")
    ip_range = cidr_to_range(cidr_input)
    
    if isinstance(ip_range, tuple):
        print(f"La plage d'adresses pour {cidr_input} est de {ip_range[0]} à {ip_range[1]}.")
    else:
        print(f"Erreur : {ip_range}")

if __name__ == "__main__":
    main()
