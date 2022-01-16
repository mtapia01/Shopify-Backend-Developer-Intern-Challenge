from math import radians
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import csv
import random
import pdb
import re


from datetime import date
app = Flask(__name__, static_folder = 'static', template_folder = 'templates')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
CORS(app)

# ===============================================================================

# Render Home Page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/inventoryFile')
def inventoryFile():
        return cvsDisplay()

@app.route('/newitem')
def newitem():
        item = request.args.get("item")
        currentDate = date.today()

        cvsFile = open('inventory.csv', 'r')
        inventory = cvsFile.readlines()
        cvsFile.close

        randomNumber = list(range(1000))
        random.shuffle(randomNumber)
        id = randomNumber.pop()

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
                                
        with open('inventory.csv', 'r+') as f:
                data = f.read()
                f.seek(0)
                for i in range(len(inventory)):
                        row = inventory[i]
                        element = row.split(',')
                        item = element[0]

                        if item == editItemID:
                                item = updatedItem
                        

                        itemDate = element[1]
                        
                        itemID = element[2]

                        cleanRow = {
                                'cleanItem': item,
                                'cleanDate': itemDate,
                                'cleanID': itemID
                        }
                        f.write(item)
                        f.write(',')
                        f.write(itemDate)
                        f.write(',')
                        f.write(itemID)
                        f.truncate()
                f.close()
                cleanFile.append(cleanRow)

        return {'cleanListing': cleanFile}     

@app.route('/delete')
def delete():
        cvsFile = open('inventory.csv', 'r')
        inventory = cvsFile.readlines()
        cvsFile.close

        editItemID = request.args.get("delItem")       

        cleanFile = []

        with open('inventory.csv', 'r+') as f:
                data = f.read()
                f.seek(0)
                for i in range(len(inventory)):
                        row = inventory[i]
                        element = row.split(',')
                        item = element[0]
                        itemDate = element[1]
                        itemID = element[2]

                        if item == editItemID:
                                print("deleting")
                                del item
                                del itemDate
                                del itemID
                        else:
                                cleanRow = {
                                        'cleanItem': item,
                                        'cleanDate': itemDate,
                                        'cleanID': itemID
                                }
                                f.write(item)
                                f.write(',')
                                f.write(itemDate)
                                f.write(',')
                                f.write(itemID)
                                f.truncate()
                        cleanFile.append(cleanRow)
                f.close()
        return {'cleanListing': cleanFile}     

# ===============================================================================
if __name__ == '__main__':
        app.run(debug=True, host="0.0.0.0", port=9000)