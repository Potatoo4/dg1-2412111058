#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Su dung: $0 <thu_muc_can_sao_luu>"
    exit 1
fi

SOURCE="$1"

if [ ! -d "$SOURCE" ]; then
    echo "Loi: '$SOURCE' khong phai la thu muc."
    exit 2
fi

PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
BACKUP_DIR="$HOME/backup"

mkdir -p "$BACKUP_DIR"

SOURCE_ABS="$(cd "$SOURCE" && pwd)"
NAME="$(basename "$SOURCE_ABS")"
TIMESTAMP="$(date '+%Y%m%d_%H%M%S')"

DEST="$BACKUP_DIR/${NAME}_${TIMESTAMP}.tar.gz"

tar -czf "$DEST" -C "$(dirname "$SOURCE_ABS")" "$NAME"

if [ $? -ne 0 ]; then
    echo "Loi: backup that bai."
    exit 3
fi

echo "$(date '+%Y-%m-%d %H:%M:%S') | $DEST" >> "$PROJECT_ROOT/logs/backup.log"

echo "Backup thanh cong!"
echo "File: $DEST"

exit 
