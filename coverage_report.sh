#!/bin/sh
coverage erase
coverage run test.py --omit="*/.pyenv*,*/__init__*,*/util/*,*/test*,*/model/*,*/exception/*"
coverage report --omit="*/.pyenv*,*/__init__*,*/util/*,*/test*,*/model/*,*/exception/*"
# coverage html --omit="*/.pyenv*,*/__init__*,*/util/*,*/test*,*/model/*,*/exception/*"
# cd htmlcov && python3 -m http.server 8000 --bind 127.0.0.1
