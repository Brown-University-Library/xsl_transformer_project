import json, os


README_URL = "https://github.com/Brown-University-Library/xsl_transformer_project/blob/master/README.md"

LEGIT_IPS_KEYS = json.loads( os.environ['XSL__LEGIT_IPS_KEYS_JSON'] )

"""
example XSL__LEGIT_IPS_KEYS_JSON setting (see your ip and get a random key at `http://host/xsl_transformer/keymaker/`):

export XSL__LEGIT_IPS_KEYS_JSON='
    {
      "label_a": {
        "ip_auth_key": "some_key_a",
        "legit_ip": "some_ip_a"
      },
      "label_b": {
        "ip_auth_key": "some_key_b",
        "legit_ip": "some_ip_b"
      }
    }
    '
"""

WHITELISTED_HOSTS = json.loads( os.environ['XSL__WHITELISTED_HOSTS_JSON'] )

SAXON_CLASSPATH = os.environ['XSL__SAXON_CLASSPATH']
