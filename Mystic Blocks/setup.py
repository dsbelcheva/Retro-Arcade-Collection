from setuptools import setup, find_packages

setup(
    name='MysticBlocks',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'click',
    ],
      entry_points={
        'console_scripts': [
            'play-mystic-blocks=mysticblocks.play_mystic_blocks:cli',
        ],
    },
)
