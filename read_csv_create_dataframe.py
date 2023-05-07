import pandas

def read_csv_file(file_name):
    # read data from csv file using pandas.
    data = pandas.read_csv(f"{file_name}")
    # changing data to list of dictionaries
    data_dict_in_list = data.to_dict(orient='records')
    return data_dict_in_list

def upload_data_to_file(file_name, data_dict_in_list):
    # creating data frame using pandas and adding data of list of dictionaries in data frame.
    data_frame = pandas.DataFrame(data_dict_in_list)
    # converting data frame into csv file and index False means the index is not written in csv file.
    data_frame.to_csv(f"{file_name}", index=False)

def upload_room_data_in_write_mood(room_data):
    data_frame = pandas.DataFrame(room_data)
    data_frame.to_csv("room_allotment.csv", mode="w", header=True, index=False)