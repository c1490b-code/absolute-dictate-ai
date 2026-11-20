#!/usr/bin/env bash
set -eu
cd "$(dirname "$0")"
python3 install.py
chmod +x start.sh bin/dictate
echo "Install complete. Run ./start.sh"
