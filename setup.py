from setuptools import setup

setup(
    name="plurk-api",
    packages=["plurk-api"],
    version="1.0.0",
    description="Plurk API",
    author="Joshua Avalon",
    author_email="joshuaavalon@gmail.com",
    url="https://github.com/joshuaavalon/python-plurk-api",
    keywords=["plurk", "oauth"],
    classifiers=[],
    license="MIT",
    python_requires=">=3",
    requires=["oauth2"]
)
