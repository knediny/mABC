import inspect
import copy

from copy import deepcopy
from dataclasses import dataclass, InitVar, field

from functools import reduce, partial, wraps
import json
import logging
import numpy as np
import os
import pathlib
import json
logging.basicConfig(level=getattr(logging, os.environ.get('LOG_LEVEL','INFO').upper()))
import tqdm

def preetify_endpoint_Name(s):
    return s
    splits = s.split('/')
    splits = [s for s in splits if ' ' not in s and '-' not in s]
    return '/'.join(splits)

records = [json.loads(l.strip()) for l in open('data/meta/span_info_0109.jsonl').readlines()]

min_time = min([r['startTime'] for r in records])

segment_id_span_to_endpoint_name={}
for record in records:
    segment_id_span_to_endpoint_name[f"{record['segmentId']}-{record['spanId']}"] = preetify_endpoint_Name(record['endpointName'])

stats={}
records_2 = []
for record in tqdm.tqdm(records):
    record_2={}
    record_2.update(record)
    record_2.update({
        "new_span_id": f"{record['segmentId']}-{record['spanId']}",
        "new_parent_span_id": f"{record['segmentId']}-{record['parentSpanId']}",
        "duration": record['endTime']-record['startTime'],
        "endpointName": preetify_endpoint_Name(record['endpointName']),
    })
    if record["parentSpanId"]==-1 and len(record['refs']):
        record_2["new_parent_span_id"]=f"{record['refs'][0]['parentSegmentId']}-{record['refs'][0]['parentSpanId']}"
    if '--1' not in record_2['new_parent_span_id']:
        if record_2['new_parent_span_id'] in segment_id_span_to_endpoint_name:
            record_2['parent_endpoint_name'] = segment_id_span_to_endpoint_name[record_2['new_parent_span_id']]
            stats['A'] = stats.get('A',0)+1
        else:
            record_2['parent_endpoint_name'] = "-2"
            stats['B'] = stats.get('B',0)+1
    else:
        record_2['parent_endpoint_name'] = "-1"
        stats['C'] = stats.get('C',0)+1
    records_2.append(record_2)

tmp=set([str(r) for r in records_2])
tmp_2 = [eval(r) for r in tmp]
records_4 =tmp_2

tmp = set([f"{r['traceId']}-{r['endpointName']}" for r in records_4])
records_5=[]
for r in tqdm.tqdm(records_4):
    if f"{r['traceId']}-{r['parent_endpoint_name']}" in tmp:
        records_5.append(r)
    else:
        r = copy.deepcopy(r)
        r["parent_endpoint_name"]= "-1"
        records_5.append(r)



os.makedirs('/root/work/ops/data/records_3/ops',exist_ok=True)
fout = open('/root/work/ops/data/records_3/ops/records_5.jsonl','w')
for r in records_5:
    fout.write(json.dumps(r,ensure_ascii=False))
    fout.write('\n')
fout.close()

records_5_by_endpoints = {}
for record in  tqdm.tqdm(records_5):
    r = record
    if r['endpointName'] not in records_5_by_endpoints:
        records_5_by_endpoints[ r['endpointName']] = {'records':[]}
    records_5_by_endpoints[r['endpointName']]['records'].append(r)


# filtering out the non-cause spans
timeout_free = {}
# i, endpoint_name = 13,[*records_5_by_endpoints.keys()][13]
for i, endpoint_name in enumerate(records_5_by_endpoints):
    durations = sorted([r['duration']+5 for r in records_5_by_endpoints[endpoint_name]['records']])
    rates = [-1]+[ durations[i]/durations[i-1] for i in range(1,len(durations))]
    max_rates = max(rates)
    max_rates_index = rates.index(max_rates)
    threshold_duration = durations[max_rates_index]
    if max_rates <3:
        import math
        threshold_duration = math.inf
    threshold_duration=max(threshold_duration,1000)
    threshold_duration = 100
    for r in records_5_by_endpoints[endpoint_name]['records']:
        r['timeout']=r['duration']>=threshold_duration
        if r['timeout'] and r['parent_endpoint_name']!='-1':
            p = r['parent_endpoint_name']
            if p not in timeout_free:
                timeout_free[p] = []
            timeout_free[p].append(r['traceId'])
timeout_free_2={k:set(v) for k,v in timeout_free.items()}
records_3 = []
tqdm_context = tqdm.tqdm(total=sum([len(records_5_by_endpoints[e]['records']) for e in records_5_by_endpoints]))
stats={}
for i, endpoint_name in enumerate(records_5_by_endpoints):
    for r in records_5_by_endpoints[endpoint_name]['records']:
        tqdm_context.update(1)
        if not r['timeout']:
            stats['C'] = stats.get('C',0)+1
            continue
        if endpoint_name in timeout_free and r['traceId'] in timeout_free_2[endpoint_name]:
            stats['A'] = stats.get('A',0)+1
        else:
            stats['B'] = stats.get('B',0)+1
            records_3.append(r)
tqdm_context.close()
fout = open('/root/work/ops/data/records_3/ops/records_3.jsonl','w')
for r in records_3:
    fout.write(json.dumps(r,ensure_ascii=False))
    fout.write('\n')
fout.close()



# filtering based on cnt of endpointname
tmp = {}
for c in records_3:
    s = f"{c['endpointName']}"
    if s not in tmp:
        tmp[s]={
            'cnt':0,
            'min_start_time':math.inf,
            'max_start_time':-1,
            'min_duration':math.inf,
            'records':[]
        }
    tmp[s]['cnt']+=1
    tmp[s]['min_start_time']=min(tmp[s]['min_start_time'],c['startTime'])
    tmp[s]['max_start_time']=max(tmp[s]['max_start_time'],c['startTime'])
    tmp[s]['min_duration']=min(tmp[s]['min_duration'],c['duration'])
    tmp[s]['records'].append(c)
for s in tmp:
    tmp[s]['duration'] = tmp[s]['max_start_time']-tmp[s]['min_start_time']
records_by_endpoint = tmp

[x['cnt'] for x in records_by_endpoint.values()]
os.system('rm -rf /root/work/ops/data/records_3/opsfigs/')
os.makedirs('/root/work/ops/data/records_3/opsfigs/',exist_ok=True)
for i,e in enumerate(tmp):
    import matplotlib
    matplotlib.use('Agg')  # Use the non-interactive backend 'Agg'
    from matplotlib import pyplot as plt
    plt.figure()
    plt.scatter([(r['startTime']-min_time)/1000/60 for r in tmp[e]['records']], [r['duration'] for r in tmp[e]['records']])
    plt.savefig(f"/root/work/ops/data/records_3/opsfigs/{i}_scatter.png")

    plt.figure()
    plt.hist([(r['startTime']-min_time)/1000/60 for r in tmp[e]['records']])
    plt.savefig(f"/root/work/ops/data/records_3/opsfigs/{i}_hist.png")
