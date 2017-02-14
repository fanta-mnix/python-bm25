#!/usr/bin/env bash

pip install -r requirements.txt && python -c "import nltk; nltk.download('mac_morpho'); nltk.download('punkt')"
