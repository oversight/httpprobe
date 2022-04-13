[![CI](https://github.com/oversight/httpprobe/workflows/CI/badge.svg)](https://github.com/oversight/httpprobe/actions)
[![Release Version](https://img.shields.io/github/release/oversight/httpprobe)](https://github.com/oversight/httpprobe/releases)

# Oversight HTTP Probe

## Docker build

```
docker build -t httpprobe . --no-cache
```

## Exceptions

If the option `verifySSL` is enabled, and the certificate is *not* valid, then the `SSLCertVerificationError` exception will be raised and the check will fail.
