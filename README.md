[![CI](https://github.com/oversight/httpprobe/workflows/CI/badge.svg)](https://github.com/oversight/httpprobe/actions)
[![Release Version](https://img.shields.io/github/release/oversight/httpprobe)](https://github.com/oversight/httpprobe/releases)

# Oversight HTTP Probe

## Docker build

```
docker build -t httpprobe . --no-cache
```

## Exceptions

If the option `verifySSL` is enabled, and the certificate is *not* valid, then the `SSLCertVerificationError` exception will be raised and the check will fail.

## User testing

[httpstat.us](https://httpstat.us) is an online service for testing various http status code conditions.

Below is a subset of uri's we found useful for testing:

* [200](https://httpstat.us/200) OK
* [301](https://httpstat.us/301) Moved Permanently
* [400](https://httpstat.us/400) Bad Request
* [401](https://httpstat.us/401) Unauthorized
* [402](https://httpstat.us/402) Payment Required
* [403](https://httpstat.us/403)Forbidden
* [404](https://httpstat.us/404) Not Found
