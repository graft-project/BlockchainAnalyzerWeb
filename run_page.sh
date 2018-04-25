#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

nohup python $DIR/run.py &> $DIR/block_analyzer.log &
