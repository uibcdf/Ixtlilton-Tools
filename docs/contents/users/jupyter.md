# Jupyter


conda install jupyter jupyter_contrib_nbextensions ipywidgets widgetsnbextension nb_conda nb_anacondacloud

## JupyterHub

## Sources
http://jupyter-notebook.readthedocs.io/en/stable/index.html

https://jupyterhub.readthedocs.io/en/latest/
https://jupyterhub.readthedocs.io/en/0.7.0/getting-started.html
https://github.com/jupyterhub/jupyterhub/wiki/Spawners

http://jupyter-contrib-nbextensions.readthedocs.io/en/latest/index.html
https://github.com/Anaconda-Platform/nb_conda

https://ipywidgets.readthedocs.io/en/latest/
http://ipywidgets.readthedocs.io/en/stable/index.html

##
```
yum install npm nodejs
conda create -n JupyterHub python=3
source activate JupyterHub
conda install jupyter
conda install jupyterhub notebook
```

```
jupyterhub --ip 192.168.0.100 --port 443
```


## Jupyter Notebook Extensions

```
conda install jupyter_contrib_nbextensions
conda install -c conda-forge ipywidgets
conda install -c conda-forge widgetsnbextension
conda install -c conda-forge nb_conda
conda install -c conda-forge nb_anacondacloud
```

## Environments

## MDLab2

## JupyterLab

http://192.168.0.100:443/lab

http://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html
http://jupyterlab.readthedocs.io/en/stable/user/jupyterhub.html

```
conda update -y --all
conda install -c conda-forge jupyterlab
jupyter labextension install @jupyterlab/hub-extension
jupyter labextension install jupyterlab_bokeh
jupyter labextension install @jupyterlab/google-drive
jupyter labextension install @jupyterlab/github
```
