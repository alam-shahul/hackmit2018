#!/bin/bash

COUNTDOWN_LIMIT=$1

python ui.py &
python main.py 100 &
