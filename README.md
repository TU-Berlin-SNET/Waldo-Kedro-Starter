# The `waldo-kedro-starter` Kedro starter

This Kedro starter was created as part of the [_Waldo_](https://www.snet.tu-berlin.de/menue/projects/waldo/) research project.

## Authors
- [Aljoscha Schulte](https://www.tu.berlin/en/snet/about-us/team-and-persons/aljoscha-schulte/)
- [Christoph Schulthess](https://www.snet.tu-berlin.de/menue/team/christoph_schulthess/)
- [Uttam Dhakal](https://github.com/uttamdhakal)
- [Zohaib Akhtar Khan](https://github.com/zakhan4)

## Introduction

The code in this repository demonstrates best practice when working with Kedro. It contains a Kedro starter template with some initial configuration and an example pipeline.

## Installation

In order to create a new kedro project using a starter, you need to apply the `--starter` flag to `kedro new` like this:

```
kedro new --starter=<path-to-waldo-kedro-starter>
```

You will now get a prompt to set your `Project Name`, `Repository Name` and `Python Package Name`. You can also specify this from a configuration file as follows:

```
kedro new --config=my_project_config.yml --starter=<path-to-waldo-kedro-starter>
```

