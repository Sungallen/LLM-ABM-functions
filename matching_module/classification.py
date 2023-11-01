import json 
from transformers import pipeline
import numpy as np
import os

class location_register():
    def __init__(self) -> None:
        self.candidate_labels = ["Accommodation", "Commercial", "Religious", "Civic", "Agricultural", "Sports", "Storage", "Power", "Other"]

        self.classifier = pipeline("zero-shot-classification", model="MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli")
        self.building_category = dict
        self._read_building_category()

    def _read_building_category(self):
        working_directory = os.getcwd()
        file_path = working_directory + '/matching_module/building_category.json'
        with open(file_path, 'r') as f:
            self.building_category = json.loads(f.read())['building_category']


    def output(self, input: str, categoty: str):
        tmp =  self.classifier(input, self.building_category[categoty], multi_label=False) 
        labels = tmp['labels']
        scores = np.argsort([-s for s in tmp['scores']])
        print(f"{input} + {categoty} == {labels[scores[0]]}")
        return labels[scores[0]]
    
    def output2(self, input: str):
        building_category = [b for index, b in enumerate(self.building_category)]
        tmp =  self.classifier(input, building_category, multi_label=False) 
        labels = tmp['labels']
        scores = np.argsort([-s for s in tmp['scores']])
        print(123, input)

        print(f"{input} >>> building category: {labels[scores[0]]}")
        return labels[scores[0]]




if __name__ == "__main__":
    lr = location_register()
    # ans = lr.output('Activity: Client Meetings', 'Commercial')
    # Or: file_path = os.path.join(working_directory, 'my_file.py')
   
    ans = lr.output2('Activity: Client Meetings',)
    print(ans)