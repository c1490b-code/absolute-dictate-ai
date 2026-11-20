#!/usr/bin/env python3
import json
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def add(text):
 (ROOT/"data").mkdir(exist_ok=True)
 entry={"time":datetime.now(timezone.utc).isoformat(),"text":text}
 with (ROOT/"data"/"memory.jsonl").open("a",encoding="utf8") as f:f.write(json.dumps(entry,ensure_ascii=False)+"\n")
 return entry
def list_notes():
 p=ROOT/"data"/"memory.jsonl"
 return [json.loads(x) for x in p.read_text().splitlines() if x.strip()] if p.exists() else []
