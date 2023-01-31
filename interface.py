from flask import Flask , render_template , request , jsonify
from utils import CellPhone




app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('home.html')
    

@app.route('/predict_cell_phone_price',methods = ['GET','POST']) 
def get_cell():
    if request.method == 'POST':
        print('we are in post method')
        data = request.form
        #Pid = request.form["ProductId"]
        Product_id  = data['ProductId']
        weight        = data['weight']
        internal_mem  = data['Internalmemory']
        ram           = data['RAM']
        RearCam       = data['RearCam']
        Front_Cam     = data['FrontCam']
        battery       = data['Battery']
        thickness     = data['Thickness']
        print(Product_id)

        # print('Product_id :',Product_id,'weight :',weight,'internal_mem :',internal_mem,'ram :',ram,
        # 'RearCam :',RearCam,'Front_cam :',Front_Cam,'battery :',battery,'thickness :',thickness)
        # 
        obj = CellPhone(Product_id,weight,internal_mem,ram,RearCam,Front_Cam,battery,thickness)
        price = obj.get_cell_price()
        fprice = 'Price of CellPhone  : '+ str(price)
        #return price
        # print(price) 
        # return jsonify({f'Predicted price of CellPhone is {price}'})
        return fprice
        # return Product_id
    else:
        return "GET"
    

if __name__== '__main__':
    app.run(host='0.0.0.0',port=8080)
          

