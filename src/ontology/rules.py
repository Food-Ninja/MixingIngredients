from owlready2 import *

from ontology.ingredient import Ingredient
from ontology.task import Task
from ontology.motion import Motion

onto = get_ontology("http://www.ease-crc.org/ont/mixing")
soma_namespace = get_ontology("http://www.ease-crc.org/ont/SOMA.owl")


def create_rule(name: str, rule: str) -> Imp:
    r = Imp(name=name)
    r.set_as_rule(rule=rule, namespaces=[onto, soma_namespace])
    return r


with onto:
    class useTool(ObjectProperty):
        pass


    class useContainer(ObjectProperty):
        pass


    class performMotion(ObjectProperty, Task >> Motion):
        pass


    class hasIngredient(ObjectProperty, Task >> Ingredient):
        pass


    """
    MIXING RULES
    """
    r1 = create_rule(name="MixingPowderLiquid",
                     rule="MixingTask(?x) ^ DryPowderIngredient(?ing1) ^ hasIngredient(?x, ?ing1) "
                          "^ LiquidIngredient(?ing2) ^ hasIngredient(?x, ?ing2) ^ Motion(?motion)"
                          "^ performMotion(?x, ?motion) -> WhirlstormMotion(?motion)")

    r2 = create_rule(name="MixingPowderWet",
                    rule="MixingTask(?x) ^ DryPowderIngredient(?ing1) ^ hasIngredient(?x, ?ing1)"
                         "^ WetIngredient(?ing2) ^ hasIngredient(?x, ?ing2) ^ Motion(?motion)"
                         "^ performMotion(?x, ?motion) -> WhirlstormMotion(?motion)")

    r3 = create_rule(name="MixingWet",
                     rule="MixingTask(?x) ^  WetIngredient(?ing) ^ hasIngredient(?x, ?ing1)"
                          "^ Motion(?motion) ^ performMotion(?x, ?motion) -> WhirlstormThenVertical(?motion)")

    r4 = create_rule(name="MixingPowder",
                     rule="MixingTask(?x) ^ DryPowderIngredient(?ing1) ^ hasIngredient(?x, ?ing1)"
                          "^ Motion(?motion) ^ performMotion(?x, ?motion) -> WhirlstormMotion(?motion)")

    r5 = create_rule(name="MixingLiquid",
                     rule="MixingTask(?x) ^ DryPowderIngredient(?ing1) ^ hasIngredient(?x, ?ing1)"
                          "^ WetIngredient(?ing2) ^ hasIngredient(?x, ?ing2)"
                          "^ Motion(?motion) ^ performMotion(?x, ?motion) -> WhirlstormMotion(?motion)")

    r6 = create_rule(name="MixingLiquidWet",
                     rule="MixingTask(?x) ^ LiquidIngredient(?ing1) ^ hasIngredient(?x, ?ing1)"
                          "^ WetIngredient(?ing2) ^ hasIngredient(?x, ?ing2)"
                          "^ Motion(?motion) ^ performMotion(?x, ?motion)-> WhirlstormMotion(?motion)")

    """
    STIRRING RULES
    """

    r7 = create_rule(name="StirPowderWet",
                     rule="StirringTask(?x) ^ DryPowderIngredient(?ing1) ^ hasIngredient(?x, ?ing1) "
                          "^ WetIngredient(?ing2) ^ hasIngredient(?x, ?ing2)"
                          "^ Motion(?motion) ^ performMotion(?x, ?motion) -> WhirlstormThenVertical(?motion)")

    r8 = create_rule(name="StirWet",
                     rule="StirringTask(?x) ^ WetIngredient(?ing) ^ hasIngredient(?x, ?ing1) "
                          "^ Motion(?motion) ^ performMotion(?x, ?motion) -> "
                          "WhirlstormThenCircularDivingToInner(?motion)")

    r9 = create_rule(name="StirLiquid",
                     rule="StirringTask(?x) ^ LiquidIngredient(?ing) ^ hasIngredient(?x, ?ing1) "
                          "^ Motion(?motion) ^ performMotion(?x, ?motion) -> CircularMotion(?motion)")

    r10 = create_rule(name="StirLiquidPowder",
                      rule="StirringTask(?x) ^LiquidIngredient(?ing1) "
                           "^ DryPowderIngredient(?ing2) ^ hasIngredient(?x, ?ing1)"
                           "^ Motion(?motion) ^ performMotion(?x, ?motion) -> WhirlstormMotion(?motion)")

    r11 = create_rule(name="StirLiquidWet",
                      rule="StirringTask(?x) ^LiquidIngredient(?ing1) ^ hasIngredient(?x, ?ing1)"
                           "^ WetIngredient(?ing2) ^ hasIngredient(?x, ?ing2) "
                           "^ Motion(?motion) ^ performMotion(?x, ?motion) -> WhirlstormMotion(?motion)")

    """
    BEATING RULES
    """

    r12 = create_rule(name="BeatingWet",
                      rule="BeatingTask(?x) ^ WetIngredient(?ing) ^ hasIngredient(?x, ?ing1)"
                           "^Motion(?motion) ^ performMotion(?x, ?motion) -> VerticalCircularMotion(?motion)")

    r13 = create_rule(name="BeatingPowderWet",
                      rule="BeatingTask(?x) ^ DryPowderIngredient(?ing1) ^ hasIngredient(?x, ?ing1)"
                           "^ WetIngredient(?ing2) ^ hasIngredient(?x, ?ing2)"
                           " ^Motion(?motion) ^ performMotion(?x, ?motion) -> WhirlstormMotion(?motion)")

    r14 = create_rule(name="BeatingLiquidPowderWet",
                      rule="BeatingTask(?x) ^ LiquidIngredient(?ing1) ^ hasIngredient(?x, ?ing1)"
                           "^ DryPowderIngredient(?ing2) ^ hasIngredient(?x, ?ing2)"
                           "^ WetIngredient(?ing3) ^ hasIngredient(?x, ?ing1) "
                           "^ Motion(?motion) ^ performMotion(?x, ?motion) -> "
                           "WhirlstormMotion(?motion)")

    """
    WHISK RULES
    """

    r15 = create_rule(name="WhiskWet",
                      rule="WhiskingTask(?x) ^ WetIngredient(?ing) ^ hasIngredient(?x, ?ing1)"
                           "^ Motion(?motion) ^ performMotion(?x, ?motion) -> VerticalCircularMotion(?motion)")

    r16 = create_rule(name="WhiskPowderWet",
                      rule="WhiskingTask(?x) ^ DryPowderIngredient(?ing1) ^ hasIngredient(?x, ?ing1)"
                           "^ WetIngredient(?ing2) ^ hasIngredient(?x, ?ing2) "
                           "^Motion(?motion) ^ performMotion(?x, ?motion) -> WhirlstormMotion(?motion)")

    r17 = create_rule(name="WhiskPowder",
                      rule="WhiskingTask(?x) ^ DryPowderIngredient(?ing) ^ hasIngredient(?x, ?ing1)"
                           "^ Motion(?motion) ^ performMotion(?x, ?motion) -> WhirlstormMotion(?motion)")
