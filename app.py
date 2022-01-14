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
        
        print(inventory)
        editList = []
        # if len(editItem) != 0:
        editItem = "dog"
        for i in range(len(inventory)):
                row = inventory[i]
                print(row)
                element = row.split(',')
                item = element[0]
                print(item)
                if item == editItem:
                        item = updatedItem

                itemDate = element[1]
                itemID = element[2]
                editList.append(row)
                if editItemID == itemID:
                        print("updating")
                        item = updatedItem
                cleanRow = {
                        'cleanItem': item,
                        'cleanDate': itemDate,
                        'cleanID': itemID
                }

                cleanFile.append(cleanRow)
                        

        # myfile.close()
        print(cleanFile)
        with open('inventory.csv','w') as myfile:
                for i in range(len(editList)):
                        row = editList[i]
                        element = row.split(',')
                        item = element[0]
                        itemDate = element[1]
                        itemID = element[2]
                        myfile.write(item)
                        myfile.write(',')
                        myfile.write(itemDate)
                        myfile.write(',')
                        myfile.write(itemDate+'\n')


        # print(cleanFile)
        return {'cleanListing': cleanFile}
        
        # return cvsDisplay()

                # elif len(deleteItem) != 0:
                #         for i in range(len(inventory)):
                #                 row = inventory[i]
                #                 element = row.split(',')
                #                 item = element[0]
                #                 itemDate = element[1]
                #                 cleanRow = {
                #                         'cleanItem': item,
                #                         'cleanDate': itemDate
                #                 }
                #                 if cleanRow[0] == request.args.get("deleteItem"):
                #                         cleanRow[0] = ""
                #                         cleanRow[1] = ""
                #                 cleanFile.append(cleanRow)
                #                 i = i + 1
                # with open('inventory.csv', 'w') as myfile:
                #         myfile.write(cleanFile)
                #         cleanFile = []
        # else:
        #         for i in range(len(inventory)):
        #                 row = inventory[i]
        #                 element = row.split(',')
        #                 item = element[0]
        #                 itemDate = element[1]
        #                 cleanRow = {
        #                         'cleanItem': item,
        #                         'cleanDate': itemDate
        #                 }
        #                 cleanFile.append(cleanRow)
        #         print(cleanFile)

        #         return {'cleanListing': cleanFile}
                
                # make a list then send them all at once instead of one at a time that way you can still edit
        

# ===============================================================================
if __name__ == '__main__':
        app.run(debug=True, host="0.0.0.0", port=9000)