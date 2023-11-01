from .methods.data.data import data
from .methods.stats import getRandom
from .methods.rules import rules

class Distro:
    def __init__(self, customPrompt = None):
        if customPrompt: self.customPrompt = customPrompt
    
    def generate(self):
        auxillary = {}
        for item in data:
            if item == "name":
                auxillary.update({item : getRandom("name", data[item])})
            elif item == "age":
                auxillary.update({item : getRandom("gaussian", data[item])})
            else:
                auxillary.update({item : getRandom("weighted", data[item])})
        auxillary = rules(auxillary)
        return auxillary
    
    def format(self, auxillary):
        formatted_paragraph = f"""
The individual, known as {auxillary['name']}, has a life experience spanning {auxillary['age']} years.
They possess an educational background in {auxillary['education']} and belong to the {auxillary['race']} ethnic group.
Their gender identity is {auxillary['gender']} and their beliefs are influenced by {auxillary['religion']} principles.
Professionally, they are {auxillary['employment']}, resulting in an income level of {auxillary['income']}.
They currently reside in {auxillary['location']}, and work as a {auxillary["occupation"]}.
Their political orientation is aligned with {auxillary['political']} ideologies, and they have participated in {auxillary['votes']} voting events.
Their immigration status is categorized as {auxillary['immigration']}.
As for health, they are {auxillary["weight"]}
In terms of personal relationships, they presently identify as {auxillary['relation']}.
        """
        return formatted_paragraph

