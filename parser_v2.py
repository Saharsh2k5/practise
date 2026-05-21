from collections import Counter
import argparse
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO,format='%(levelname)s |  %(message)s')

# read_log     → opens any file safely, handles missing files
# summarise    → classifies and counts log lines by tag  
# get_args     → CLI interface, --input flag
# main         → wires it together
# logging      → professional output control

def read_log(filepath):
    if not Path(filepath).exists():
        logging.error(f"Error: file '{filepath}' not found")
        exit(1)
    with open(filepath,'r') as f:
        return f.readlines()

def summarise(lines):
    tags=["INFO","WARNING","ERROR"]
    counter=Counter()
    for line in lines:
        for tag in tags:
            if tag in line:
                counter[tag]+=1
                break
            
    return counter
    
def get_args():
    parser = argparse.ArgumentParser(description="Build log analyser")
    parser.add_argument("--input", required=True, help="Path to log file")
    return parser.parse_args()
    
def main():
    args = get_args()
    lines = read_log(args.input)
    counts=summarise(lines)
    for tag,cnt in counts.items():
        logging.info(f"{tag} : {cnt}")
        
main()