import streamlit as st
import json
from pathlib import Path

DATA_FILE = Path("ip_list.json")

# Load existing IP list
if DATA_FILE.exists():
    ip_list = json.loads(DATA_FILE.read_text())
else:
    ip_list = []

st.title("➕ Add IP Addresses")

new_ip = st.text_input("Enter IP address:")
if st.button("Add"):
    if new_ip and new_ip not in ip_list:
        ip_list.append(new_ip)
        DATA_FILE.write_text(json.dumps(ip_list))
        st.success(f"Added {new_ip}")
    elif new_ip in ip_list:
        st.warning("IP already in the list!")
    else:
        st.error("Please enter a valid IP address")

st.subheader("Current IPs")
for ip in ip_list:
    st.write(ip)
