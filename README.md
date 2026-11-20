# Absolute Dictate AI

Local-first voice assistant for Termux Android and Linux, designed to integrate with PERFECT-OS, LUX and N7.

## Install (Termux)

```bash
pkg update -y && pkg install -y python termux-api
cd ~/PERFECT-OS/projects # or choose another location
# Extract this archive into ~/PERFECT-OS/absolute-dictate-ai
cd ~/PERFECT-OS/absolute-dictate-ai
./install.sh
./start.sh
```
Visit http://127.0.0.1:8768. If no model server is running, dictation and notes still work.

## Linux/Debian
Install Python 3.10+, extract, run `./install.sh` then `./start.sh`. Native Termux voice requires Android/Termux; browser speech recognition is optional and browser-dependent.

## Capabilities
- Native Termux speech-to-text bridge
- Browser speech API (if supported)
- Local OpenAI-compatible model endpoint
- Notes journal, transcript log, file workspace
- File preview and explicit save confirmation
- Workspace path confinement; no shell execution
- Diagnostic/status and basic command routing

Configure `config.json`. Generated content is untrusted and should be reviewed. Server binds to localhost by default.
