[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/guiwitz/napari_demo/master)

# Repository for tests of napari

In this repository you can find two examples of the possibilities offered by the visualisation tool [napari](https://github.com/napari/napari). Both examples are really meant to be demos and not full fledged tools or scientific studies.

## Running the examples

### On mybinder
Both examples can be run via [mybinder](https://mybinder.org/) by clicking the button on top of this Readme. As napari is not integrated into Jupyter, the workaround solution provided [here](https://github.com/manics/jupyter-omeroanalysis-desktop/tree/napari-binder) is used. In both notebooks, you have to click on a link provided at the top of the notebook which opens a new window where napari is visible (within a remote desktop). Mybinder is not meant to process large datasets, so the data used in the 3D image processing example have to be reduced. Just follow the instructions at the data import step.

### Local installation
It's really easy to install the necessary pices on your own machine using conda. Copy the following lines into a file typically called environment.yml:

```yml
name: python3d
channels:
  - conda-forge
dependencies:
  - pip
  - scipy
  - numpy
  - matplotlib
  - pandas
  - scikit-image
  - scikit-learn
  - jupyter
  - ipywidgets
  - pip:
    - napari
    - trackpy
    - requests
```

And create the conda environment by calling:
```bash
conda env create -f environment.yml
```

## Example 1: [Ilastik-like application](napari_ilastik.ipynb)

This notebook allows to use a Pixel classifier to segment images based on a manual selection of categories. It follows in a very simplified way the principle of [ilastik](https://www.ilastik.org/). ilastik is a great software, so what's the purpose of this demo? Here's a few ideas:

- It can be used for teaching purposes as all the steps are directly accesible within the notebook, e.g. the paramters of the classifier can be changed. 
- This approach can also be customized very easily, e.g. with specific filters. 
- ilastik is sometimes constraining in terms of file formats. Here this issue can be handled directly in the notebook with numpy and e.g. bioformats.
- Other useful packages could be mixed in. For example one can use [dask](https://docs.dask.org/en/latest/) on a cluster to run sciki-learn on large dataset, typcially 3D images.

## Example 2: [3D image processing](napari_3d_image_processing.ipynb)

This notebook shows how napari can be used in a typical 3D image processing pipeline. This is a thing which was notoriously difficult to do in Python/Jupyter (see e.g. the [interesting post](https://ilovesymposia.com/2019/10/24/introducing-napari-a-fast-n-dimensional-image-viewer-in-python/) on this topic of one of the napari developers). I'm using here a public dataset deposited on [zenodo](https://zenodo.org/record/1211599#.Xbf9QpP0nOS). Detection and tracking of cells is done with [scikit-image](https://scikit-image.org/) and [trackpy](https://soft-matter.github.io/trackpy/v0.3.2/). This example is not meant to be "scientifically meaningful" but an demo of how different type of information can be shown in napari.
