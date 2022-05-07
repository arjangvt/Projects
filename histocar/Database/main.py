import sys
sys.path.insert(0, '../')

from Database.DBSampleData import DBSampleData

def main():
    data_make_list = []
    
    # Make starts here  
    data_make = {}
    data_make["id"] = 1
    data_make["vehicle_makes"] = "Ferrari"
    data_make_list.append(data_make)

    data_make = {}
    data_make["id"] = 2
    data_make["vehicle_makes"] = "Jaguar"
    data_make_list.append(data_make)

    data_make = {}
    data_make["id"] = 3
    data_make["vehicle_makes"] = "Testla"
    data_make_list.append(data_make)

    data_make = {}
    data_make["id"] = 4
    data_make["vehicle_makes"] = "Lamborghini"
    data_make_list.append(data_make)

    data_make = {}    
    data_make["id"] = 5
    data_make["vehicle_makes"] = "Porsche"
    data_make_list.append(data_make)

    data_make = {}    
    data_make["id"] = 6
    data_make["vehicle_makes"] = "Toyota"
    data_make_list.append(data_make)

    data_make = {}        
    data_make["id"] = 7
    data_make["vehicle_makes"] = "Bugatti"
    data_make_list.append(data_make)

    data_make = {}        
    data_make["id"] = 8
    data_make["vehicle_makes"] = "Maserati"
    data_make_list.append(data_make)

    data_make = {}        
    data_make["id"] = 9
    data_make["vehicle_makes"] = "BMW"
    data_make_list.append(data_make)

    data_make = {}        
    data_make["id"] = 10
    data_make["vehicle_makes"] = "Aston Martin"
    data_make_list.append(data_make)

    data_make = {}        
    data_make["id"] = 11
    data_make["vehicle_makes"] = "Bentley"
    data_make_list.append(data_make)

    # Model list starts here
    data_model_list = []
    data_model = {}
    data_model["id"] = 1  # Jaguar
    data_model["vehicle_make_id"] = 2
    data_model["model"] = "XJ"
    data_model_list.append(data_model)

    data_model = {}
    data_model["id"] = 2
    data_model["vehicle_make_id"] = 3  # Tesla
    data_model["model"] = "Model S"
    data_model_list.append(data_model)

    data_model = {}
    data_model["id"] = 3
    data_model["vehicle_make_id"] = 3  # Tesla
    data_model["model"] = "Model X"
    data_model_list.append(data_model)

    data_model = {}
    data_model["id"] = 4
    data_model["vehicle_make_id"] = 4 # Lamborghini
    data_model["model"] = "Huracan"
    data_model_list.append(data_model)

    data_model = {}
    data_model["id"] = 5
    data_model["vehicle_make_id"] = 4 # Lamborghini
    data_model["model"] = "Urus"
    data_model_list.append(data_model)

    data_model = {}
    data_model["id"] = 6
    data_model["vehicle_make_id"] = 5 # Lamborghini
    data_model["model"] = "Aventador"
    data_model_list.append(data_model)

    data_model = {}
    data_model["id"] = 7
    data_model["vehicle_make_id"] = 1 # Ferrari
    data_model["model"] = "360"
    data_model_list.append(data_model)
 
    data_model = {}
    data_model["id"] = 8
    data_model["vehicle_make_id"] = 1 # Ferrari
    data_model["model"] = "F430"
    data_model_list.append(data_model)

    data_model = {}
    data_model["id"] = 9
    data_model["vehicle_make_id"] = 5 # Porsche
    data_model["model"] = "911"
    data_model_list.append(data_model)

    data_model = {}
    data_model["id"] = 10
    data_model["vehicle_make_id"] = 5 # Porsche
    data_model["model"] = "Boxter"
    data_model_list.append(data_model)

    data_model = {}
    data_model["id"] = 11
    data_model["vehicle_make_id"] = 5 # Porsche
    data_model["model"] = "Cayman"
    data_model_list.append(data_model)

    data_model = {}
    data_model["id"] = 12
    data_model["vehicle_make_id"] = 7 # Bugattie
    data_model["model"] = "Chiron"
    data_model_list.append(data_model)

    data_model = {}
    data_model["id"] = 13
    data_model["vehicle_make_id"] = 8 # Maserati
    data_model["model"] = "GranTurismo"
    data_model_list.append(data_model)

    data_model = {}
    data_model["id"] = 14
    data_model["vehicle_make_id"] = 8 # Maserati
    data_model["model"] = "Levante"
    data_model_list.append(data_model)

    data_model = {}
    data_model["id"] = 15
    data_model["vehicle_make_id"] = 8 # Maserati
    data_model["model"] = "Spyder"
    data_model_list.append(data_model)

    data_model = {}
    data_model["id"] = 16
    data_model["vehicle_make_id"] = 9 # BMW
    data_model["model"] = "M6"
    data_model_list.append(data_model)

    data_model = {}
    data_model["id"] = 17
    data_model["vehicle_make_id"] = 10 # Aston Martin
    data_model["model"] = "V12 Vantage"
    data_model_list.append(data_model)

    data_model = {}
    data_model["id"] = 18
    data_model["vehicle_make_id"] = 11 # Aston Martin
    data_model["model"] = "DB11"
    data_model_list.append(data_model)

    data_model = {}
    data_model["id"] = 19
    data_model["vehicle_make_id"] = 12 # Aston Martin
    data_model["model"] = "Continental"
    data_model_list.append(data_model)



    # Trim starts here
    data_trim_list = []
    data_trim = {}
    data_trim['id'] = 1
    data_trim["vehicle_model_id"] = 1  #Jaguar
    data_trim["trim"] = "R Sport"
    data_trim_list.append(data_trim)

    data_trim = {}
    data_trim['id'] = 2
    data_trim["vehicle_model_id"] = 1  #Jaguar
    data_trim["trim"] = "XJL Portfolio"
    data_trim_list.append(data_trim)

    data_trim = {}
    data_trim['id'] = 3
    data_trim["vehicle_model_id"] = 1  #Jaguar
    data_trim["trim"] = "XJ50 V6"
    data_trim_list.append(data_trim)

    data_trim = {}
    data_trim['id'] = 4
    data_trim["vehicle_model_id"] = 1  #Jaguar
    data_trim["trim"] = "XJ Supercharged"
    data_trim_list.append(data_trim)

    data_trim = {}
    data_trim['id'] = 5
    data_trim["vehicle_model_id"] = 1  #Jaguar
    data_trim["trim"] = "XJL Supercharged"
    data_trim_list.append(data_trim)

    data_trim = {}
    data_trim['id'] = 6
    data_trim["vehicle_model_id"] = 1  #Jaguar
    data_trim["trim"] = "XJ50 V8"
    data_trim_list.append(data_trim)

    data_trim = {}
    data_trim['id'] = 7
    data_trim["vehicle_model_id"] = 1  #Jaguar
    data_trim["trim"] = "XJR575"
    data_trim_list.append(data_trim)


    _dbSample = DBSampleData()
    _dbSample.InsertMake(data_make_list)
    _dbSample.InsertModel(data_model_list)
    _dbSample.InsertTrim(data_trim_list)

if __name__ == "__main__":
    main()