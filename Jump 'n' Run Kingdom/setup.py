from setuptools import setup, find_packages

setup(
    name='Jump \'n\' Run Kingdom',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'click',
    ],
      entry_points={
        'console_scripts': [
            'play-jump-run=jumprun.play_jump_run:cli',
        ],
    },
)