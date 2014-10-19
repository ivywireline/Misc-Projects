About:

This school project aims to identify the authors of mysterious files. There are mysterious files,
author_function.py, author_program.py and .stat files in the repository. Python 3.3 or above is required
in order to run author_program.py. 

The author_program.py imports functions written in
author_functions.py to generate the 5 signature numbers(explained below Procedure) 
of a mysterious file and then match the result with
each of the author's signature .stat files to see which
author's signature stats have the closest approximations to
the mysterious file. This author will then be considered as the most
likely person to have written the content in the mysterious
files.

Procedure:

1) Git clone the link provided in the repository.
2) Open and run the author_program.py in a Python IDE or Shell.
3) Type in one of the mysterious files names with .txt extension. E.g.
 
>>> Enter the name of the file with unknown author: mystery1.txt

4) Type in the directory where the author's signature .stat files are located. E.g.

>>> Enter the path to the directory of signature files: C:\Users\STEVEN\Desktop\Authorship detection\Signature Files

5) Wait for the execution to be finished. Due to the fact that each mysterious file contains
a whole novel, the execution may take 1 or 2 hours and even more depending on the computer.

The authorship detection project cotains premade stats files for authors
Agatha Christie, Alexandre Dumas, Brothers Grim, Charles Dickens,
Douglas Adams, Emily Bronte, Fyodor Dostoevsky, James Joyce,
Jane Austen, Lewis Caroll, Mark Twain, Sir Arthur Conan Doyle
and William Shakespeare. 

Each .stat file contains 5 numbers and they respectively
represent the average word ength,type token ratio, 
hapax legomena ratio, average sentence length and
average sentence complexity in the text made by the author.
Type token ratio and hapax legomena ratio are both measures of how repetitive the author
uses words. The collection of these numbers creates the signature or 
identity for the author.

Link to the description of the project: http://www.cdf.toronto.edu/~csc108h/winter/assignments/a2/index.shtml
