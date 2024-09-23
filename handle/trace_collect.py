import json
from datetime import datetime, timedelta

class TraceExplorer:
    def __init__(self):
        files = '/root/work/ops/data/topology/endpoint_maps.json'
        self.endpoint_maps = self.load_data(files)

    def load_data(self, filename):
        with open(filename, 'r') as f:
            return json.load(f)

    def get_endpoint_downstream(self, endpoint, time_minute):
        t = self.endpoint_maps.get(endpoint, {})
        return t.get(time_minute, {})

    def get_endpoint_downstream_in_range(self, endpoint, time_minute):
        range_stats = {}
        example_time_minute = datetime.strptime(time_minute, '%Y-%m-%d %H:%M:%S')
        start_time = example_time_minute - timedelta(minutes=15)
        end_time = example_time_minute + timedelta(minutes=5)
        current_time = start_time
        while current_time <= end_time:
            time_minute_str = current_time.strftime('%Y-%m-%d %H:%M:%S')
            if endpoint in self.endpoint_maps:
                range_stats[time_minute_str] = self.endpoint_maps[endpoint].get(time_minute_str, [])
            current_time += timedelta(minutes=1)
        return range_stats

if __name__ == '__main__':
    explorer = TraceExplorer()

    # example_endpoint = "ts-order-other-service-PUT:/api/v1/orderOtherService/orderOther"
    # example_endpoint = "PUT:/api/v1/orderOtherService/orderOther"
    # example_time_minute = "2024-01-09 09:00:00"
    E = "ts-travel-plan-service-/api/v1/routeplanservice/routePlan/quickestRoute"
    T = "2024-01-09 09:00:00"

    stats_in_range = explorer.get_endpoint_downstream(E, T)
    print(stats_in_range)

    stats_in_range = explorer.get_endpoint_downstream_in_range(E, T)
    print(stats_in_range)
    # print(f"Stats for {E} around {T} (15 time_minutes before and 5 time_minutes after):")
    # for time_minute, stats in stats_in_range.items():
    #     print(f"At {time_minute}: {stats}")