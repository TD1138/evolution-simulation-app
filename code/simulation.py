import json

from organism import organism
from food import food

# import ipdb; ipdb.set_trace()

with open('code/environment_config.json', 'r') as json_file:
    environment_config = json.load(json_file)

organisms = []

for org_id in range(environment_config['initial_organisms']):
    organisms.append(organism(environment_config, wih_init, who_init, name='org_'+str(org_id).zfill(3)))