#!/bin/bash

scp -P 65000 out/so_intimate_40_small*.png deploy@localhost:/home/deploy/devel/mar/neural-style/in/
scp -P 65000 out/comp5_081*.png deploy@localhost:/home/deploy/devel/mar/neural-style/in/
