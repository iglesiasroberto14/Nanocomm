#!/bin/bash

if [ $(hash whois) ]; then
  echo "whois: command not found (apt-install whois)"
  exit 1
fi

DOMAIN=$1

EXPIRE=$(whois $DOMAIN | grep expire | tr '\t' ' ' | tr -s ' ' | cut -d' ' -f2)
TODAY=$(date "+%Y-%m-%d")



DAYS_LEFT=$((($(date -d "$EXPIRE" +%s) - $(date -d "$TODAY" +%s)) / 60 / 60 / 24))

echo $DAYS_LEFT
exit 0
