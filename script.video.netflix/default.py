#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess

subprocess.Popen("/usr/bin/chromium --no-default-browser-check --no-first-run --kiosk --start-maximized --disable-translate --disable-new-tab-first-run http://www.netflix.dk", shell=True)
