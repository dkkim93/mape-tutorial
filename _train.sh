#!/bin/bash

# Load python virtualenv
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt

# Add PYTHONPATH
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export PYTHONPATH=$DIR/thirdparty/multiagent-particle-envs:$PYTHONPATH

# Begin experiment
for SEED in {1..1}
do
    python3 main.py \
    --seed $SEED \
    --env-name "simple_spread" \
    --prefix ""
done
