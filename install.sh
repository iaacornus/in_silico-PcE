#!/usr/bin/env bash

function conda_install() {
    if [[ ! $(command -v conda &> /dev/null) ]]; then
        wget https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Linux-x86_64.sh
        bash Anaconda3-2023.09-0-Linux-x86_64.sh
    end
}

conda_install
conda update conda
conda create -n prototype python=3.11 anaconda
conda activate prototype



