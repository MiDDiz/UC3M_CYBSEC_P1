import sys
import statistics

def get_sec(time_str):
    """Get seconds from time."""
    d, h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

piped_input = sys.stdin.read()
splitted_lines = piped_input.split('\n')
stripped_splitted_input = [str_time[:str_time.find(' ')] for str_time in splitted_lines] # ['0:00:00:01', '0:00:00:02', ...]
processed_input = [get_sec(time_str) for time_str in stripped_splitted_input[:-1]] # last element is garbage. [1, 2, 2, ..]

secs_list = []
for elem in processed_input:
    prev = processed_input[len(secs_list) - 1] if len(secs_list) > 0 else 0
    secs_list.append(elem - prev)
print(secs_list)
print(processed_input)

print(f"Mean: {statistics.mean(secs_list)}")
print(f"Median: {statistics.median(secs_list)}")
print(f"Percentage Cracked: {len(secs_list)/100.0 * 100}%")