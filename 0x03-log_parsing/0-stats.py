#!/usr/bin/python3
"""
A script that reads stdin by line and computes metrics
"""
import sys


line_count = 0
total_size = 0
status_code_counts = {}


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
    except ValueError:
        return
    total_size += size
    status_code_counts[code] = status_code_counts.get(code, 0) + 1

try:
    for line in sys.stdin:
        process_line(line)


except KeyboardInterrupt:
    pass


print_statistics()

if __name__ == '__main__':
