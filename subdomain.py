import os
import requests

def main():
    os.system("clear")
    print('''
█▀ █░█ █▄▄ █▀▄ █▀█ █▀▄▀█ ▄▀█ █ █▄░█
▄█ █▄█ █▄█ █▄▀ █▄█ █░▀░█ █▀█ █  █░▀█

█▀▀ █ █▄░█ █▀▄ █▀▀ █▀█
█▀░ █ █░▀█ █▄▀ ██▄ █▀▄

— coded by NowMeee
> note : dont use http/https on list sites
''')
    api_key = input("Masukan apikey: ")  # Prompt the user for their API key
    domain_list_file = input("Enter File: ")
    output_file = input("Enter output: ")

    with open(domain_list_file, "r") as file:
        domains = file.read().splitlines()

    with open(output_file, "w") as output:
        for domain in domains:
            subdomains = find_subdomains(domain, api_key)
            subdomain_count = len(subdomains)
            
            if subdomain_count == 0:
                print(f"\x1b[31m[{domain} >> {subdomain_count}]\x1b[0m")  # Red text for 0 subdomains
            elif 1 <= subdomain_count <= 20:
                print(f"\x1b[33m[{domain} >> {subdomain_count}]\x1b[0m")  # Yellow text for 1-20 subdomains
            else:
                print(f"\x1b[32m[{domain} >> {subdomain_count}]\x1b[0m")  # Green text for more than 20 subdomains
            if subdomains:
                output.write("\n".join(subdomains) + "\n")
                output.flush()  # Ensure data is written immediately

    print(f"Subdomains found and saved in {output_file}")

def find_subdomains(domain, api_key):
    url = f"https://v1.nomisec07.site/api/subdomain_finder?domain={domain}&apikey={api_key}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            subdomains = data.get("subdomains", [])
            return subdomains
    except Exception:
        pass
    return []

if __name__ == "__main__":
    main()
