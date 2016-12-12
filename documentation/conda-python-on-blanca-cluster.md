---
layout: single
title: 'Setting up a custom Python environment on the Earth Lab condo cluster'
date: 2016-12-12
authors: [Max Joseph]
category: [tutorials]
excerpt: 'This tutorial explains how members of Earth Lab can log in to the condo cluster and set up Python environments with Anaconda.'
sidebar:
  nav:
author_profile: false
comments: true
lang: python
lib: 
---

This post is written for members of Earth Lab with CU Boulder Research Computing accounts who would like to use the Earth Lab condo cluster to run jobs in Python with custom libraries. 
If you are in Earth Lab, but do not have an account, you'll need to see the [Research Computing Getting Started Guide](https://rc.colorado.edu/support/getting-started.html) and follow the instructions for gaining access.
Assuming that you're in Earth lab, and that you have an account, this tutorial will guide you through the process of logging in to the cluster, starting an interactive job, installing [Anaconda](https://www.continuum.io/), and creating a virtual environment with custom modules. 

## Step 1: use SSH to access a login node

To gain access to the Earth Lab cluster, you must use SSH to access a Research Computing login node. 
For more on this step, see the [Remote access and logging in guide](https://rc.colorado.edu/support/user-guide/remote-access.html).

```bash
ssh -l $username login.rc.colorado.edu
```

replacing `$username` with your Research Computing username. 

## Step 2: start an interactive job on the Earth Lab cluster

The above command gets you access to a login node. 
Next, you'll want to start an interactive job on the Earth Lab cluster. 
This step requires that you have permission to use the cluster. 
If you are in Earth Lab and you do not have permission, contact the Analytics Hub by sending an e-mail to el-help@colorado.edu to gain access. 

```bash
ml slurm/blanca
sinteractive --qos=blanca-el
```

## Step 3: installing Anaconda

First you'll need to download the Anaconda installer from [Continuum's website](https://www.continuum.io/downloads). 
There is an installer for Python 2 and one for Python 3 - be sure to get the installer that corresponds to the version of Python that you would like to use. 
Here, I'll assume you want Python 3.
We will download our file into our projects directory, to avoid cluttering our home directory. 

```bash
cd /projects/$USER/
wget https://repo.continuum.io/archive/Anaconda3-4.2.0-Linux-x86_64.sh
```

Before executing the installation script, you should verify the data integrity of the files using the MD5 hash. 
First, go online to find what the hash should be. 
For instance, the hash information for the file downloaded above can be found at https://docs.continuum.io/anaconda/hashes/Anaconda3-4.2.0-Linux-x86_64.sh-hash. 
This address will differ based on which version of the installer you are using. 
To find hash information for other installers, see [https://docs.continuum.io/anaconda/hashes/](https://docs.continuum.io/anaconda/hashes/).

To check the MD5 sum of the file that you downloaded, execute the following from within your interactive session: 

```bash
md5sum Anaconda3-4.2.0-Linux-x86_64.sh 
```

Next, verify that the output from that command matches the hash online. 
If it does not, the file may not have downloaded completely, and you may need to download it again. 

Once the MD5 sums match, you can install Anaconda by executing the script:

```bash
bash Anaconda3-4.2.0-Linux-x86_64.sh
```

The installer will prompt you to approve the terms of the license, and it will also prompt you to provide an installation location. 
Instead of using the default (`/home/$USER/anaconda3`), use your projects directory: `/projects/$USER/anaconda3`. 
After you specify your installation directory, the installation will proceed. 
Once the installation is done, you will be prompted to prepend the Anaconda install location to your PATH variable. 
If you are primarily going to use Anaconda on the Earth Lab condo cluster for your Python needs, you can answer yes. 
If you plan to frequently use other Python builds, you may wish to answer no. 

In order for the installation to take effect, exit and reopen your interactive session. 

```bash
exit
sinteractive --qos=el-blanca
```

To update conda, type the following:

```bash
conda update conda
```
 
For more information on installation and uninstallation, see http://conda.pydata.org/docs/install/full.html

## Step 4: creating virtual environments

Anaconda allows you to have separate virtual environments for projects that require different dependencies, and provides fairly good support for package dependency management. 
For instance, if you had a project that needed to use the [GDAL](http://www.gdal.org/) and [PySAL](http://pysal.readthedocs.io/en/latest/) libraries, you could create a named environment with gdal installed via:

```bash
conda create --name my-spatial-env gdal pysal 
```

Anaconda will then prompt you to proceed or not, and list the packages that will be downloaded, upgraded/downgraded, and installed.
If you hit `y + Return`, the installation will proceed. 

Once the installation is complete, you can activate the environment by typing:

```bash
source activate my-spatial-env
```

(If you need to deactivate an environment you can do so via `source deactivate`).

Then test it out to verify that the packages were actually installed!

```bash
python
```

From within python, you should now be able to import these packages. 

```python
from osgeo import gdal
import pysal
quit()
```

That's it! 
For more information on managing Anaconda virtual environments, have a look at the [Getting Started Guide](http://conda.pydata.org/docs/test-drive.html) on the Anaconda website. 

