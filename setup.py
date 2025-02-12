from setuptools import setup, find_packages

setup(
    name="octav",  # Package name
    version="0.2.0",  # Initial version
    packages=find_packages(),  # Finds the octav/ folder
    description="A simple text modifier library",  # Short description
    author="Camil Caudron",
    author_email="0c1avf@gmail.com",
    url="https://github.com/0c1av",  # Update with your GitHub link
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
