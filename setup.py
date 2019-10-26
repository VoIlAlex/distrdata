from distutils.core import setup
setup(
    name='distrdata',         # How you named your package folder (MyLib)
    packages=['distrdata'],   # Chose the same as "name"
    # Start with a small number and increase it with every change you make
    version='1.0.0-alpha',
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license='MIT',
    # Give a short description about your library
    description='Collection of generators for generating points of different distributions.',
    author='Ilya Vouk',                   # Type in your name
    author_email='ilya.vouk@gmail.com',      # Type in your E-Mail
    # Provide either the link to your github or to your website
    url='https://github.com/VoIlAlex/distrdata',
    # I explain this later on
    download_url='https://github.com/VoIlAlex/distrdata/archive/v1.0.0-alpha.tar.gz',
    # Keywords that define your package best
    keywords=['dataset', 'generator', 'data', 'science'],
    install_requires=[            # I get to this in a second
        'numpy',
        'scipy',
    ],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
)
