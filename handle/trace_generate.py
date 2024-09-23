import json
import os
from collections import defaultdict
from datetime import datetime
import tqdm


# 文件路径和结果文件夹
file_path = 'data/records_3/ops/records_6.jsonl'
result_folder = 'data/topology/'
if not os.path.exists(result_folder):
    os.makedirs(result_folder)

# 处理文件    
datas = []
endpoint_maps = defaultdict(lambda: defaultdict(list))

with open(file_path, 'r') as file:
    for line in tqdm.tqdm(file):
        data = json.loads(line)
        datas.append(data)

        endpoint = data['endpointName']
        start_time = data['startTime']
        endpoint_upstream = data['parent_endpoint_name']
        
        minute = datetime.fromtimestamp(start_time // 1000).strftime('%Y-%m-%d %H:%M:00')
        endpoint_maps[endpoint_upstream][minute].append(endpoint)

for endpoint, minutes in tqdm.tqdm(endpoint_maps.items()):
    for minute, data_list in minutes.items():
        data_list = set(data_list)
        # 将列表转换为集合去重，再转回列表
        minutes[minute] = list(data_list)

output_file = result_folder + 'endpoint_maps.json'
with open(output_file, 'w') as f:
    json.dump(endpoint_maps, f, indent=4)
