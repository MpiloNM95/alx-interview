#!/usr/bin/python3
"""
Script that reads stdin by line and computes metrics
"""
import sys

status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
line_count = 0
total_size = 0
status_code_counts = {code: 0 for code in status_codes}

def print_statistics():
    print(f"Total file size: {total_size}")
    for code in sorted(status_code_counts):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")
    print()

def process_line(line):
    global line_count, total_size, status_code_counts
    line_count += 1
    if line_count > 10:
        print_statistics()
        line_count = 1
    parts = line.split()
    if len(parts) != 10:
        return
    try:
        code = int(parts[8])
        size = int(parts[9])
    except (ValueError, IndexError):
        return
    total_size += size
    if code in status_code_counts:
        status_code_counts[code] += 1

try:
    for line in sys.stdin:
        process_line(line)

except KeyboardInterrupt:
    pass

print_statistics()

