#! /usr/bin/env python

# This is an example script for accessing the Netstorage API.
# The authentication mechanism is as listed in the HTTP API guide for Netstorage.
# This example uses the objectstore version of NetStorage

# Notes: This API does not use standard HTTP methods - POST or PUT are used for
# Write actions and GET is used for reads.  The "Action" header includes the
# Actual information about what the action will be.
import requests
import hashlib
import hmac
from time import time
t = time()
import logging
import base64

# Overall call syntax:
# PUT /[CPCode]/[path]/[file.ext] HTTP/1.1
# Host: [example]-nsu.akamaihd.net
# X-Akamai-ACS-Action: version=1&action=upload
# [Signature Headers (as described on page 13)]
#[PUT body]

import httplib as http_client
http_client.HTTPConnection.debuglevel = 10
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

# Authentication pieces
authdata = "5, 0.0.0.0, 0.0.0.0, %d, %d, kirsten" % (t, t)
signature = base64.b64encode(hmac.new("<api_key>", authdata + "/384473/index.html\n" + "x-akamai-acs-action:version=1&action=upload\n", hashlib.sha256).digest())

payload = "This is a test"

s = requests.Session()
s.headers.update({"X-Akamai-ACS-Action":'version=1&action=upload'})
s.headers.update({"X-Akamai-ACS-Auth-Data":authdata})
s.headers.update({"X-Akamai-ACS-Auth-Sign":signature})
 
req = requests.Request('PUT', <URL>, data=payload)
prepped = s.prepare_request(req)

resp = s.send(prepped)

print resp.status_code

