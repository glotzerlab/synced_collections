.. _installation:

============
Installation
============

The software is tested for Python versions 3.8+ and has no required dependencies.
Some features or backends are not supported by the standard library and require additional packages.

Source Code Installation
========================

You can clone the `git repository <https://github.com/glotzerlab/synced_collections>`_ and pip install it directly (Option 1), or install directly from git (Option 2).

.. code:: bash

  # Option 1
  git clone https://github.com/glotzerlab/synced_collections.git
  cd synced_collections
  pip install .

  # Option 2
  pip install git+https://github.com/glotzerlab/synced_collections.git


Consider installing :ref:`optional dependencies <optional_dependencies>`.

.. _optional_dependencies:

Optional dependencies
=====================

Optional dependencies are not installed automatically.
In case you want to use extra features that require external packages, you need to install these manually.

Extra features with dependencies:

.. glossary::

    Support for storing numpy arrays as synced lists
      required: ``numpy``

    Zarr backend
      required: ``zarr``

    Redis backend
      required: ``redis``

    MongoDB backend
      required: ``pymongo``
