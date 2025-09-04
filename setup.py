from setuptools import setup, Extension
import pybind11

ext_modules = [
    Extension(
        "grayscale.grayscale",       # full module path
        ["grayscale/grayscale.cpp"], # source file
        include_dirs=[pybind11.get_include()],
        language="c++",
        extra_compile_args=["-O3", "-std=c++17"],
    ),
]

setup(
    name="grayscale",
    version="0.1.0",
    author="Satyam Patel",
    description="A fast RGB → Grayscale converter using C++ + stb",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/samir1120k/grayscale", 
    license="MIT",
    packages=["grayscale"],
    ext_modules=ext_modules,
    python_requires=">=3.7",
    install_requires=["numpy", "pybind11"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: C++",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
