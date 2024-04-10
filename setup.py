import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_discription = f.read()

__version__ = "0.0.0"

REPO_NAME = "terraflood"
AUTHOR_USER_NAME = "miladshani"
SRC_REPO = "terraflood"
AUTHOR_EMAIL = "milad.shani@terradue.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    description="Python package for flood/water masking using Sentinel1 satellite data",
    long_description=long_discription,
    long_description_markdown="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)