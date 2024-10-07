import requests

# Configuration settings


application_host = "virtualhost"
application_port = 3333
application_path = "/hello"


def get_connectivity_service_token(client_id, client_secret, token_service_url):
    """function to get a token from a oauth endpoint"""
    token_response = requests.post(url=token_service_url, params={'grant_type': 'client_credentials'}, auth=(client_id, client_secret))
    
    if token_response.status_code != 200:
        print(token_response.status_code, token_response.text)  # issue retrieving the auth token - likely credentials issue
        exit(-1)

    jwt = token_response.json()['access_token']
    return jwt


def example_http_request(application_host, application_port, application_path, auth_token, location_id, proxy_host):
    r = requests.get(f"http://{application_host}:{application_port}{application_path}",
            headers={"proxy-authorization": "Bearer " + auth_token,
                    "SAP-Connectivity-SCC-Location_ID": location_id},
            proxies={'http': proxy_host},
            verify=False)
    return r


token_service_url = connectivity_service_key['token_service_url'] + "/oauth/token"
client_id = connectivity_service_key['clientid']
client_secret = connectivity_service_key['clientsecret']
proxy_host = "http://" + connectivity_service_key["onpremise_proxy_host"] + ":" + connectivity_service_key["onpremise_proxy_port"]

token = get_connectivity_service_token(client_id, client_secret, token_service_url)
req = example_http_request(application_host, application_port, application_path, token, "FELIXLAPTOP", proxy_host)
print(req.content)
print("script done")



