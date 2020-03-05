import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="physiquepy", # Replace with your own username
    version="0.0.1",
    author="THERINCOURT David",
    author_email="",
    description="Une librairie Python pour les sciences physiques",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/david-therincourt/physique",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
