# Palo Alto Prisma Access Egress IP Retriever

Retrieves various endpoints of a Prisma Access tenant using its [API]([https://docs.paloaltonetworks.com/panorama/10-2/panorama-admin/manage-firewalls/manage-templates-and-template-stacks/override-a-template-setting](https://docs.paloaltonetworks.com/prisma/prisma-access/prisma-access-panorama-admin/prisma-access-overview/retrieve-ip-addresses-for-prisma-access)).

### Usage

```
> python3 prisma_access_addresses.py
Select service type (all | remote_network | gp_gateway | gp_portal | clean_pipe | swg_proxy)
> all
Select address type (all | active | service_ip | auth_cache_service | network_load_balancer)
> all
Select location (all | deployed)
> all
Enter API Key: abcd1234

Europe
198.51.100.2
203.0.113.10
2001:db8:a::100

Global
203.0.113.15
198.51.100.5
2001:db8:100::100
```
                               
### Requirements

- [requests](https://pypi.org/project/requests/) (install with ```pip3 install requests```)

### License

This project is licensed under the [MIT License](LICENSE).
