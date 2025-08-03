import mysql.connector
import subprocess
from datetime import datetime

# === Database Configuration ===
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "vrs@123",
    "database": "asterisk"
}

# === Asterisk Configuration File ===
SIP_CONF_PATH = "/etc/asterisk/sip_custom.conf"

def fetch_users():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM sip_users ORDER BY name")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return users

def write_sip_conf(users):
    with open(SIP_CONF_PATH, 'w') as f:
        for user in users:
            f.write(f"\n[{user['name']}]\n")
            f.write(f"type={user.get('type', 'friend')}\n")
            f.write(f"host={user.get('host', 'dynamic')}\n")
            f.write(f"secret={user['secret']}\n")
            f.write(f"context={user.get('context', 'internal')}\n")
            f.write(f"dtmfmode={user.get('dtmfmode', 'rfc2833')}\n")
            f.write(f"nat={user.get('nat', 'yes')}\n")
            f.write(f"disallow={user.get('disallow', 'all')}\n")
            f.write(f"allow={user.get('allow', 'ulaw,alaw')}\n")
            f.write(f"qualify={user.get('qualify', 'yes')}\n")
            f.write(f"canreinvite={user.get('canreinvite', 'no')}\n")

    print(f"[{datetime.now()}] sip_custom.conf rewritten with {len(users)} user(s)")

def reload_asterisk_sip():
    try:
        subprocess.run(["sudo", "asterisk", "-rx", "sip reload"], check=True)
        print(f"[{datetime.now()}] Asterisk SIP config reloaded.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to reload Asterisk: {e}")

if __name__ == "__main__":
    users = fetch_users()
    write_sip_conf(users)
    reload_asterisk_sip()
