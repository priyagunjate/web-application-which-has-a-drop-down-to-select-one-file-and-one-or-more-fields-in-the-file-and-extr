from flask import Flask, render_template, request, url_for, redirect
import pandas as pd

app = Flask(__name__)

#@app.route('/')
@app.route('/index')
def index():
    return render_template("dropdown.html")

@app.route('/login', methods=['GET', 'POST'])

def login():
    if request.method == "POST":
        f = request.form.get("file_path")
        file_read=pd.read_csv(f)
        col=file_read.iloc[:,0].values.tolist()
        print(col)
        print(file_read)
        if request.method == "POST":
            file_value=request.form.get("value")
            for i in range(len(file_read.iloc[:,0])):
                #print(file_read.iloc[i,0])
                if  file_value == file_read.iloc[i,0]:
                    zz=file_read.iloc[i,1]
                    return zz
            
            
  
if __name__ == '__main__':
    app.run(debug=True)
    
