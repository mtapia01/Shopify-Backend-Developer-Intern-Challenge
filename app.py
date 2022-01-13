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
        # print(cvsFile)
        inventory = cvsFile.readlines()
        cvsFile.close
        # print(inventory)
        
        for i in range(len(inventory)):
                inventory[i] = inventory[i].strip()

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

@app.route('/listOfItems')
def listOfItems():
        item = request.args.get('item')
        print(item)
        file = open('itemList.txt', 'a')
        file.writelines([json.dumps(item), '\n'])
        file.close()

        return "", 201

@app.route('/getItemList')
def getItemList():
        file = open('itemList.txt', 'r')
        lines = file.readlines()

        items = []

        for i in lines:
                i = i.strip()
                itemJSON = json.loads(i)
                items.append(itemJSON)
        file.close()

        return {"items": items}

# ===============================================================================
if __name__ == '__main__':
        app.run(debug=True, host="0.0.0.0", port=9000)