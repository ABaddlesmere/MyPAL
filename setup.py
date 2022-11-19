from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="MyPAL",
    version="0.0.1",
    author="ABaddlesmere",
    author_email="alexdickers@gmail.com",
    description="An asynchronous python API wrapper for MyAnimeList",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ABaddlesmere/MyPAL",
    install_requires=['aiohttp', 'asyncio'],
    packages=find_packages(),
    python_requires=">=3.10",
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)