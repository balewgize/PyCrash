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
  same directory as that of the current python file....and so on ... this process continues
  and nearly all python files of a user will be infected by the virus. Be careful :)

## Caution !!!

- Be careful about the PDF files, the damage is irreversible.

- Don't put the virus near your Python installation directory or any virtual environments.

- It may infect your python installation files. If it happens, at least you will need to re-install Python again
  (My virus is kind, it will not cause much damage)

## Don't worry too much, there must be a solution

# Aflem Antivirus

- I also create an antivirus for it. I don't want to be
  danger to the world but I want to rescue.

- The antivirus works based on signature. It looks for siganture of the virus
  on Python files. If the signature is found above some threshold level, it suspect
  the file may be infected by the virus.

- It has the ability to do Quick scan the current path, Custom scan any specific path,
  or Full scan the whole Drive.

- It lets a user to take actions on those files that are suspected being infected by
  the virus, like removing or recovering (if possible).
