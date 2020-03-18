# Reader Prototype for Tifffile

1. Clone this repo.

   ```sh
   git clone https://github.com/danielballan/tifffile_reader
   cd tifffile_reader
   ```

2. Generate example data.

   ```sh
   pip install -r requirements_for_generate_example_data.txt
   python generate_example_data.py
   ```

3. Install ``tifffile_reader``.

   ```sh
   pip install -e tifffile_reader
   ```

4. Try using reader directly to read one TIFF.

   ```py
   In [1]: import tifffile_reader

   In [2]: reader = tifffile_reader.TIFFReader('example_data/coffee.tif')

   In [3]: reader
   Out[3]: TiffReader('example_data/coffee.tif')

   In [4]: reader.read()
   Out[4]: dask.array<from-value, shape=(400, 600, 3), dtype=uint8, chunksize=(400, 600, 3), chunktype=numpy.ndarray>

   In [5]: reader.read().compute()
   <numpy array output, snipped>

   In [6]: reader.close()
   ```

   Use the reader as a context manager.

   ```py
   In [7]: with tifffile_reader.TIFFReader('example_data/coffee.tif') as reader:
      ...:     subsection = reader.read()[0, 0].compute()
   ```

   Try a TIFF series and stack as well.

   ```py
   In [3]: tifffile_reader.TIFFReader('example_data/series/*.tif').read().shape
   Out[3]: (200, 25, 25)

   In [4]: tifffile_reader.TIFFReader('example_data/lfw_subset_as_stack.tif').read().shape
   Out[4]: (200, 25, 25)
   ```
