import json
from datetime import datetime, timedelta

class MetricExplorer:
    def __init__(self):
        stats_file="data/metric/endpoint_stats.json"
        self.aggregated_stats = self.load_data(stats_file)

    def load_data(self, filename):
        with open(filename, 'r') as f:
            return json.load(f)

    def query_endpoint_stats(self, endpoint, time_minute):
        endpoint_data = self.aggregated_stats.get(endpoint, {})
        return endpoint_data.get(time_minute, {})

    def query_endpoint_stats_in_range(self, endpoint, time_minute):
        range_stats = {}
        example_time_minute = datetime.strptime(time_minute, '%Y-%m-%d %H:%M:%S')
        start_time = example_time_minute - timedelta(minutes=15)
        end_time = example_time_minute + timedelta(minutes=5)
        current_time = start_time
        while current_time <= end_time:
            time_minute_str = current_time.strftime('%Y-%m-%d %H:%M:%S')
            if endpoint in self.aggregated_stats:
                range_stats[time_minute_str] = self.aggregated_stats[endpoint].get(time_minute_str, {'calls': 0, 'success_rate': 0, 'error_rate': 0, 'average_duration': 0, 'timeout_rate': 0})
            current_time += timedelta(minutes=1)
        return range_stats

if __name__ == '__main__':
    explorer = MetricExplorer()

    # example_endpoint = "ts-order-other-service-PUT:/api/v1/orderOtherService/orderOther"
    # example_endpoint = "PUT:/api/v1/orderOtherService/orderOther"
    # example_time_minute = "2024-01-09 09:00:00"
    E = "ts-travel-plan-service-/api/v1/routeplanservice/routePlan/quickestRoute"
    T = "2024-01-09 09:00:00"

    stats_in_range = explorer.query_endpoint_stats(E, T)
    print(stats_in_range)

    stats_in_range = explorer.query_endpoint_stats_in_range(E, T)
    print(f"Stats for {E} around {T} (15 time_minutes before and 5 time_minutes after):")
    for time_minute, stats in stats_in_range.items():
        print(f"At {time_minute}: {stats}")
