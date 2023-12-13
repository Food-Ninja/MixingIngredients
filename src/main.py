from ontology.container import *
from ontology.task import *
from ontology.motion import *
from ontology.ingredient import *

from ontology.rules import *

task = StirringTask("task")
pot = Pot("pot")
spoon = WoodenSpoon("wooden_spoon")
whisk = Whisk("whisk")
mixer = Mixer("mixer")
fork = Fork("fork")
bowl = Bowl("bowl")
cup = Cup("cup")
mug = Mug("mug")
ing = Flour("flour")
ing2 = Sugar("sugar")
ing3 = Water("water")
motion = Motion("motion")

sync_reasoner_pellet(infer_property_values=True, infer_data_property_values=True)

print(task.performMotion[0].is_a)
#print(task.useContainer[0].is_a)
#print(task.useTool[0].is_a)

# onto.save(file="mixing", format="rdfxml")
