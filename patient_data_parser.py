import json

def parse_my_data(filepath):
    file = open(filepath)

    patient_data = json.load(file)

    filtered_patient_data = []
    for patient in patient_data:
        filtered_patient = dict()
        for (key, value) in patient.items():
            if key != "favorite_color" and key != "favorite_food":
                filtered_patient[key] = value
        filtered_patient_data.append(filtered_patient)

    return filtered_patient_data

    # with open("filtered_patient.json", "w") as outfile:
    #     json.dump(filtered_patient_data, outfile)