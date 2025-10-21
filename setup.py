from setuptools import setup, find_packages

setup(
    name="plotutils",
    version="0.0.1",  # Typically start with 0.0.1 or 0.1.0 for initial release
    description="A collection of functions often used in my thesis plots",
    long_description=open(
        "README.md"
    ).read(),  # Include a README file for long description
    long_description_content_type="text/markdown",  # Specify the format of the long description
    url="https://github.com/philipp666/plotutils",
    author="Philipp Ziegler",
    author_email="ziegler_philipp@live.de",
    license="MIT",  # Ensure the license name is correctly formatted
    packages=find_packages(),  # Use find_packages() to automatically discover all packages
    install_requires=[
        "matplotlib>=3.0.0",  # Specify minimum versions if necessary
        "numpy>=1.17.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
    keywords="plotting, matplotlib, numpy, thesis, utilities",
    python_requires=">=3.6",  # Specify the Python versions you support
    include_package_data=True,  # Include package data specified in MANIFEST.in
)

