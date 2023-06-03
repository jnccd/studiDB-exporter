import argparse
import os
import sys
import time
from pathlib import Path
import os
import csv
from py_linq import *

root_dir = Path(__file__).resolve().parent
copied_path = root_dir / 'copied.txt'
csv_path = root_dir / 'data.csv'

entries = []
with open(copied_path) as f:
    for line in f.readlines():
        trimmed_line = line.removesuffix("\n")
        entry = trimmed_line.split('\t')
        
        if not entry[0].startswith(("WS", "SS")):
            continue
        
        if entry[2] == "5.0":
            entry[3] = "0.0"
        
        entries.append(entry)
        
#print(entries)

entries_e = Enumerable(entries)
sem_stats = entries_e.group_by(key_names=['semester'], key=lambda x: [x[0]]).select(lambda g: { 
    'semester': g.key.semester, 
    'count': g.count(), 
    'avg-grade': str(Enumerable(g).avg(lambda x: float(x[2]))),
    'sum-ects':  str(Enumerable(g).sum(lambda x: float(x[3]))) }).order_by(lambda x: x['semester'].split(' ')[-1]).to_list()

print(sem_stats)

with open(csv_path, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    
    writer.writerow("Semester	Modul	Note	ECTS	Dozent	Scheinart".split("\t"))
    for entry in entries:
        writer.writerow(entry)
        
    writer.writerow([ ])
    writer.writerow(['semester', 'num modules', 'avg grade', 'sum ects'])
    for stat in sem_stats:
        writer.writerow([*stat.values()])
    