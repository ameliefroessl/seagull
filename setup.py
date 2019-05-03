# -*- coding: utf-8 -*-

# Import modules
from setuptools import find_packages, setup

with open("README.md", encoding="utf8") as readme_file:
    readme = readme_file.read()

with open("requirements.in") as f:
    requirements = f.read().splitlines()

test_requirements = [
    "pytest==3.6.4",
    "pytest-cov",
    "flake8==3.5.0",
    "tox",
    "mypy",
]

setup(
    name="Seagull",
    version="1.0.0-alpha.1",
    description="Python library for simulating Conway's Game of Life",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Lester James V. Miranda",
    author_email="ljvmiranda@gmail.com",
    url="https://github.com/ljvmiranda921/seagull",
    packages=find_packages(exclude=["docs", "tests"]),
    include_package_data=True,
    install_requires=requirements,
    tests_require=test_requirements,
    license="MIT license",
    zip_safe=False,
    keywords=["osm", "conway game of life" "mathematics", "cellular automata"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Artificial Life",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.5",
    ],
    test_suite="tests",
)
