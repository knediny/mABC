import json
import math
import copy

# 2 + 3 => 4

RECORDS_2_PATH = "/root/work/ops/data/records_3/ops/records_5.jsonl"
RECORDS_2_PART_NUM = 1
RECORDS_3_PATH = "/root/work/ops/data/records_3/ops/records_3.jsonl"
RECORDS_4_PATH = "/root/work/ops/data/records_3/ops/records_4.jsonl"

if __name__=="__main__":
    records_2_count = 0
    with open(RECORDS_2_PATH,"r",encoding="utf-8") as records_2:
        for line in records_2:
            records_2_count+=1
    print(f"records_2_count: {records_2_count}")

    timeout_seg_span_id_dict ={} #也就是 new_span_id 的 dict
    with open(RECORDS_3_PATH,"r",encoding="utf-8") as records_3:
        for line in records_3:
            span = json.loads(line)
            timeout_seg_span_id_dict[span["new_span_id"]] = 1
    print(f"records_3_count: {len(timeout_seg_span_id_dict)}")

    chunk_size = math.ceil(records_2_count / RECORDS_2_PART_NUM)
    with open(RECORDS_2_PATH,"r",encoding="utf-8") as records_2:
        chunk = []
        chunk_index = 0
        for line in records_2:
            span = json.loads(line)
            chunk.append(span)
            if len(chunk) % chunk_size == 0:
                chunk.sort(key=lambda span:span["traceId"])
                with open(f"records_2_sorted_part_{chunk_index}.jsonl","w",encoding="utf-8") as output:
                    for span in chunk:
                        output.write(f"{json.dumps(span,ensure_ascii=False)}\n")
                chunk = []
                chunk_index += 1
        if len(chunk) != 0:
            chunk.sort(key=lambda span:span["traceId"])
            with open(f"records_2_sorted_part_{chunk_index}.jsonl","w",encoding="utf-8") as output:
                for span in chunk:
                    output.write(f"{json.dumps(span,ensure_ascii=False)}\n")
            chunk = []
            chunk_index += 1

    actual_chunk_num = chunk_index
    chunk_files = []
    for i in range(actual_chunk_num):
        chunk_files.append(open(f"records_2_sorted_part_{i}.jsonl","r",encoding="utf-8"))
    
    # 合并
    cur_spans = [json.loads(chunk_file.readline()) for chunk_file in chunk_files] # 每个文件至少有一行数据
    with open(f"records_2_sorted.jsonl","w",encoding="utf-8") as output:
        while len(chunk_files) > 0:
            min_index = cur_spans.index(min(cur_spans,key=lambda span:span["traceId"]))
            output.write(f"{json.dumps(cur_spans[min_index], ensure_ascii=False)}\n")
            new_line = chunk_files[min_index].readline()
            if new_line == "":
                chunk_files.pop(min_index).close()
                cur_spans.pop(min_index)
            else:
                new_span = json.loads(new_line)
                cur_spans[min_index] = new_span
    
    # 在一个 traceid 下构建树，并标记timeout
    def _get_tree(span_list):
        span_list = copy.deepcopy(span_list)
        seg_span_id_dict = {}
        for span in span_list:
            span["children"] = []
            span["timeout"] = False
            new_span_id = f"{span['segmentId']}-{span['spanId']}"
            seg_span_id_dict[new_span_id] = span
            if new_span_id in timeout_seg_span_id_dict:
                span["timeout"] = True
        
        root_spans = []
        for span in span_list:
            if span["parentSpanId"]==-1 and len(span['refs']):
                new_parent_span_id=f"{span['refs'][0]['parentSegmentId']}-{span['refs'][0]['parentSpanId']}"
            else:
                new_parent_span_id=f"{span['segmentId']}-{span['parentSpanId']}"

            if '--1' not in new_parent_span_id:
                if new_parent_span_id not in seg_span_id_dict:
                    print(f"warn: nonexist parent seg span id {new_parent_span_id}")
                    root_spans.append(span)
                else:
                    seg_span_id_dict[new_parent_span_id]["children"].append(span)
            else:
                root_spans.append(span)
        
        def _mark_timeout(span):
            for child in span["children"]:
                _mark_timeout(child)
                if child["timeout"]:
                    span["timeout"] = True
            return
        
        for root_span in root_spans:
            _mark_timeout(root_span)
        return root_spans
    
    cur_trace_spans = []
    cur_trace_id = ""
    with open(f"records_2_sorted.jsonl","r",encoding="utf-8") as records_2_sorted:
        with open(RECORDS_4_PATH,"w",encoding="utf-8") as output:
            for line in records_2_sorted:
                span = json.loads(line)
                if cur_trace_id != span["traceId"]:
                    if len(cur_trace_spans)>0:
                        trees = _get_tree(cur_trace_spans)
                        for tree in trees:
                            output.write(f"{json.dumps(tree,ensure_ascii=False)}\n")

                    cur_trace_id = span["traceId"]
                    cur_trace_spans = [span]
                else:
                    cur_trace_spans.append(span)

            if len(cur_trace_spans)>0:
                trees = _get_tree(cur_trace_spans)
                for tree in trees:
                    output.write(f"{json.dumps(tree,ensure_ascii=False)}\n")