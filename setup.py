import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scrape-pkg-djwight",
    version="0.1",
    author="Darren Wight",
    author_email="d.j.wight@gmail.com",
    description="A package to scrape different types of database websites",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/djwight/scrape",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',)
