#!/usr/bin/env python3
'''Module to read stdin line by line and computes metrics.
'''
import sys
import re


def process_line(line):
    '''Process a line and extract relevant information'''
    pt = re.compile(
             r'(\d+\.\d+\.\d+\.\d+) - \[.*\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)'
    )
    match = pt.match(line)
    if match:
        ip_address, stat_code, file_size = match.groups()
        return ip_address, int(stat_code), int(file_size)
    else:
        return None


def print_statistics(total_size, stat_counts):
    '''Print computed statistics'''
    print(f'Total file size: {total_size}')

    for stat_code in sorted(stat_counts.keys()):
        print(f'{stat_code}: {stat_counts[stat_code]}')


def main():
    total_size = 0
    stat_counts = {}

    try:
        for line_number, line in enumerate(sys.stdin, start=1):
            data = process_line(line)
            if data:
                _, stat_code, file_size = data
                total_size += file_size
                stat_counts[stat_code] = stat_counts.get(stat_code, 0) + 1

            if line_number % 10 == 0:
                print_statistics(total_size, stat_counts)

    except KeyboardInterrupt:
        print_statistics(total_size, stat_counts)


if __name__ == "__main__":
    main()
