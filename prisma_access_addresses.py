"""Print Prisma Addresses of tenant"""
import json
import getpass
import requests

API_ENDPOINT = 'https://api.prod.datapath.prismaaccess.com/getPrismaAccessIP/v2'
CONN_TIMEOUT = 10

if __name__ == '__main__':
    print('Select service type (all | remote_network | gp_gateway | gp_portal | clean_pipe | '
          'swg_proxy)')
    SERVICE_TYPE = input()
    print('Select address type (all | active | service_ip | auth_cache_service | '
          'network_load_balancer)')
    ADDRESS_TYPE = input()
    print('Select location (all | deployed)')
    LOCATION = input()
    print('Enter API Key:')
    API_KEY = getpass.getpass()
    fw_req = requests.Session()
    fw_req.verify = True
    fw_req.timeout = CONN_TIMEOUT
    fw_req.headers.update({'header-api-key': API_KEY})
    body_as_dict = {'serviceType': SERVICE_TYPE, 'addrType': ADDRESS_TYPE, 'location': LOCATION}
    response = fw_req.post(API_ENDPOINT, json=body_as_dict)
    response.raise_for_status()
    body_dict = json.loads(response.text)  # json to dict
    for result in body_dict['result']:
        print('')
        print(result['zone'])
        for address in result['addresses']:
            print(address)
        for address6 in result['addresses_v6']:
            print(address6)
