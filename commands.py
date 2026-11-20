#!/usr/bin/env python3
import re,sys
def route(text):
 s=text.strip().lower()
 if re.search(r"\b(status|health)\b",s):return "status"
 if re.search(r"\b(remember|save note|note this)\b",s):return "memory"
 if re.search(r"\b(dictate|transcribe|voice note)\b",s):return "dictation"
 if re.search(r"\b(create|write|generate)\b.*\b(file|document|script|code)\b",s):return "create_file"
 if re.search(r"\b(ask|explain|tell me|what|how|why)\b",s):return "ask_ai"
 return "general"
if __name__=="__main__":print(route(" ".join(sys.argv[1:])))
