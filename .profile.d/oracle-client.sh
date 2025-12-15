#!/usr/bin/env bash
# Oracle Instant Client Kurulumu (Buildpack için)

# Gerekli Instant Client sürümü
ORACLE_INSTANT_CLIENT_VERSION="23.4.0.0.0"
ORACLE_INSTANT_CLIENT_DIR="/app/.heroku/python/instantclient_${ORACLE_INSTANT_CLIENT_VERSION}"

# Geçici indirme dizini
mkdir -p $ORACLE_INSTANT_CLIENT_DIR

# Instant Client Basic Package'ı indirme (Linux x64 için)
curl -o /tmp/instantclient.zip https://download.oracle.com/otn_software/linux/instantclient/234000/instantclient-basiclite-linux.x64-23.4.0.24.05.zip

# İndirilen dosyayı açma
unzip /tmp/instantclient.zip -d $ORACLE_INSTANT_CLIENT_DIR
rm /tmp/instantclient.zip

# ORACLE INSTANT CLIENT'ın yükleme dizinini PATH'e ekleme
# Bu kısım oracledb kütüphanesinin ihtiyacı
export LD_LIBRARY_PATH=$ORACLE_INSTANT_CLIENT_DIR/instantclient_${ORACLE_INSTANT_CLIENT_VERSION}

# NOT: TNS_ADMIN burada AYARLANMAYACAK. settings.py kullanacak.