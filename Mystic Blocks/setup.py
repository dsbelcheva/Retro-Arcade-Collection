from setuptools import setup

setup(
    name='MysticBlocks',
    version='0.1.0',
    py_modules=['play_mystic_blocks'],
    install_requires=[
        'click',
    ],
      entry_points={
        'console_scripts': [
            'play-mystic-blocks=play_mystic_blocks:cli',
        ],
    },
)
