from setuptools import setup
with open("README.md","r",encoding="utf-8") as fh:
    long_description=fh.read()
    
name_var = "hikari_Paginator"
author_var = "SnowyJaguar1034"
setup(
    name=name_var,
    version="0.0.0",
    description="Unofficial hikari multi page embed handler",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/{author_var}/{name_var}",
    author=author_var,
    author_email="51423344+SnowyJaguar1034@users.noreply.github.com",
    license="GNU",
    packages=["dinteractions_Paginator"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=["hikari"],
)
