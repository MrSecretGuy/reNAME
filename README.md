# reNAME

reNAME is a simple Python program that allows you to batch rename files of any given file type in a single folder. The program first asks for a path to the folder, then for a file extension to target within the folder, and finally asks for a static part of the files' new names. The files are then renamed in the format of ```staticname-X```, where the running number ```X``` is automatically formatted according to the amount of affected files of the target type in the folder. 

reNAME does __not__ target subfolders.

Please note that reNAME __will__ rename __every single__ file with the spesified file extention within the folder, so be sure that the folder contains no files that aren't supposed to be renamed.

When reNAME finishes running, a count of the files renamed will be shown.

## Usage
To use reNAME, simply run the script in your terminal and follow the prompts.
```python rename.py```
## Requirements
reNAME requires Python 3 to run.
