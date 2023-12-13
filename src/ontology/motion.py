from owlready2 import *

onto = get_ontology("http://www.ease-crc.org/ont/mixing")

with onto:
    class Motion(Thing):
        pass


    class MixingMotion(Motion):
        pass


    class CircularMotion(MixingMotion):
        pass


    class WhirlstormMotion(MixingMotion):
        pass


    class VerticalCircularMotion(MixingMotion):
        pass

    class CircularDivingToInner(MixingMotion):
        pass
