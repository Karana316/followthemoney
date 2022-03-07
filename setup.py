from setuptools import setup, find_packages

setup(
    name='followthemoney',
    url='https://github.com/Karana316/followthemoney',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    setup_requires=['setuptools_scm'],
    use_scm_version=True,
    install_requires=['requests', 'regex', 'pandas', 'python-dotenv'],
    include_package_data=True,
)

