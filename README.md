## Creating your environment

### 1. Install conda
Ensure you have conda and mamba installed.

If you have conda, install mamba: `conda install -c conda-forge mamba`

If you have neither, install [mambaforge]().

### 2. Clone (or download) this repository

If you don't have git, install it via conda/mamba: `mamba install git`

Then, once you have git: `git clone https://github.com/themartinlab/crystal-video`

### 2. Create your conda environment
```
mamba env create -f environment.yaml
```

### 3. Activate your environment and start jupyterlab
```
conda activate crystal-video
jupyter lab .
``` 