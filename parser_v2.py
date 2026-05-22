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
    parser.add_argument("--output", help="Write summary to file")
    parser.add_argument("--verbose", action="store_true")
    return parser.parse_args()
    
def main():
    args = get_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    lines = read_log(args.input)
    counts = summarise(lines)

    for tag, cnt in counts.items():
        logging.info(f"{tag} : {cnt}")

    if args.output:
        with open(args.output, "w") as f:
            for tag, cnt in counts.items():
                f.write(f"{tag}: {cnt}\n")
        logging.info(f"Summary written to {args.output}")
        
if __name__ == "__main__":
    main()