import json

with open('mobs_stats.json') as f:
	data = json.load(f)

print(data[0]['rows'])