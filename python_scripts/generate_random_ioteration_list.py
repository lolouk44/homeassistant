group_entities = hass.states.get('group.all_lights').attributes['entity_id']
all_lights = []
for e in group_entities: all_lights.append(e)
service_data = {'entity_id': 'input_select.inventory_position','options': all_lights}
hass.services.call('input_select', 'set_options', service_data)