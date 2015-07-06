# create a connection to the node
import pyeapi
node = pyeapi.connect_to('veos01')

# get the instance of the API (in this case vlans)
vlans = node.api('vlans')

# return all vlans from the node
vlans.getall()
{'1': {'state': 'active', 'name': 'default', 'vlan_id': 1, 'trunk_groups': []},
'10': {'state': 'active', 'name': 'VLAN0010', 'vlan_id': 10, 'trunk_groups':
[]}}

# return a specific vlan from the node
vlans.get(1)
{'state': 'active', 'name': 'default', 'vlan_id': 1, 'trunk_groups': []}

# add a new vlan to the node
vlans.create(100)
True

# set the new vlan name
vlans.set_name(100, 'foo')
True
