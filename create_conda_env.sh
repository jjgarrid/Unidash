#!/bin/bash

# Create a conda environment named "unidash_env" with Python 3.8
conda create --name unidash_env python=3.8 -y

# Activate the conda environment
source activate unidash_env

# Install the required packages from requirements.txt
pip install -r requirements.txt
