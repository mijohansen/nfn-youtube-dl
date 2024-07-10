# Download certificate

```bash 
wget -q  https://raw.githubusercontent.com/luminati-io/luminati-proxy/master/bin/ca.crt

```

Transform

```bash
openssl x509 -inform DER -in ca.crt -out proxy.pem -text


```

```bash
openssl x509 -in ca.crt -out proxy.pem -outform PEM
```