# The `waldo-kedro-starter` Kedro starter

## Authors
- Aljoscha Schulte
- Christoph Schulthess
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

