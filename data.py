from api import lta_data
list = []
for value in lta_data["value"]:
    if value["ChargeAmount"] != 0:
        list.append([value["VehicleType"], (value["StartTime"]), (value["ChargeAmount"])])
    else:
        pass
print(list)
vehicle_type = set([vehicle[0] for vehicle in list])
start_time = set([time[1] for time in list])
print(start_time)