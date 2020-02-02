import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="text_manips", # Replace with your own username
    version="0.0.1",
    author="Lorcan Conroy",
    author_email="lorcan.conroy@ucdconnect.ie",
    description="Library for manipulating text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Lockers13/text_manips",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
