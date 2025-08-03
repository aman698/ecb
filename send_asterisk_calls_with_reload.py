import socket
import time
import os
import re
import subprocess

# ========== CONFIG ==========
AST_LOG = "/var/log/asterisk/full"  # Asterisk log file
SERVER_IP = "192.168.2.11"          # Your receiving server IP
SERVER_PORT = 5566                  # Port number to send data to
# ============================

def send_to_socket(message):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((SERVER_IP, SERVER_PORT))
            s.sendall(message.encode('utf-8'))
    except Exception as e:
        print(f"[Socket Error] {e}")

def reload_sip_config():
    try:
        subprocess.run(["sudo", "asterisk", "-rx", "sip reload"], check=True)
        print("🔄 Asterisk SIP config reloaded.")
    except subprocess.CalledProcessError as e:
        print(f"[Reload Error] {e}")

def tail_file(filepath):
    with open(filepath, 'r') as f:
        f.seek(0, os.SEEK_END)
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.2)
                continue
            yield line.strip()

def filter_and_send(line):
    if not line:
        return

    # Match 1: Call start (NoOp with Call from)
    if re.search(r'Executing \[\d+@internal:\d+\] NoOp\("SIP/.*?", "Call from .*? <\d+> to \d+"\)', line):
        send_to_socket(f"[CALL START] {line}")
    
    # Match 2: DISPOSITION (Busy, No Answer, etc.)
    elif re.search(r'DISPOSITION=(NOANSWER|BUSY|ANSWERED|FAILED)', line):
        send_to_socket(f"[DISPOSITION] {line}")

    # Match 3: Answered
    elif re.search(r'SIP/\d+-\w+ answered SIP/\d+-\w+', line):
        send_to_socket(f"[ANSWERED] {line}")

    # Match 4: Call End
    elif re.search(r'Spawn extension \(internal, \d+, \d+\) exited non-zero', line):
        send_to_socket(f"[CALL END] {line}")
        reload_sip_config()  # Optional: only reload after call ends

if __name__ == "__main__":
    print("🔍 Watching Asterisk log for specific call events...")
    for log_line in tail_file(AST_LOG):
        filter_and_send(log_line)
