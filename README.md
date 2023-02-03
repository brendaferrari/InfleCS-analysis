🔴❗UNDER DEVELOPMENT❗🔴

# INFLECS methodology

Script developed to use [Free energy estimation and clustering with InfleCS](https://github.com/delemottelab/InfleCS-free-energy-clustering-tutorial) methodology of Free Energy Landscape generation.

## Instalation

Download [Free energy estimation and clustering with InfleCS](https://github.com/delemottelab/InfleCS-free-energy-clustering-tutorial) on the working directory

Download the INFLECS methodology code and unzip it on the desirable directory. To prepare the environment use the following command:

```
conda env create -f environment.yml
``` 

Copy the folder 'free_energy_clustering' inside the inflecs method folder, in which you are going to have:

```
inflecs-method

    - free_energy_clustering

    - environment.yml

    - main.py

    - README.md
```

## How to use

Activate the environment using:

```
conda activate inflecs-analysis
```

You may modify the filename 'data_c.csv' on the main.py file for the name of your file

```
data = np.loadtxt('data_c.csv')
print(data)
```

To run the analysis just use:

```
python main.py
```

## Observations

This script was developed following the [Tutorial: Estimating Free energy landscapes and clustering with Gaussian mixture models](https://github.com/delemottelab/InfleCS-free-energy-clustering-tutorial/blob/master/tutorial_free_energy_clustering.ipynb).

## Authorship

* Author: **Brenda Ferrari** ([brendaferrari](https://github.com/brendaferrari))