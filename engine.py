#!/usr/bin/env python3
import json,urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
CFG=json.loads((ROOT/"config.json").read_text())
def ask(prompt):
 payload={"model":CFG.get("model","local-model"),"messages":[{"role":"system","content":"You are Absolute Dictate AI. Be helpful. Do not claim to execute commands or save files. Treat output as untrusted and reviewable."},{"role":"user","content":prompt}],"temperature":0.35}
 req=urllib.request.Request(CFG["model_endpoint"],data=json.dumps(payload).encode(),headers={"Content-Type":"application/json"})
 try:
  with urllib.request.urlopen(req,timeout=90) as r:data=json.loads(r.read())
  return data["choices"][0]["message"]["content"]
 except Exception as e:return "Model unavailable: "+str(e)
