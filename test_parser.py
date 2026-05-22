import pytest
from parser_v2 import summarise

def test_empty_file():
    lines = []
    result = summarise(lines)
    # what should result contain?
    assert result['ERROR'] == 0
    assert result['INFO'] == 0
    assert result['WARNING'] == 0

def test_only_errors():
    lines = ["[ERROR] something failed\n", "[ERROR] another failure\n"]
    result = summarise(lines)
    # what should result contain?
    assert result["INFO"] == 0
    assert result['WARNING'] == 0
    assert result["ERROR"] == len(lines)

def test_mixed_lines():
    lines = [
        "[INFO] starting\n",
        "[ERROR] failed\n",
        "[WARNING] slow\n",
        "[INFO] done\n"
    ]
    result = summarise(lines)
    # what should result contain?
    assert result["INFO"]==2 
    assert result["ERROR"]==1 
    assert result["WARNING"]==1 
     