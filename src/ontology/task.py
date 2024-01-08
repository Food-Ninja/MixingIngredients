from owlready2 import *

onto = get_ontology("http://www.ease-crc.org/ont/mixing")

with onto:
    class Task(Thing):
        label = [locstr("task", "en")]


    class BeatingTask(Task):
        label = [locstr("beating task", "en")]


    class FoldingTask(Task):
        label = [locstr("folding task", "en")]


    class MixingTask(Task):
        label = [locstr("mixing task", "en")]


    class StirringTask(Task):
        label = [locstr("stirring task", "en")]


    class WhiskingTask(Task):
        label = [locstr("whisking task", "en")]
