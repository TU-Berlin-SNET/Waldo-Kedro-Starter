# {{ cookiecutter.project_name }}

## Overview

This is your new Kedro project, which was generated using `Kedro {{ cookiecutter.kedro_version }}`.

Take a look at the [Kedro documentation](https://kedro.readthedocs.io) to get started.

## Rules and guidelines

In order to get the best out of the template:

* Don't remove any lines from the `.gitignore` file we provide
* Make sure your results can be reproduced by following a [data engineering convention](https://kedro.readthedocs.io/en/stable/11_faq/01_faq.html#what-is-data-engineering-convention)
* Don't commit data to your repository
* Don't commit any credentials or your local configuration to your repository. Keep all your credentials and local configuration in `conf/local/`

## How to install dependencies

Declare any dependencies in `src/requirements.txt` for `pip` installation and `src/environment.yml` for `conda` installation.

To install them, run:

```
pip install -r src/requirements.txt
```

## How to run Kedro

You can run your Kedro project with:

```
kedro run
```

## How to test your Kedro project

Have a look at the file `src/tests/test_run.py` for instructions on how to write your tests. You can run your tests as follows:

```
kedro test
```

To configure the coverage threshold, look at the `.coveragerc` file.


## Project dependencies

To generate or update the dependency requirements for your project:

```
kedro build-reqs
```

This will copy the contents of `src/requirements.txt` into a new file `src/requirements.in` which will be used as the source for `pip-compile`. You can see the output of the resolution by opening `src/requirements.txt`.

After this, if you'd like to update your project requirements, please update `src/requirements.in` and re-run `kedro build-reqs`.

[Further information about project dependencies](https://kedro.readthedocs.io/en/stable/04_kedro_project_setup/01_dependencies.html#project-specific-dependencies)


## Using Docker

### Build the docker image (depending on your setup, use sudo)
```
docker build \
    -t {{ cookiecutter.project_name }}/$VERSION_TAG \
    --build-arg DOCKER_BUILDKIT=1 \
    --build-arg BUILDKIT_INLINE_CACHE=1 \
    .
```

### Run Docker container w/ volume mount for all pipelines
```
docker run \
    -v $INPUT_DATA_DIR_PATH:/home/{{ cookiecutter.project_name }}/data/00_input \
    -v $OUTPUT_DATA_DIR_PATH:/home/{{ cookiecutter.project_name }}/data/99_output \
    --env DOCKER_BUILDKIT=1 \
    {{ cookiecutter.project_name }}/$VERSION_TAG 
```

### Run Docker container w/ volume mount for a specific pipeline
```
docker run \
    -v $INPUT_DATA_DIR_PATH:/home/{{ cookiecutter.project_name }}/data/00_input \
    -v $OUTPUT_DATA_DIR_PATH:/home/{{ cookiecutter.project_name }}/data/99_output \
    --env DOCKER_BUILDKIT=1 \
    {{ cookiecutter.project_name }}/$VERSION_TAG  \
    --pipeline $PIPELINE_NAME
```
