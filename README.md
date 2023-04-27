# <img src="https://raw.githubusercontent.com/glotzerlab/signac/main/doc/images/palette-header.png" width="75" height="58"> synced_collections - Pythonic abstractions over data collections

[![Affiliated with NumFOCUS](https://img.shields.io/badge/NumFOCUS-affiliated%20project-orange.svg?style=flat&colorA=E1523D&colorB=007D8A)](https://numfocus.org/sponsored-projects/affiliated-projects)
[![GitHub Actions](https://github.com/glotzerlab/synced_collections/actions/workflows/run-pytest.yml/badge.svg)](https://github.com/glotzerlab/synced_collections/actions)
[![License](https://img.shields.io/github/license/glotzerlab/synced_collections.svg)](https://github.com/glotzerlab/synced_collections/blob/main/LICENSE.txt)
[![Slack](https://img.shields.io/badge/Slack-chat%20support-brightgreen.svg?style=flat&logo=slack)](https://signac.io/slack-invite/)
[![Twitter](https://img.shields.io/twitter/follow/signacdata?style=social)](https://twitter.com/signacdata)
[![GitHub Stars](https://img.shields.io/github/stars/glotzerlab/synced_collections?style=social)](https://github.com/glotzerlab/synced_collections/)

The [**signac** framework](https://signac.io) helps users manage and scale file-based workflows, facilitating data reuse, sharing, and reproducibility.

The **synced_collections** package provides Pythonic abstractions over various underlying data stores, presenting APIs that behave like standard built-in Python collections like dicts.
**synced_collections** form the backbone of **signac**'s data and metadata storage, but may be used just as easily outside of **signac**.
For instance, users wishing to access a JSON file on disk like a dictionary and automatically persist all changes could use the `synced_collections.JSONDict`.

## Resources

- [Slack Chat Support](https://signac.io/slack-invite/):
  Get help and ask questions on the **signac** Slack workspace.
- [**signac** website](https://signac.io/):
  Framework overview and news.

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
