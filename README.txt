INSTRUCTIONS ON HOW TO GENERATE DOCUMENTATION:

You must install Sphinx. We use Sphinx to generate the documentation (html files 
and a pdf file). Read about installation here: http://www.sphinx-doc.org/en/stable/install.html
Note: The conf.py file is the Sphinx configuration file. This should only be
edited if you know what you are doing with documentation.

Once Sphinx is installed, change directories to repo-name/documentation.

To create html files, type the command:
> make html

To create a pdf, type the command:
> make latexpdf

Sometimes it is useful to clean out the _build directory. You can do this by 
typing the command:
> make clean

Both the html files and the pdf file will be generated in the 
repo-name/documentation/_build directory. Note: This directory is ignored in the 
.hgignore file.

Work Flow:
To update the documentation.pflotran.org website with the documentation, 
follow these instructions step-by-step:
1. If you haven't already run the QA test suite, run the QA test suite.
This will generate the figures and the report card.
You do this by changing directories to repo-name/qa_tests, and reading
the directions there (in README).
2. Generate the pdf of the documentation by changing into the directory
repo-name/documentation and typing in
> make latexpdf
Note: You must generate the pdf before you generate the html files!! The pdf
file must be created first so that the website build can use it. 
3. Now that the pdf is created, create the html files by typing in
> make html
4. Check that the website looks the way you want it to look by opening up your
local copy of the website in a browser. You can do this by opening the file
repo-name/documentation/_build/html/index.html; If everything looks good, 
proceed. If not, fix it and try again.
5. Create a tar ball of the website by changing into the directory
repo-name/documentation/_build/html and typing in
> tar -czvf website.tar.gz *
Note the * after the file name - don't forget that!
6. Transfer the file website.tar.gz to pflotran.org in the directory
public_html/documentation and untar the file by typing in
> tar -xzvf website.tar.gz
Note: If you do not have access to the pflotran.org server, then create a pull
request of your documentation changes and one of the PFLOTRAN developers will
review your documentation changes and update the website if the changes are
approved.
7. Done! Check the website to confirm it was updated.