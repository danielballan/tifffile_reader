from setuptools import setup


setup(
    name='tifffile_reader',
    packages=['tifffile_reader'],
    entry_points={
        'TBD.readers':
            ['image/tiff = tifffile_reader:TIFFReader']},
    install_requires=['dask[array]', 'tifffile'],
)
