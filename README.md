# PyCrash - simple Python Virus

- PyCrash is a simple virus written in Python that damage PDF files permanently
  by adding watermark to them.

- The virus can spread itself by injecting the virus code into .py files that
  found in the current directory where the virus resides.

- The virus is somewhat intelligent, it infects a file only once i.e while the virus
  is spreading itself by injecting the code into other .py files, if the file is already
  infected by the virus, it will not infect it again.

- Infected python files contain the virus code besides their original source code so when
  they get executed, they act as a virus and infect other python files that reside in the
  same directory as that of the current python file.
