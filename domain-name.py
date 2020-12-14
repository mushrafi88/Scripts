from urllib.parse import urlparse
import sys
def extract_domain(url, remove_http=True):
    uri = urlparse(url)
    if remove_http:
        domain_name = f"{uri.netloc}"
    else:
        domain_name = f"{uri.netloc}://{uri.netloc}"
    return domain_name
url =  sys.argv[1]
#print("Original: ", url)
print(extract_domain(url))
