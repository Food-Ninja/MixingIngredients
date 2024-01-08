from owlready2 import *

onto = get_ontology("http://www.ease-crc.org/ont/mixing")

with onto:
    class motion_parameters(DataProperty):
        pass


    class angle_shift1(motion_parameters):
        pass


    class angle_shift2(motion_parameters):
        pass


    class height_increment(motion_parameters):
        pass


    class radius_lower_bound(motion_parameters):
        pass


    class radius_upper_bound(motion_parameters):
        pass


    class vertical_increment(motion_parameters):
        pass


    class Motion(Thing):
        label = [locstr("motion", "en")]


    class MixingMotion(Motion):
        label = [locstr("mixing motion", "en")]


    class CircularDivingToInnerMotion(MixingMotion):
        label = [locstr("circular diving to inner motion", "en")]
        is_a = [radius_lower_bound.value(0.0) & radius_upper_bound.value(0.7),
                height_increment.value(0.1)]


    class CircularMotion(MixingMotion):
        label = [locstr("circular motion", "en")]
        is_a = [radius_lower_bound.value(0.8) & radius_upper_bound.value(0.7)]


    class FoldingMotion(MixingMotion):
        label = [locstr("folding motion", "en")]
        is_a = [radius_lower_bound.value(0.0) & radius_upper_bound.value(0.7),
                angle_shift1.value(90), angle_shift2.value(22.5)]


    class VerticalCircularMotion(MixingMotion):
        label = [locstr("vertical circular motion", "en")]
        is_a = [radius_lower_bound.value(0.0) & radius_upper_bound.value(0.7),
                vertical_increment.value(0.1)]


    class WhirlstormMotion(MixingMotion):
        label = [locstr("whirlstorm motion", "en")]
        is_a = [radius_lower_bound.value(0.0) & radius_upper_bound.value(0.7)]
