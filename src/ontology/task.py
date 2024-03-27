from owlready2 import *

onto = get_ontology("http://www.ease-crc.org/ont/mixing")
dul = get_ontology("http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#")

with onto:
    class Task(Thing):
        label = [locstr("task", "en")]
        namespace = dul


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

