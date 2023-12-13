from owlready2 import *

onto = get_ontology("http://www.ease-crc.org/ont/mixing")

soma_namespace = get_ontology("http://www.ease-crc.org/ont/SOMA.owl")

with onto:
    class DesignedTool(Thing):
        namespace = soma_namespace


    class KitchenTool(DesignedTool):
        pass


    class Mixer(KitchenTool):
        pass


    class ElectricMixer(Mixer):
        pass


    class Handmixer(Mixer):
        pass


    class Whisk(KitchenTool):
        pass


    class TableWare(DesignedTool):
        namespace = soma_namespace


    class Crockery(TableWare):
        namespace = soma_namespace


    class Bowl(Crockery):
        namespace = soma_namespace


    class PastaBowl(Bowl):
        pass


    class SaladBowl(Bowl):
        pass


    class Cup(Crockery):
        namespace = soma_namespace


    class Mug(Crockery):
        pass


    class Pan(Crockery):
        namespace = soma_namespace


    class Pot(Crockery):
        namespace = soma_namespace


    class Cutlery(DesignedTool):
        namespace = soma_namespace


    class Spoon(Cutlery):
        namespace = soma_namespace


    class WoodenSpoon(Spoon):
        pass


    class Fork(Cutlery):
        pass
