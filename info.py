import argparse
import whois
import dns.resolver
import requests
import socket

argparse=argparse.ArgumentParser(description="This is a basic tool", usage="python -u info.py -d domain name")
argparse.add_argument("-d","--domain",help="Enter the domain name",required=True)


args=argparse.parse_args()
domain=args.domain



#whois-----
try:
    info=whois.whois(domain)
    print("[+] who is loaded.............")
    for i in info:
        if(i=="status"):
            continue
        else:
            print(f"{i} : {info[i]}")
    
except:
    print("Somthing error")
print("[+]Whois exit...............")


## DNS-----
domain_record_list=["A","AAAA","PTR","NS","MX","SOA","CNAME","TXT"] #DNS all record name list

print("[+]DNS star...........................")
for i in domain_record_list:
    try:
        py=dns.resolver.resolve(domain,i)

        for j in py:
            print(f"{i} record is : {j}")
    except:
        print(f"{i} Recode Not found")
print("[+]DNS exit................................")

#ip location
print("[+] Location info start....................................")
try:
    location_info=requests.get("https://geolocation-db.com/json/50ad4a90-fd5e-11ec-b463-1717be8c9ff1/"+socket.gethostbyname(domain)).json()
    for i in location_info:
        print(f"{i} : {location_info[i]}")
except:
    print("Location Info not found")
print("[+]Location info End........................")

#sub domain-----------------
user_input=input("Do you want to find subdomain[y/n]: ")
if(user_input == "y" or user_input == "Y"):
    print("[+] Subdomain find start..........")
    f=open("domainWordList.txt","r")
    all_domain_name=f.read()
    domainWordList=all_domain_name.splitlines()
    f.close()

    for subdomain in domainWordList:
        url1=f"http://{subdomain}.{domain}"
        url2=f"https://{subdomain}.{domain}"
        try:
            requests.get(url1)
            print(f"Discover subdomain : {url1}")
        except:
            pass
    
        try:
            requests.get(url2)
            print(f"Discover subdomain : {url2}")
        except:
            pass
else:
    print("Thnq")
print("[+] Subdomain Find End....................")