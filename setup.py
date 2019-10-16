import setuptools

setuptools.setup(
    name='elegance',

    version='1.0.0',

    author="Cem",

    author_email="cem@yokmail.com",

    description="Test tornado server",

    packages=['elegance', ],

    entry_points={'console_scripts': [
        'elegance = elegance.server:main',
    ]},

    install_requires=['tornado', ],

    python_requires='==3.6.8',
)
