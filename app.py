from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import csv
import json

from datetime import date
app = Flask(__name__, static_folder = 'static', template_folder = 'templates')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
CORS(app)

# ===============================================================================

# Render Home Page
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/newitem')
def newitem():
        item = request.args.get("item")
        currentDate = date.today()
        newListing = [
                item,
                currentDate
        ]
        with open('inventory.csv', 'a', newline='\n')as file:
                writer = csv.writer(file)
                writer.writerow(newListing)
        return {"inventoryList": newListing}, 201

@app.route('/cvsDisplay')
def cvsDisplay():
        cvsFile = open('inventory.csv', 'r')
        inventory = cvsFile.readlines()
        cvsFile.close

        cleanFile = []
        
        for i in range(len(inventory)):
                row = inventory[i]
                element = row.split(',')
                item = element[0]
                itemDate = element[1]
                cleanRow = {
                        'cleanItem': item,
                        'cleanDate': itemDate
                }
                cleanFile.append(cleanRow)

        return {'cleanListing': cleanFile}

@app.route('/edit')
def edit():
        cvsFile = open('inventory.csv', 'r')
        inventory = cvsFile.readlines()
        cvsFile.close

        cleanFile = []
        for i in range(len(inventory)):
                inventory[i] = inventory[i].strip()
                cleanFile = []
                if request.args.get("editItem") > 0:
                        for i in range(len(inventory)):
                                row = inventory[i]
                                element = row.split(',')
                                item = element[0]
                                itemDate = element[1]
                                cleanRow = {
                                        'cleanItem': item,
                                        'cleanDate': itemDate
                                }
                                if cleanRow[0] == request.args.get("editItem"):
                                        cleanRow[0] = request.args.get("updateInput")

                                cleanFile.append(cleanRow)
                elif request.args.get("deleteItem") > 0:
                        for i in range(len(inventory)):
                                row = inventory[i]
                                element = row.split(',')
                                item = element[0]
                                itemDate = element[1]
                                cleanRow = {
                                        'cleanItem': item,
                                        'cleanDate': itemDate
                                }
                                if cleanRow[0] == request.args.get("deleteItem"):
                                        cleanRow[0] = ""
                                        cleanRow[1] = ""
                                cleanFile.append(cleanRow)
                with open('inventory.csv', 'w') as myfile:
                        myfile.write(cleanFile)
                cvsDisplay()
                
        

# ===============================================================================
if __name__ == '__main__':
        app.run(debug=True, host="0.0.0.0", port=9000)