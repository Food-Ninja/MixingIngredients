from owlready2 import *

onto = get_ontology("http://www.ease-crc.org/ont/mixing")

with onto:
    class Motion(Thing):
        label = [locstr("motion", "en")]


    class hasMotion(ObjectProperty, Motion >> Motion):
        pass


    class followedBy(ObjectProperty, Motion >> Motion):
        pass


    class motion_parameters(DataProperty, Motion >> float):
        label = [locstr("motion parameters", "en")]



    class folding_rotation_shift(motion_parameters):
        label = [locstr("folding rotation shift", "en")]


    class repetitive_folding_rotation_shift(motion_parameters):
        label = [locstr("repetitive folding rotation shift", "en")]


    class height_increment(motion_parameters):
        label = [locstr("height increment", "en")]


    class radius_lower_bound_absolute(motion_parameters):
        label = [locstr("radius lower bound absolute", "en")]


    class radius_upper_bound_absolute(motion_parameters):
        label = [locstr("radius upper bound absolute", "en")]


    class radius_lower_bound_relative(motion_parameters):
        label = [locstr("radius lower bound relative", "en")]


    class radius_upper_bound_relative(motion_parameters):
        label = [locstr("radius upper bound relative", "en")]


    class ellipse_shift(motion_parameters):
        label = [locstr("ellipse shift", "en")]


    class MixingMotion(Motion):
        label = [locstr("mixing motion", "en")]


    class CircularDivingToInnerMotion(MixingMotion):
        label = [locstr("circular diving to inner motion", "en")]
        is_a = [radius_lower_bound_relative.value(0.0) & radius_upper_bound_relative.value(0.7),
                height_increment.value(0.1)]


    class CircularMotion(MixingMotion):
        label = [locstr("circular motion", "en")]
        is_a = [radius_lower_bound_relative.value(0.7) & radius_upper_bound_relative.value(0.7)]


    class FoldingMotion(MixingMotion):
        label = [locstr("folding motion", "en")]
        is_a = [radius_lower_bound_relative.value(0.0) & radius_upper_bound_relative.value(0.7),
                folding_rotation_shift.value(90), repetitive_folding_rotation_shift.value(22.5)]


    class HorizontalEllipticalMotion(MixingMotion):
        label = [locstr("horizontal elliptical motion", "en")]
        is_a = [radius_lower_bound_relative.value(0.0) & radius_upper_bound_relative.value(0.7),
                ellipse_shift.value(0.04)]


    class WhirlstormMotion(MixingMotion):
        label = [locstr("whirlstorm motion", "en")]
        is_a = [radius_lower_bound_relative.value(0.0) & radius_upper_bound_relative.value(0.7)]


    class CompoundMotion(Motion):
        label = [locstr("compound motion", "en")]


    class WhirlstormThenCircularDivingToInner(CompoundMotion):
        label = [locstr("whirlstorm then circular to diving inner")]
        equivalent_to = [Motion & (hasMotion.some(WhirlstormMotion & followedBy.some(CircularDivingToInnerMotion)
                                                  & followedBy.exactly(1, Motion)))]


    class WhirlstormThenHorizontal(CompoundMotion):
        label = [locstr("whirlstorm then horizontal")]
        equivalent_to = [Motion & (hasMotion.some(WhirlstormMotion & followedBy.some(HorizontalEllipticalMotion) &
                                                  followedBy.exactly(1, Motion)))]
