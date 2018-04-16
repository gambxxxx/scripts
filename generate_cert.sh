#!/bin/bash

#   Generate Key
openssl req -new -x509 -days 365 -sha1 -newkey rsa:1024 \
-nodes -keyout server.key -out server.crt \
-subj '/O=Company/OU=Department/CN=www.example.com'
#   Generate Certificate
openssl req -new -sha1 -newkey rsa:1024 -nodes \ 
-keyout server.key -out www.example.com.csr \ 
-subj '/O=Company/OU=Department/CN=www.example.com'
