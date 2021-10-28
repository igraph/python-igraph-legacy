Legacy wrapper for the Python interface of the igraph library
--------------------------------------------------------------

The Python interface of the [igraph library](https://igraph.org/python/) has
been published on PyPI as `python-igraph` since the inception of the project.
However, the Python interface was renamed to `igraph` on PyPI in October 2021
and the package is now published as` igraph` from version 0.9.7 onwards. This
package is a placeholder that is going to be published as `python-igraph` for
new `igraph` releases until Sep 1, 2022 and its only purpose is to bring in
the "real" igraph package as a dependency during the transition period.

If you use `python-igraph` as a dependency in any of your own projects, you
are advised to change the dependency to `igraph` until Sep 1, 2022. New
releases will _not_ be published under `python-igraph` from Sep 1, 2022
onwards.
