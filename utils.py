
import pickle
import json
import numpy as np

class CellPhone():

    def __init__(self,Product_id,weight,intrnal_mem,ram,RearCam,Front_Cam,battery,thickness):

        self.Product_id    = Product_id
        self.weight        = weight
        self.internal_mem  = intrnal_mem
        self.ram           = ram
        self.RearCam       = RearCam
        self.Front_Cam     = Front_Cam
        self.battery       = battery
        self.thickness     = thickness

    def load_model(self):
        
        with open (r'C:\Users\SAI\practice\Linear Regression Model\project_cell\cellphone_price_predictor.pkl','rb') as file:
            self.model = pickle.load(file)

        with open (r'C:\Users\SAI\practice\Linear Regression Model\project_cell\project_data.json','r') as file:
            self.json_data = json.load(file) 



    def get_cell_price(self):

        self.load_model()


        test_array = np.zeros(len(self.json_data['columns'])) 
        test_array[0] = self.Product_id
        test_array[1] = self.weight
        test_array[2] = self.internal_mem
        test_array[3] = self.ram
        test_array[4] = self.RearCam
        test_array[5] = self.Front_Cam
        test_array[6] = self.battery
        test_array[7] = self.thickness
        print(test_array)
        print('predicted_cell_phone_price :',np.around(self.model.predict([test_array])[0],2))
        resulttt = np.around(self.model.predict([test_array])[0],2)
        new_result = str(resulttt)
        print(resulttt)
        return new_result


if __name__ == '__main__':
    Product_id    = 203.0
    weight        = 135.0
    internal_mem  = 16.0
    ram           = 3.0
    RearCam       = 13.0
    Front_Cam     = 8.0
    battery       = 2610.0
    thickness     = 7.4

    obj = CellPhone(Product_id,weight,internal_mem,ram,RearCam,Front_Cam,battery,thickness)
    obj.get_cell_price()                   