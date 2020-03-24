
# Computational Neuroscience Project Skeleton

This repository is a skeleton Python package that students in PSYC 5270 can use to get started on their data exploration assignments.

## Getting started

Start by cloning the repository: `git clone https://github.com/melizalab/comp-neurosci-skeleton.git`

This will create a new directory, `comp-neurosci-skeleton`, containing the following items:

- `README.md`: this file
- `setup.py`:  package description file. You will need to edit this.
- `requirements.txt`: a list of packages your code depends on
- `.gitignore`: a list of files git will ignore when telling you what's changed
- `src`:       a directory where you will put your python code
- `test`:      a directory where you will put test code
- `data`:      a directory where your data will live
- `build`:     a directory where processed output from your analysis will live

Choose a new name for your package. For the PSYC 5270 assignment, use something like `crcns-datasetid-computingid`. Rename the top-level directory (`comp-neurosci-skeleton`) and edit `setup.py` to set the new name and other identifying information.

Now you need to create a github repository of your own. Go to [https://github.com/new](https://github.com/new). Give the repository your chosen name and a description, then click Create Repository. **DO NOT** check the box to initialize the repository with a readme. Ignore the instructions on how to set up your repository, but make a note of the address. It will look something like `https://github.com/dmeliza/dummy.git`

Finally, set your local directory to track the github repository by running the following commands in your working directory. Replace the repository address in the code below with the one for your project.

``` shell
git remote rm origin
git remote add origin https://github.com/dmeliza/dummy.git
git push -u origin master
```

If you get an error on the last command, it's probably because you let github initialize your repository. You'll have to delete and re-create the repository on github and then run the last command again.

## Next steps

Edit `data/README.md` to describe how to retrieve data. Better yet, write a script.

Edit `requirements.txt` to add any needed dependencies, then create a virtual environment and install the dependencies as follows:

``` shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Alternatively, if you're using anaconda, create a new environment and run the following to install dependencies:

``` shell
conda install git numpy scipy pandas matplotlib notebook
```

Install the project in development mode by running `python setup.py develop`. If you use notebooks, this will ensure that you can access your modules.

Edit this file to describe your actual project.

## Project Description

Experiment Description:

This mouse received an injection of AAV1.Syn.Flex.GCaMP6s.WPRE lot CS0215 designed by the GENIE Project, Janelia Farms, and produced by the University of Pennsylvania Vector Core on postnatal day 36 (P36). The mouse then received surgery for head-plate implantation and a craniotomy for glass window placement over visual cortex at P59. A metal head-plate was cemented to the skull and a 5 mm circular craniotomy was made. Two 5 mm and one 8 mm circular glass cover slips were glued together and fitted into the craniotomy. The 8 mm coverslip rested against the surface of the skull and was cemented in place.

The mouse was handled and habituated to head-fixation and the imaging rig for 3 weeks before experiments began. During the example experiment, the animal was permitted to run on a freely-rotating disc while visual stimuli were presented to the eye contralateral to the imaged region. Visual stimuli and software for tracking the eye and motion of the mouse were created in Python. Stimuli consisted of drifting sinusoidal gratings presented at 80% contrast shown in random order for all permutations of 5 spatial frequencies (SF), 5 temporal frequencies (TF), and 8 orientations (0° to 315° in 45° steps). Stimuli were presented 8 times each, full-field, for 3 seconds with a mean luminance inter-stimulus-interval of 2 seconds on an LCD monitor spanning 60° in elevation and 130° in azimuth. The mouse’s eye was positioned 22 cm away from the center of the monitor. Image data were acquired using a custom built two-photon microscope with resonant and galvo scanners, and a MaiTai femtosecond laser (Spectra-Physics) at 910 nm. Images were collected at approximately 30 Hz with 512 lines per frame. The image area is approximately 300 micrometers below the pia, which corresponds to layer 4 in the windowed adult mice.