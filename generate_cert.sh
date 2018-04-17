#!/bin/bash
# Run with SUDO
echo "Enter directory to generate key and cert"
Generate_Key=$1
echo "Enter directory to save key and cert"
Save_Key=$2
cd $HOME
mkdir $Generate_Key
mkdir -p $Save_Key
#   Generate Key
openssl req -new -x509 -days 365 -sha1 -newkey rsa:1024 \
-nodes -keyout server.key -out server.crt \
-subj '/O=Company/OU=Department/CN=127.0.0.1'
#   Generate Certificate
openssl req -new -sha1 -newkey rsa:1024 -nodes \ 
-keyout server.key -out 127.0.0.1.csr \ 
-subj '/O=Company/OU=Department/CN=127.0.0.1'

cd $HOME
mv $Generate_Key $Save_Key