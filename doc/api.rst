.. _api:

=============
API Reference
=============

This is the API for the **synced_collections** package.

Collection Types
================

.. currentmodule:: synced_collections

.. autoclass:: SyncedCollection
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: SyncedDict
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: SyncedList
    :members:
    :undoc-members:
    :show-inheritance:

.. currentmodule:: synced_collections.data_types.attr_dict

.. autoclass:: AttrDict
    :members:
    :undoc-members:
    :show-inheritance:

Backends
========

.. currentmodule:: synced_collections.backends.collection_json

.. autoclass:: JSONCollection
    :members:
    :undoc-members:
    :show-inheritance:

.. currentmodule:: synced_collections.backends.collection_mongodb

.. autoclass:: MongoDBCollection
    :members:
    :undoc-members:
    :show-inheritance:

.. currentmodule:: synced_collections.backends.collection_redis

.. autoclass:: RedisCollection
    :members:
    :undoc-members:
    :show-inheritance:

.. currentmodule:: synced_collections.backends.collection_zarr

.. autoclass:: ZarrCollection
    :members:
    :undoc-members:
    :show-inheritance:


Buffers
=======

.. currentmodule:: synced_collections.buffers.buffered_collection

.. autoclass:: BufferedCollection
    :members:
    :undoc-members:
    :show-inheritance:

.. currentmodule:: synced_collections.buffers.file_buffered_collection

.. autoclass:: FileBufferedCollection
    :members:
    :undoc-members:
    :show-inheritance:

.. currentmodule:: synced_collections.buffers.memory_buffered_collection

.. autoclass:: SharedMemoryFileBufferedCollection
    :members:
    :undoc-members:
    :show-inheritance:

.. currentmodule:: synced_collections.buffers.serialized_file_buffered_collection

.. autoclass:: SerializedFileBufferedCollection
    :members:
    :undoc-members:
    :show-inheritance:

Concrete Collections
====================

.. currentmodule:: synced_collections.backends.collection_json

.. autoclass:: JSONDict
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: JSONList
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: BufferedJSONCollection
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: BufferedJSONDict
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: BufferedJSONList
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: MemoryBufferedJSONCollection
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: MemoryBufferedJSONDict
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: MemoryBufferedJSONList
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: JSONAttrDict
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: JSONAttrList
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: BufferedJSONAttrDict
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: BufferedJSONAttrList
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: MemoryBufferedJSONAttrDict
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: MemoryBufferedJSONAttrList
    :members:
    :undoc-members:
    :show-inheritance:

.. currentmodule:: synced_collections.backends.collection_mongodb

.. autoclass:: MongoDBDict
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: MongoDBList
    :members:
    :undoc-members:
    :show-inheritance:

.. currentmodule:: synced_collections.backends.collection_zarr

.. autoclass:: ZarrDict
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: ZarrList
    :members:
    :undoc-members:
    :show-inheritance:

.. currentmodule:: synced_collections.backends.collection_redis

.. autoclass:: RedisDict
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: RedisList
    :members:
    :undoc-members:
    :show-inheritance:
