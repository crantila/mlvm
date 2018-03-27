# MarkLogic Version Manager (In Python for Linux)

Copyright 2018 Christopher Antila

Subject to the terms of the Apache License, included in the LICENCE file.

Loosely based on the "mlvm" project for macOS: https://github.com/withjam/mlvm


## Install

1. Clone the repository.
1. Create a virtualenv with Python 3.5 or newer.
1. Activate the virtualenv.
1. Run `pip install -r requirements.txt` in this directory.
1. Deactivate the virtualenv.
1. Make a script like this, somewhere in your PATH:

```bash
#!/usr/bin/env bash

sudo /path/to/virtualenv/bin/python /path/to/this/repo/mlvm.py $@
```
