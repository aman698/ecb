#!/bin/bash

# MySQL credentials
DB_USER="root"
DB_PASS="vrs@123"
DB_NAME="asterisk"

# Directories
SRC_DIR="/var/spool/asterisk/monitor"
DEST_DIR="/home/vrsiis/ftp/upload"
LOG_FILE="/home/vrsiis/ftp/move.log"

# Temporary working directory
cd /tmp || exit 1

# Ensure destination exists
mkdir -p "$DEST_DIR"

# Query recent CDRs (last 10 minutes)
CDRS=$(mysql -u"$DB_USER" -p"$DB_PASS" -D"$DB_NAME" -se "
SELECT 
    DATE_FORMAT(calldate, '%Y%m%d-%H%i%S') AS timestamp,
    src, dst 
FROM cdr 
WHERE calldate >= NOW() - INTERVAL 10 MINUTE;
")

# Loop through each CDR entry and try to move matching .wav file
while read -r timestamp src dst; do
    filename="${timestamp}-${src}-${dst}.wav"
    src_file="${SRC_DIR}/${filename}"

    if [ -f "$src_file" ]; then
        # Double-check file is not being written (optional: 1 sec delay)
        sleep 1

        mv "$src_file" "$DEST_DIR/"
        chmod 644 "$DEST_DIR/$filename"

        echo "$(date '+%Y-%m-%d %H:%M:%S') - Moved $filename to $DEST_DIR" >> "$LOG_FILE"
    fi
done <<< "$CDRS"
