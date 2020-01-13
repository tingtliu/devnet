import syslog
import json
from cli import *


target_routes = ["1.1.1.1/32","2.2.2.2/32","3.3.3.3/32"]
current_routes=json.loads(clid('show ip route'))
i = 0
route_list=[]
for route in current_routes['TABLE_vrf']['ROW_vrf']['TABLE_addrf']['ROW_addrf']['TABLE_prefix']['ROW_prefix']:
	route_str =str(route['ipprefix'])
	route_join = '' .join(route_str)
	route_list.insert(i,route_join)
	i = i + 1

if route_list == target_routes:
	syslog.syslog(3, 'We got 3 routes , mission completed!!!')



