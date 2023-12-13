from owlready2 import *

onto = get_ontology("http://www.ease-crc.org/ont/mixing")

with onto:
    class Task(Thing):
        pass

    class StirringTask(Task):
        pass

    class MixingTask(Task):
        pass

    class BeatingTask(Task):
        pass

    class WhiskTask(Task):
        pass