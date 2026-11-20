#!/usr/bin/env python3
import subprocess,sys,json
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def capture():
 p=subprocess.run(["termux-speech-to-text"],capture_output=True,text=True,timeout=180)
 if p.returncode: raise RuntimeError(p.stderr.strip() or "Speech capture failed")
 transcript=p.stdout.strip()
 if not transcript: raise RuntimeError("No speech recognized")
 (ROOT/"data").mkdir(exist_ok=True)
 with (ROOT/"data"/"dictation.jsonl").open("a",encoding="utf8") as f:f.write(json.dumps({"time":datetime.now(timezone.utc).isoformat(),"text":transcript},ensure_ascii=False)+"\n")
 return transcript
if __name__=="__main__":
 try:print(capture())
 except FileNotFoundError:print("Missing Termux:API. Install app and pkg termux-api.",file=sys.stderr);sys.exit(1)
 except Exception as e:print("Voice error:",e,file=sys.stderr);sys.exit(1)
