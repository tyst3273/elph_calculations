#!/bin/bash

/home/ty/anaconda3/bin/python make_stripes.py

cat phonons_template.py model.py > phonons.py
cat polaron_template.py model.py > polaron.py
cat polaron_restart_template.py model.py > polaron_restart.py
cat polaron_nscf_template.py model.py > polaron_nscf.py

/home/ty/research/repos/elph/ELPH.py -i phonons.py polaron.py polaron_restart.py polaron_nscf.py

