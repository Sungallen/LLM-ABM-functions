import openai

from .broad.broadCall import broadCall
from .broad.data.instructions import instructions
from .broad.data.broadSchedule import functions

from .narrow.narrowCall import narrowCall
from .narrow.data.functions import createNarrow
from .narrow.data.narrowPrompt import narrowPrompt

def scheduler(info):
    broadSchedule = broadCall(instructions, info, functions)
    broadSchedule = eval(broadSchedule)
    schedule = {}
    for hour in range(24):
        activity = broadSchedule[f"{hour}:00 Activity"]  
        place = broadSchedule[f"{hour}:00 Place"]
        narrowSchedule = eval(narrowCall(narrowPrompt + f" the person is doing {activity} in {place}", demo, createNarrow(hour)))
        schedule.update({f"{hour}:00": narrowSchedule})
        print(f"Epoch {hour + 1}/24")
    return schedule
