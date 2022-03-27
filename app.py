from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import mysql.connector as MYSQL
#from flask_ngrok import run_with_ngrok

app = Flask(__name__)
CORS(app)
#run_with_ngrok(app)

@app.route('/GetDataset', methods=['GET'])
def GetOrders():
  with open ('content/GetDataset.ddl') as ddl_file:
    sql = ddl_file.read()
  myDb = MYSQL.connect(host="147.232.40.14", user="mt830ca", passwd="eeY1ooxe", database="mt830ca")
  cursor = myDb.cursor()
  cursor.execute(sql)
  result = cursor.fetchall()
  insertObject = []
  columnNames = [column[0] for column in cursor.description]
  for record in result:
    insertObject.append( dict( zip( columnNames , record )))
  cursor.close()
  myDb.close()
  return jsonify(insertObject),200

@app.route('/CreateDataset', methods=["POST"])
def CreateOrder():
  data = request.get_json(force=True)
  dataset_dict = dict(data)
  with open ('content/InsertDataset.ddl') as ddl_file:
    sql = ddl_file.read()
  myDb = MYSQL.connect(host="147.232.40.14", user="mt830ca", passwd="eeY1ooxe", database="mt830ca")
  cursor = myDb.cursor()
  cursor.execute(sql.format(dataset_dict["FOD"],dataset_dict["LOD"],dataset_dict["ROD"],dataset_dict["TA"],dataset_dict["TurningDirection"]))
  myDb.commit()
  cursor.close()
  myDb.close()
  return jsonify("Insert"),201


if __name__ == "__main__":
    app.run()
