from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text


a= Flask(__name__)

jobs=[{'S.no':1, 'Name': 'DAYALAN', 'Age':10},{'S.no':2, 'Name': 'DAY', 'Age':11},{'S.no':3, 'Name': 'DAYPRA', 'Age':13},{'S.no':4, 'Name': 'PRAVEEN', 'Age':15},{'S.no':5, 'Name': 'PRAV', 'Age':13}]

def load_details_from_db():
  with engine.connect() as conn:
    c= conn.execute(text("select * from vetri"))
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

@a.route("/about")
def about():
  return jsonify(jobs)
  
if __name__ == '__main__':
  a.run(host='0.0.0.0' , debug=True)

