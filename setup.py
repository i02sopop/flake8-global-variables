import setuptools

requires = [
    "flake8 > 3.0.0",
]

setuptools.setup(
    name="flake8_global_variables",
    license="MIT",
    version="0.1.0",
    description="It shows an error when it finds a global variable defined",
    author="Ritho",
    author_email="p.alvarez@zaleos.net",
    url="https://github.com/i02sopop/flake8-global-variables",
    packages=[
        "flake8_global_variables",
    ],
    install_requires=requires,
    entry_points={
        'flake8.extension': [
            'X = flake8_global_variables.globalvariables:GlobalVariables',
        ],
    },
    classifiers=[
        "Framework :: Flake8",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
)
