#!/bin/bash
# Run with SUDO
echo "Enter directory to generate key and cert"
read $1
echo "Enter directory to save key and cert"
read $2
cd $HOME
mkdir $1
mkdir -p $2
#   Generate Key
openssl req -new -x509 -days 365 -sha1 -newkey rsa:1024 \
-nodes -keyout server.key -out server.crt \
-subj '/O=Company/OU=Department/CN=127.0.0.1'
#   Generate Certificate
openssl req -new -sha1 -newkey rsa:1024 -nodes \ 
-keyout server.key -out www.example.com.csr \ 
-subj '/O=Company/OU=Department/CN=127.0.0.1'

cd $HOME
mv $1 $2