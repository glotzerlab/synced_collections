# <img src="https://raw.githubusercontent.com/glotzerlab/signac/main/doc/images/palette-header.png" width="75" height="58"> synced_collections - Pythonic abstractions over data collections

[![Affiliated with NumFOCUS](https://img.shields.io/badge/NumFOCUS-affiliated%20project-orange.svg?style=flat&colorA=E1523D&colorB=007D8A)](https://numfocus.org/sponsored-projects/affiliated-projects)
[![GitHub Actions](https://github.com/glotzerlab/synced_collections/actions/workflows/run-pytest.yml/badge.svg)](https://github.com/glotzerlab/synced_collections/actions)
[![License](https://img.shields.io/github/license/glotzerlab/synced_collections.svg)](https://github.com/glotzerlab/synced_collections/blob/main/LICENSE.txt)
[![Slack](https://img.shields.io/badge/Slack-chat%20support-brightgreen.svg?style=flat&logo=slack)](https://signac.readthedocs.io/slack-invite/)
[![Twitter](https://img.shields.io/twitter/follow/signacdata?style=social)](https://twitter.com/signacdata)
[![GitHub Stars](https://img.shields.io/github/stars/glotzerlab/synced_collections?style=social)](https://github.com/glotzerlab/synced_collections/)
[![PyPI](https://img.shields.io/pypi/v/synced_collections.svg)](https://pypi.org/project/synced_collections/)
[![conda-forge](https://img.shields.io/conda/vn/conda-forge/synced_collections.svg?style=flat)](https://anaconda.org/conda-forge/synced_collections)
[![RTD](https://img.shields.io/readthedocs/synced_collections.svg?style=flat)](https://signac.readthedocs.io)
[![PyPI-downloads](https://img.shields.io/pypi/dm/synced_collections.svg?style=flat)](https://pypistats.org/packages/synced_collections)

The [**signac** framework](https://signac.readthedocs.io) helps users manage and scale file-based workflows, facilitating data reuse, sharing, and reproducibility.

The **synced_collections** package provides Pythonic abstractions over various underlying data stores, presenting APIs that behave like standard built-in Python collections like dicts.
**synced_collections** form the backbone of **signac**'s data and metadata storage, but may be used just as easily outside of **signac**.
For instance, users wishing to access a JSON file on disk like a dictionary and automatically persist all changes could use the `synced_collections.JSONDict`.

## Resources

- [Slack Chat Support](https://signac.readthedocs.io/slack-invite/):
  Get help and ask questions on the **signac** Slack workspace.
- [**signac** website](https://signac.readthedocs.io/):
  Framework overview and news.
- [Framework documentation](https://signac.readthedocs.io/):
  Examples, tutorials, topic guides, and package Python APIs.
- [Package documentation](https://signac.readthedocs.io/projects/synced-collections/):
  API reference for the **synced_collections** package.

## Installation

The recommended installation method for **synced_collections** is through **conda** or **pip**.
The software is tested for Python 3.8+ and is built for all major platforms.

To install **synced_collections** *via* the [conda-forge](https://conda-forge.org/) channel, execute:

```bash
conda install -c conda-forge synced_collections
```

To install **synced_collections** *via* **pip**, execute:

```bash
pip install synced_collections
```

**Detailed information about alternative installation methods can be found in the [documentation](https://signac.readthedocs.io/en/latest/installation.html).**

## Quickstart

This short example demonstrates what you can do with `synced_collections`.

```python
>>> from synced_collections.backends.collection_json import JSONDict
>>> d = JSONDict("data.json")
>>> d["size"] = 10
>>> d["color"] = "blue"
>>> import json
>>> with open("data.json") as f:
...     print(json.load(f))
...
{'size': 10, 'color': 'blue'}
```

## Testing

You can test this package by executing:

```bash
$ python -m pytest tests/
```

## Acknowledgment

When using **synced_collections** as part of your work towards a publication, we would really appreciate that you acknowledge the **signac** frameworkf appropriately.
We have prepared examples on how to do that [here](https://signac.readthedocs.io/en/latest/acknowledge.html).
**Thank you very much!**

The signac framework is a [NumFOCUS Affiliated Project](https://numfocus.org/sponsored-projects/affiliated-projects).
