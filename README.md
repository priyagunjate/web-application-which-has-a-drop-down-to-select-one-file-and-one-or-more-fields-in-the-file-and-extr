# web-application-which-has-a-drop-down-to-select-one-file-and-one-or-more-fields-in-the-file-and-extr
I have a bunch of files in CSV format (with same set of fields) and to aid non-programmers I need to make it easy to access the same. Can you develop a web application which has a drop-down to select one file and one or more fields in the file and extract the information? Write both the front-end code and back-end code.


# vDOCUMENTATION :

### 1. Install virtualenv for development environment
   pip install virtualenv

After Installation, Create “upload_data” folder
mkdir upload_data
cd upload_data
virtualenv venv
venv\scripts\activate
pip install Flask

Output window:
 

Folder Introduction:
•	File_path folder :-contains bunch of csv file
•	 Templates folder :- contains “dropdown.html”  html file
•	App.py is python program file

App.py file : 
This is a flask program file .
 
 
Fig:cmd window to run app.py file
 
 
Fig:html code










After running the above code from Python Shell. Visit the URL http://localhost:5000/index in the browser. Thus we get following website.
 
 
Fig: Final output window


# Read The Documentation File for more details.
