#!/bin/bash

LOG_FILE="run_analysis.log"
INPUT_DIR="logs"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"
log(){
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

check_dir(){
    if [ -d "$1" ]; then
        log "Directory $1 exists"
    else
        log "Directory $1 not found — creating it"
        mkdir -p "$1"
    fi
}

check_dir "$INPUT_DIR"

log "Running log parser"

python3 parser_v2.py --input build.log --output summary.txt

if [ $? -eq 0 ]; then
    log "Parser finished successfully"
else
    log "Parser failed"
    exit 1
fi

log "Error count by type:"

while IFS= read -r line; do
    log "  $line"
done < summary.txt

log "Done"