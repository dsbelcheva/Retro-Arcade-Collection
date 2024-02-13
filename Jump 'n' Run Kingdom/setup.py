from setuptools import setup

setup(
    name='Jump \'n\' Run Kingdom',
    version='0.1.0',
    py_modules=['play_jump_run'],
    install_requires=[
        'click',
    ],
      entry_points={
        'console_scripts': [
            'play-jump-run=play_jump_run:cli',
        ],
    },
)