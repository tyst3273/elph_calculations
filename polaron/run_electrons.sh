#!/bin/bash

/home/ty/anaconda3/bin/python make_stripes.py

cat scf_template.py model.py > scf.py
cat restart_template.py model.py > restart.py
cat nscf_template.py model.py > nscf.py

/home/ty/research/repos/elph/ELPH.py -i scf.py restart.py nscf.py
