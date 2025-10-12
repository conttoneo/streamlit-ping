import streamlit as st
import json
import subprocess
import platform
from pathlib import Path

DATA_FILE = Path("ip_list.json")

st.title("🔍 Check IP Status")

# Load stored IP list
if DATA_FILE.exists():
    ip_list = json.loads(DATA_FILE.read_text())
else:
    ip_list = []

def ping(ip):
    """Return True if host responds to ping, else False (fast timeout)."""
    param = "-n" if platform.system().lower() == "windows" else "-c"
    timeout = "-w" if platform.system().lower() == "windows" else "-W"
    try:
        result = subprocess.run(
            ["ping", param, "1", timeout, "1", ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return result.returncode == 0
    except Exception:
        return False

if not ip_list:
    st.warning("No IP addresses found. Please add some first.")
else:
    for ip in ip_list:
        status = ping(ip)
        color = "🟢" if status else "🔴"
        st.write(f"{color} {ip}")
