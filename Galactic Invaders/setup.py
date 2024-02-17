from setuptools import setup, find_packages

setup(
    name='Galactic Invaders',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'play-galactic-invaders=galacticinvaders.play_galactic_invaders:cli',
        ],
    },
)
