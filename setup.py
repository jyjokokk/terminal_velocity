from setuptools import setup

setup(
    name="terminal_velocity-jyjokokk",
    version="0.2.0",
    author="Jyrki Kokkola",
    packages=["terminal_velocity"],
    scripts=["bin/terminal_velocity"],
    url="http://vhp.github.com/terminal_velocity/",
    license="GNU General Public License, Version 3",
    description="A fast note-taking app for the UNIX terminal",
    long_description=open("README.md").read(),
    install_requires=[
        "urwid==1.1.1",
        "chardet==3.0.4",
        ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
    ],
    python_requires='>=3.6.3'
)
