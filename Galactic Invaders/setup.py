from setuptools import setup

setup(
    name='Galactic Invaders',
    version='0.1.0',
    py_modules=['play_galactic_invaders'],
    install_requires=[
        'click',
    ],
      entry_points={
        'console_scripts': [
            'play_galactic_invaders=play_galactic_invaders:cli',
        ],
    },
)