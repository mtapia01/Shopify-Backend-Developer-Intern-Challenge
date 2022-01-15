from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import csv
import json
import uuid

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

        cvsFile = open('inventory.csv', 'r')
        inventory = cvsFile.readlines()
        cvsFile.close
        id = len(inventory) + 1

        newListing = [
                item,
                currentDate,
                id
        ]
        with open('inventory.csv', 'a', newline='\n')as file:
                writer = csv.writer(file)
                writer.writerow(newListing)
        file.close()
        return {"inventoryList": newListing}, 201

@app.route('/cvsDisplay')
def cvsDisplay():
        cvsFile = open('inventory.csv', 'r')
        inventory = cvsFile.readlines()
        cvsFile.close

        for i in range(len(inventory)):
                inventory[i] = inventory[i].strip()

        cleanFile = []

        for i in range(len(inventory)):
                row = inventory[i]
                element = row.split(',')
                item = element[0]
                itemDate = element[1]
                itemID = element[2]
                cleanRow = {
                        'cleanItem': item,
                        'cleanDate': itemDate,
                        'id': "id:"+itemID
                }
                cleanFile.append(cleanRow)

        return {'cleanListing': cleanFile}

@app.route('/edit')
def edit():
        cvsFile = open('inventory.csv', 'r')
        inventory = cvsFile.readlines()
        cvsFile.close

        editItemID = request.args.get("oldItem")

        updatedItem = request.args.get("newItem")        

        cleanFile = []
        
        editList = []

        for i in range(len(inventory)):
                row = inventory[i]
                element = row.split(',')
                item = element[0]

                if item == editItemID:
                        item = updatedItem

                itemDate = element[1]
                itemID = element[2]
                if itemID == editItemID[0]:
                        item = updatedItem
                editList.append(row)
                
                cleanRow = {
                        'cleanItem': item,
                        'cleanDate': itemDate,
                        'cleanID': itemID
                }
                cleanFile.append(cleanRow)
        # print(cleanFile)
                        
        with open('inventory.csv', 'r+') as f:
                data = f.read()
                f.seek(0)
                for i in range(len(cleanFile)):
                        f.write(item)
                        f.write(',')
                        f.write(itemDate)
                        f.write(',')
                        f.write(itemID)
                f.truncate()
        f.close()
        return {'cleanListing': cleanFile}     

@app.route('/delete')
def delete():
        cvsFile = open('inventory.csv', 'r')
        inventory = cvsFile.readlines()
        cvsFile.close

        editItemID = request.args.get("delItem")       

        cleanFile = []
        
        for i in range(len(inventory)):
                row = inventory[i]
                element = row.split(',')
                item = element[0]
                if item == editItemID:
                        print("deleting")
                else:
                        row = inventory[i]
                        element = row.split(',')
                        itemDate = element[1]
                        itemID = element[2]
                # if item == editItemID:
                #         del item
                #         del itemDate
                #         del itemID
                # editList.append(row)
                        cleanRow = {
                                'cleanItem': item,
                                'cleanDate': itemDate,
                                'cleanID': itemID
                        }
                        cleanFile.append(cleanRow)
        with open('inventory.csv', 'r+') as f:
                data = f.read()
                f.seek(0)
                for i in range(len(cleanFile)):
                        f.write(item)
                        f.write(',')
                        f.write(itemDate)
                        f.write(',')
                        f.write(itemID)
                f.truncate()
        f.close()
        return {'cleanListing': cleanFile}     

# ===============================================================================
if __name__ == '__main__':
        app.run(debug=True, host="0.0.0.0", port=9000)