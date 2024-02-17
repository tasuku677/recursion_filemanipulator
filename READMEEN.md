# Code Collection for Data Stream and File Operations
## Overview
There are three Python files: question.py, file_manipulator.py, and file_converter.py.

question.py is a code for a number guessing game. It was created to get familiar with backend development environment setup and to create a simple Command Line Interface (CLI) script. I developed it using Ubuntu in dual boot, Visual Studio Code, Python, and Git. When executing the Python script via CLI, it reads from standard input until the correct answer is provided or the game ends, then writes to standard output.

file_manipulator.py is a code for file operations.

file_converter.py converts Markdown files to HTML. It's implemented using Markdown, a markup language.

## Motivation
I created these scripts for practice using data streams and for practicing file operations.

## Technologies Used
Python, Markdown

## How to Use
-question.py
question.py is a code for a number guessing game. Users input the maximum and minimum values, and the game starts. The user has to guess the number prepared by the program within 10 attempts to win.

-file_manipulator.py
file_manipulator.py is a code for file operations. Users can execute the following four commands in the terminal to perform different operations:

python3 file_manipulator.py reverse inputpath outputpath: It takes the file at inputpath, reverses its content, and creates a new file with the reversed content at outputpath.

python3 file_manipulator.py copy inputpath outputpath: It creates a copy of the file at inputpath and saves it as outputpath.

python3 file_manipulator.py duplicate-contents inputpath n: It reads the content of the file at inputpath, duplicates it, and saves the duplicated content n times at inputpath.

python3 file_manipulator.py replace-string inputpath needle newstring: It searches for the string 'needle' in the content of the file at inputpath and replaces all occurrences of 'needle' with 'newstring'.

-file_converter.py
file_converter.py converts Markdown files to HTML. Use the following command: python3 file-converter.py markdown inputfile outputfile.
