# MarkLogic Version Manager (In Python for Linux)

Copyright 2018 Christopher Antila

Subject to the terms of the Apache License, included in the LICENCE file.

Loosely based on the "mlvm" project for macOS: https://github.com/withjam/mlvm


## Install

#. Clone the repository.
#. Create a virtualenv with Python 3.5 or newer.
#. Activate the virtualenv.
#. Run `pip install -r requirements.txt` in this directory.
#. Deactivate the virtualenv.
#. Make a script like this, somewhere in your PATH:

```bash
#!/usr/bin/env bash

sudo /path/to/virtualenv/bin/python /path/to/this/repo/mlvm.py $@
```
