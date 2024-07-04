import requests
import json

def get_ip_info(ip=''):
    try:
        # Jika tidak ada IP yang diberikan, gunakan alamat IP publik
        url = f'http://ipinfo.io/{ip}/json' if ip else 'http://ipinfo.io/json'
        
        response = requests.get(url)
        data = response.json()
        
        # Ambil informasi yang dibutuhkan
        device_info = {
            "IP": data.get("ip"),
            "Hostname": data.get("hostname"),
            "City": data.get("city"),
            "Region": data.get("region"),
            "Country": data.get("country"),
            "Location": data.get("loc"),  # Latitude and Longitude
            "Org": data.get("org"),  # Organization
            "Postal": data.get("postal"),
            "Timezone": data.get("timezone")
        }

        return device_info
    
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    ip = input("Enter the IP you want to request (leave blank for public IP): ")
    info = get_ip_info(ip)
    print(json.dumps(info, indent=4))
