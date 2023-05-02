.. _tutorial:

========
Tutorial
========

**synced_collections** make it easy to store collections of data into various common data stores.
The simplest backend to use is the JSON backend, which works out of the box using nothing more than the Python standard library.
With this backend, a standard Python data collection may be automatically synchronized with a JSON file.

.. code-block:: python

    from synced_collections.backends.collection_json import JSONDict, JSONList

    d = JSONDict("dict.json")
    d["size"] = 10
    d["color"] = "blue"

    l = JSONList("list.json")
    l = [10, "blue"]

This will create the following JSON files:

.. code-block:: bash

    ~ $ cat dict.json
    {'size': 10, 'color': 'blue'}
    ~ $ cat list.json
    [10, "blue"]

These types automatically support nested data structures in the same way as normal collections, and will automatically convert normal Python collections accordingly:

.. code-block:: python

   d["jsonlist"] = l
   d["list"] = [10, "blue"]

.. code-block:: bash

    ~ $ cat dict.json
    {"size": 10, "color": "blue", "jsonlist": [10, "blue"], "list": [10, "blue"]}

If you are writing lots of different data, it may be helpful to work within a buffered context to reduce the overhead of writing data out to the backend after each operation.
**synced_collections** supports different buffering strategies for different backends, but these are all exposed via the same API.
For instance, the file created above may be read to or written like so:

.. code-block:: python

    from synced_collections.backends.collection_json import MemoryBufferedJSONDict as JSONDict

    d2 = JSONDict("dict.json")
    with d2.buffered:
        d2["buffer1"] = "value1"
        d2["buffer2"] = "value2"

In this case, neither of these keys will actually be written to the file until the buffered context is exited.

Alternative backends may be used if the necessary dependencies are installed.
Here is an example of storing data in a Redis instance run via Docker.
First, we launch Redis using a Docker container:

.. code-block:: bash

    docker run -p 6379:6379 -it redis/redis-stack:latest

To use this store, we create a Redis client in Python and use it with our Redis collection:

.. code-block:: python

   import redis
   from synced_collections.backends.collection_redis import RedisDict
   client = redis.Redis()
   rd = RedisDict('data')
   rd['key'] = 'val'

The optimal choice of backend will vary based on the use case.
Not all backends support the same types of data, and many backends have different performance characteristics.
The optimal choice will depend on the particular application.
