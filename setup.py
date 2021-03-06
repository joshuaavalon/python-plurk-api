from setuptools import setup

setup(
    name="plurk_api",
    packages=["plurk_api"],
    version="2.0.2",
    description="Plurk API",
    author="Joshua Avalon",
    author_email="joshuaavalon@gmail.com",
    url="https://github.com/joshuaavalon/python-plurk-api",
    keywords=["plurk", "oauth"],
    classifiers=[],
    license="MIT",
    python_requires=">=3.6",
    install_requires=["oauth2", "typing"]
)
