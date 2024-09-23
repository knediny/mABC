## 创建方法
python view.py

## 字段解释

```python
{
    "endpointName": "POST:/api/v1/preserveotherservice/preserveOther", # 经过修改后的endpointName，修改方式见view.py:25
    "parent_endpoint_name": "-1", # parent endpoint 的名字，同样经过修改
    "timeout": True, # 判断其是否超时，在筛出的超时数据中，全部超时
    "duration": 8844, # 请求的结束时间减去开始时间
}
```

records -> 加上上述字段 -> records_2 -> 删除所有重复的log -> 将日志中缺失的parent_endpoint_name重定向至-1 -> records_5 -> 对任一服务，如果本次调用(trace)的duration相比其他调用出现异常，认为它超时 -> 对于一次调用，如果当前endpoint超时，则认为它的上层endpoint不超时 -> records_3

```
## 数据位置
onedrive