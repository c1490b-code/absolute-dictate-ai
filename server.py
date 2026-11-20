#!/usr/bin/env python3
import json
from pathlib import Path
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from engine import ask
from memory import add,list_notes
ROOT=Path(__file__).resolve().parents[1]
CFG=json.loads((ROOT/"config.json").read_text())
WORK=(ROOT/CFG["workspace"]).resolve();WORK.mkdir(exist_ok=True)
UI=(ROOT/"web/index.html").read_text()
def out(x):return json.dumps(x,ensure_ascii=False).encode()
class Handler(BaseHTTPRequestHandler):
 def log_message(self,*a):pass
 def send(self,status,data,typ="application/json"):
  self.send_response(status);self.send_header("Content-Type",typ);self.send_header("Content-Length",str(len(data)));self.send_header("X-Content-Type-Options","nosniff");self.end_headers();self.wfile.write(data)
 def body(self):
  n=int(self.headers.get("Content-Length","0"))
  if n>300000:raise ValueError("Request too large")
  return json.loads(self.rfile.read(n) or b"{}")
 def do_GET(self):
  if self.path=="/":return self.send(200,UI.encode(),"text/html; charset=utf-8")
  if self.path=="/api/status":return self.send(200,out({"name":CFG["name"],"version":CFG["version"],"workspace":str(WORK),"endpoint":CFG["model_endpoint"],"voice_available":False,"note_count":len(list_notes())}))
  if self.path=="/api/notes":return self.send(200,out(list_notes()))
  if self.path=="/api/files":return self.send(200,out([str(p.relative_to(WORK)) for p in WORK.rglob("*") if p.is_file()]))
  return self.send(404,out({"error":"Not found"}))
 def do_POST(self):
  try:
   d=self.body()
   if self.path=="/api/ask":return self.send(200,out({"answer":ask(str(d.get("text","")))}))
   if self.path=="/api/note":return self.send(200,out(add(str(d.get("text","")).strip())))
   if self.path=="/api/voice":
    from voice import capture
    return self.send(200,out({"text":capture()}))
   if self.path in ("/api/preview","/api/save"):
    name=str(d.get("name",""));content=str(d.get("content",""));p=(WORK/name).resolve()
    if not name or not p.is_relative_to(WORK):raise ValueError("Invalid path: workspace confinement enforced")
    if len(content.encode())>CFG.get("max_file_bytes",200000):raise ValueError("File too large")
    if self.path=="/api/preview":return self.send(200,out({"name":name,"content":content,"preview_only":True}))
    p.parent.mkdir(parents=True,exist_ok=True);p.write_text(content,encoding="utf8")
    return self.send(200,out({"saved":str(p.relative_to(WORK))}))
   return self.send(404,out({"error":"Not found"}))
  except Exception as e:return self.send(400,out({"error":str(e)}))
if __name__=="__main__":
 print(f"Absolute Dictate AI at http://{CFG['host']}:{CFG['port']}")
 ThreadingHTTPServer((CFG["host"],CFG["port"]),Handler).serve_forever()
