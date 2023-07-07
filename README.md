# Palo Alto Prisma Access IP to EDL

Retrieves various endpoints of a Prisma Access tenant using its [API](https://docs.paloaltonetworks.com/prisma/prisma-access/prisma-access-panorama-admin/prisma-access-overview/retrieve-ip-addresses-for-prisma-access) and outputs as text-based IP list to be ingested by a firewall.

### Usage

```
usage: prisma_ip_to_edl.py [-h] [-s SERVICE_TYPE] [-a ADDRESS_TYPE] [-l LOCATION] [-k KEY] [-c KEY_FILE] [-n] [-2]
                           [-x {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
                           output

Print Prisma Access endpoints of tenant in IP list format

positional arguments:
  output                Output file name

options:
  -h, --help            show this help message and exit
  -s SERVICE_TYPE, --service-type SERVICE_TYPE
                        Service type can be one of (all | remote_network | gp_gateway | gp_portal | clean_pipe |
                        swg_proxy). Default: all
  -a ADDRESS_TYPE, --address-type ADDRESS_TYPE
                        Address type can be one of (all | active | service_ip | auth_cache_service |
                        network_load_balancer). Default: all
  -l LOCATION, --location LOCATION
                        Location can be one of (all | deployed) Default: all
  -k KEY, --key KEY     The API key if not reading it from file
  -c KEY_FILE, --key-file KEY_FILE
                        Optional. Location of the file with the API key
  -n, --no-comments     Omit address details in output file
  -2, --endpoint2       Use the alternative endpoint prod6
  -x {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --debug-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        Logging message verbosity. Default: WARNING
```
                               
### Requirements

- [requests](https://pypi.org/project/requests/) (install with ```pip3 install requests```)

### License

This project is licensed under the [MIT License](LICENSE).
