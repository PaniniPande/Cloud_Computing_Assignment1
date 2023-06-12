
from flask import Flask, render_template, request
import pyodbc

app = Flask(__name__)

@app.route('/')
def Home():
   return render_template('Home.html')

@app.route('/SalaryRange')
def SalaryRange():
   return render_template('SalaryRange.html')

@app.route('/UpdateSalary')
def UpdateSalary():
   return render_template('UpdateSalary.html')

@app.route('/Delete')
def remove():
   return render_template('Delete.html')

@app.route('/FindPerson')
def FindPerson():
   return render_template('FindPerson.html')

@app.route('/UploadPicture')
def UploadPicture():
   return render_template('UploadPicture.html')

@app.route('/UpdateKey')
def UpdateKey():
   return render_template('UpdateKey.html')

@app.route('/AddPicture')
def addpic():
   return render_template('AddPicture.html')

Panini_driver = '{ODBC Driver 18 for SQL Server}'
Panini_database = 'ADB'
Panini_server = 'tcp:adbassignments15.database.windows.net,1433'
Panini_username = "pxp4144"
Panini_password = "Paridhi@15"
Panini_conn= pyodbc.connect('DRIVER='+Panini_driver+';SERVER='+Panini_server+';DATABASE='+Panini_database+';UID='+Panini_username+';PWD='+ Panini_password)
Panini_cursor = Panini_conn.cursor() 

@app.route('/all', methods=['POST','GET'])
def full_Details():
    Panini_query="Select * from People "
    Panini_cursor.execute(Panini_query)
    Panini_rows = Panini_cursor.fetchall()
    return render_template("Details.html",rows = Panini_rows)

@app.route('/UpdateSalary',methods=['POST','GET'])
def update_sal():
    if (request.method=='POST'):
        Panini_name= str(request.form['name'])
        Panini_keyword= str(request.form['sal'])
        Panini_query="UPDATE People SET salary = '"+Panini_keyword+"'   WHERE Name ='"+Panini_name+"' "
        Panini_cursor.execute(Panini_query)
        Panini_conn.commit()
        Panini_query2="Select * from People "
        Panini_cursor.execute(Panini_query2)
        Panini_rows = Panini_cursor.fetchall()
        
    return render_template("Details.html",rows = Panini_rows)

@app.route('/UpdateKey',methods=['POST','GET'])
def updatek():
    if (request.method=='POST'):
        Panini_name= str(request.form['name'])
        Panini_keyword= str(request.form['keyword'])
        Panini_query="UPDATE People SET keywords = '"+Panini_keyword+"'   WHERE Name ='"+Panini_name+"' "
        Panini_cursor.execute(Panini_query)
        Panini_conn.commit()
        Panini_query1="Select * from People "
        Panini_cursor.execute(Panini_query1)
        Panini_rows = Panini_cursor.fetchall()
    return render_template("Details.html",rows = Panini_rows)

@app.route('/AddPicture',methods=['POST','GET'])
def addpicture():
    if (request.method=='POST'):
        Panini_name= str(request.form['name1'])
        Panini_pic= str(request.form['pic1'])
        Panini_query="UPDATE People SET Picture = '"+Panini_pic+"'   WHERE Name ='"+Panini_name+"' "
        Panini_cursor.execute(Panini_query)
        Panini_conn.commit()
        Panini_query1="Select * from People "
        Panini_cursor.execute(Panini_query1)
        Panini_rows = Panini_cursor.fetchall()
    return render_template("Details.html",rows = Panini_rows)



@app.route('/SalaryRange', methods=['GET', 'POST'])
def notmatch():
    if (request.method=='POST'):
        Panini_SalRange= (request.form['range'])
        Panini_query="select * from People WHERE Salary  <"+Panini_SalRange+""
        Panini_cursor.execute(Panini_query)
        Panini_rows = Panini_cursor.fetchall()
    return render_template("UploadPicture.html",rows = Panini_rows)

@app.route('/Delete', methods=['GET', 'POST'])
def deleterecord():
    if (request.method=='POST'):
        Panini_name= str(request.form['name'])
        Panini_query="DELETE FROM People WHERE Name ='"+Panini_name+"' "
        Panini_cursor.execute(Panini_query)
        Panini_conn.commit()
        Panini_query1="Select * from People"
        Panini_cursor.execute(Panini_query1)
        Panini_rows = Panini_cursor.fetchall()
    return render_template("Details.html",rows = Panini_rows)

@app.route('/FindPerson_deets', methods=['POST','GET'])
def Details():
    Panini_field=str(request.form['name'])
    Panini_query="Select * from People WHERE Name =  '"+Panini_field+"' "
    Panini_cursor.execute(Panini_query)
    Panini_rows = Panini_cursor.fetchall()
    return render_template("UploadPicture.html",rows = Panini_rows)

if __name__ =="__main__":
    app.run(debug=True)
    