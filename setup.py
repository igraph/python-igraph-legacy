import sys

###########################################################################

# Check Python's version info and exit early if it is too old
if sys.version_info < (3, 6):
    print("This module requires Python >= 3.6")
    sys.exit(1)

###########################################################################

from setuptools import setup

VERSION = "0.11.2"

description = """Python interface to the igraph high performance graph
library, primarily aimed at complex network research and analysis.

**This package is deprecated; use the igraph package instead. This package will
be kept in sync with igraph until Sep 1, 2022 and it will not receive any
updates after Sep 1, 2022.**

Graph plotting functionality is provided by the Cairo library, so make
sure you install the Python bindings of Cairo if you want to generate
publication-quality graph plots. You can try either `pycairo
<http://cairographics.org/pycairo>`_ or `cairocffi <http://cairocffi.readthedocs.io>`_,
``cairocffi`` is recommended because there were bug reports affecting igraph
graph plots in Jupyter notebooks when using ``pycairo`` (but not with
``cairocffi``).
"""

options = dict(
    name="python-igraph",
    version=VERSION,
    url="https://igraph.org/python",
    description="High performance graph data structures and algorithms (legacy package)",
    long_description=description,
    license="GNU General Public License (GPL)",
    author="Tamas Nepusz",
    author_email="ntamas@gmail.com",
    project_urls={
        "Bug Tracker": "https://github.com/igraph/python-igraph/issues",
        "Changelog": "https://github.com/igraph/python-igraph/blob/master/CHANGELOG.md",
        "CI": "https://github.com/igraph/python-igraph/actions",
        "Documentation": "https://igraph.org/python/doc",
        "Source Code": "https://github.com/igraph/python-igraph",
    },
    packages=[],
    install_requires=["igraph==" + VERSION],
    extras_require={
        "cairo": ["cairocffi>=1.2.0"],
        "matplotlib": ["matplotlib>=3.3.0; platform_python_implementation != 'PyPy'"],
        "plotly": ["plotly>=5.3.0"],
        # compatibility alias to 'cairo' for python-igraph <= 0.9.6
        "plotting": ["cairocffi>=1.2.0"],
    },
    python_requires=">=3.6",
    platforms="ALL",
    keywords=[
        "graph",
        "network",
        "mathematics",
        "math",
        "graph theory",
        "discrete mathematics",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: C",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)

setup(**options)
