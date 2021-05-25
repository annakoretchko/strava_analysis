
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='strava_analysis',
    version='0.01',
    author="Anna Koretchko",
    author_email='annakoretchko@gmail.com',
    description='Basic Analysis of Strava running data',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)