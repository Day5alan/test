from flask import Flask, render_template,jsonify, request
from database import engine
from sqlalchemy import text


a= Flask(__name__)

jobs=[{'S.no':1, 'Name': 'DAYALAN', 'Age':10},{'S.no':2, 'Name': 'DAY', 'Age':11},{'S.no':3, 'Name': 'DAYPRA', 'Age':13},{'S.no':4, 'Name': 'PRAVEEN', 'Age':15},{'S.no':5, 'Name': 'PRAV', 'Age':13}]

def load_details_from_db():
  with engine.connect() as con:
    c= con.execute(text("select * from vetri"))
    column_names= c.keys()  
    d = [dict(zip(column_names, row)) for row in c.fetchall()]
    total = []
    for row in d:
      total.append(row)
    return total
    
@a.route("/")
def index():
  total = load_details_from_db()
  return render_template("indexss.html", b =jobs, c= total) 

def load_dynamic_data():
  with engine.connect() as con:
    c= con.execute(text("select * from form"))
    column_name= c.keys()
    d = [dict(zip(column_name, row)) for row in c.fetchall()]
    totals = []
    for row in d:
      totals.append(row)
    return totals

@a.route("/application")
def application():
  totals= load_dynamic_data()
  return render_template("form.html", i= totals) 


@a.route("/application/apply", methods=['post'])
def export_data():
  day = request.form
  exports_data(day)
  return jsonify(day)
  


def exports_data(m):
  with engine.connect() as conn:
    try:
      query = text("INSERT INTO form (college, department, idname, location) VALUES (:college, :department, :idname, :location)")
      conn.execute(query,{
                "college": m["college"],
                "department": m["department"],
                "idname": m["idname"],
                "location": m["location"]
            })
      conn.commit()
    except Exception as e:
            print("Error inserting data into the database:", e)

if __name__ == '__main__':
  a.run(host='0.0.0.0' , debug=True)

