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
                     rule="MixingTask(?x) ^ PowderIngredient(?ing1) ^ hasIngredient(?x, ?ing1) "
                          "^ LiquidIngredient(?ing2) ^ hasIngredient(?x, ?ing2) ^ Motion(?motion)"
                          "^ performMotion(?x, ?motion) -> WhirlstormMotion(?motion)")

    r2 = create_rule(name="MixingPowderSemiLiquid",
                     rule="MixingTask(?x) ^ PowderIngredient(?ing1) ^ hasIngredient(?x, ?ing1)"
                          "^ SemiLiquidIngredient(?ing2) ^ hasIngredient(?x, ?ing2) ^ Motion(?motion)"
                          "^ performMotion(?x, ?motion) -> WhirlstormMotion(?motion)")

    r3 = create_rule(name="MixingSemiLiquid",
                     rule="MixingTask(?x) ^  SemiLiquidIngredient(?ing1) ^ hasIngredient(?x, ?ing1)"
                          "^ Motion(?motion) ^ performMotion(?x, ?motion) -> WhirlstormThenHorizontal(?motion)")

    r4 = create_rule(name="MixingPowder",
                     rule="MixingTask(?x) ^ PowderIngredient(?ing1) ^ hasIngredient(?x, ?ing1)"
                          "^ Motion(?motion) ^ performMotion(?x, ?motion) -> WhirlstormMotion(?motion)")

    r5 = create_rule(name="MixingLiquid",
                     rule="MixingTask(?x) ^ LiquidIngredient(?ing1) ^ hasIngredient(?x, ?ing1)"
                          "^ Motion(?motion) ^ performMotion(?x, ?motion) -> WhirlstormMotion(?motion)")

    r6 = create_rule(name="MixingLiquidSemiLiquid",
                     rule="MixingTask(?x) ^ LiquidIngredient(?ing1) ^ hasIngredient(?x, ?ing1)"
                          "^ SemiLiquidIngredient(?ing2) ^ hasIngredient(?x, ?ing2)"
                          "^ Motion(?motion) ^ performMotion(?x, ?motion)-> WhirlstormMotion(?motion)")

    """
    STIRRING RULES
    """
    r18 = create_rule(name="StirPowder",
                      rule="StirringTask(?x) ^ PowderIngredient(?ing1) ^ hasIngredient(?x, ?ing1) "
                           "^ Motion(?motion) ^ performMotion(?x, ?motion) -> WhirlstormMotion(?motion)")
    r7 = create_rule(name="StirPowderSemiLiquid",
                     rule="StirringTask(?x) ^ PowderIngredient(?ing1) ^ hasIngredient(?x, ?ing1) "
                          "^ SemiLiquidIngredient(?ing2) ^ hasIngredient(?x, ?ing2)"
                          "^ Motion(?motion) ^ performMotion(?x, ?motion) -> WhirlstormThenHorizontal(?motion)")

    r8 = create_rule(name="StirSemiLiquid",
                     rule="StirringTask(?x) ^ SemiLiquidIngredient(?ing1) ^ hasIngredient(?x, ?ing1) "
                          "^ Motion(?motion) ^ performMotion(?x, ?motion) -> "
                          "WhirlstormThenHorizontal(?motion)")

    r9 = create_rule(name="StirLiquid",
                     rule="StirringTask(?x) ^ LiquidIngredient(?ing1) ^ hasIngredient(?x, ?ing1) "
                          "^ Motion(?motion) ^ performMotion(?x, ?motion) -> CircularMotion(?motion)")

    r10 = create_rule(name="StirLiquidPowder",
                      rule="StirringTask(?x) ^LiquidIngredient(?ing1)  ^hasIngredient(?x, ?ing1)"
                           "^ PowderIngredient(?ing2) ^ hasIngredient(?x, ?ing1)"
                           "^ Motion(?motion) ^ performMotion(?x, ?motion) -> WhirlstormMotion(?motion)")

    r11 = create_rule(name="StirLiquidSemiLiquid",
                      rule="StirringTask(?x) ^LiquidIngredient(?ing1) ^ hasIngredient(?x, ?ing1)"
                           "^ SemiLiquidIngredient(?ing2) ^ hasIngredient(?x, ?ing2) "
                           "^ Motion(?motion) ^ performMotion(?x, ?motion) -> WhirlstormMotion(?motion)")

    """
    BEATING RULES
    """
    r19 = create_rule(name="BeatingLiquid",
                      rule="BeatingTask(?x) ^ LiquidIngredient(?ing1) ^ hasIngredient(?x, ?ing1)"
                           "^Motion(?motion) ^ performMotion(?x, ?motion) -> WhirlstormMotion(?motion)")
    r20 = create_rule(name="BeatingPowder",
                      rule="BeatingTask(?x) ^ PowderIngredient(?ing1) ^ hasIngredient(?x, ?ing1)"
                           "^Motion(?motion) ^ performMotion(?x, ?motion) -> WhirlstormThenHorizontal(?motion)")
    r12 = create_rule(name="BeatingSemiLiquid",
                      rule="BeatingTask(?x) ^ SemiLiquidIngredient(?ing1) ^ hasIngredient(?x, ?ing1)"
                           "^Motion(?motion) ^ performMotion(?x, ?motion) -> HorizontalEllipticalMotion(?motion)")

    r13 = create_rule(name="BeatingPowderSemiLiquid",
                      rule="BeatingTask(?x) ^ PowderIngredient(?ing1) ^ hasIngredient(?x, ?ing1)"
                           "^ SemiLiquidIngredient(?ing2) ^ hasIngredient(?x, ?ing2)"
                           " ^Motion(?motion) ^ performMotion(?x, ?motion) -> HorizontalEllipticalMotion(?motion)")

    r14 = create_rule(name="BeatingLiquidPowder",
                      rule="BeatingTask(?x) ^ LiquidIngredient(?ing1) ^ hasIngredient(?x, ?ing1)"
                           "^ PowderIngredient(?ing2) ^ hasIngredient(?x, ?ing2)"
                           "^ Motion(?motion) ^ performMotion(?x, ?motion) -> "
                           "WhirlstormMotion(?motion)")

    r21 = create_rule(name="BeatingLiquidSemiLiquid",
                      rule="BeatingTask(?x) ^ LiquidIngredient(?ing1) ^ hasIngredient(?x, ?ing1)"
                           "^ SemiLiquidIngredient(?ing2) ^ hasIngredient(?x, ?ing2)"
                           "^ Motion(?motion) ^ performMotion(?x, ?motion) -> "
                           "WhirlstormThenHorizontal(?motion)")

    """
    WHISK RULES
    """

    r15 = create_rule(name="WhiskSemiLiquid",
                      rule="WhiskingTask(?x) ^ SemiLiquidIngredient(?ing1) ^ hasIngredient(?x, ?ing1)"
                           "^ Motion(?motion) ^ performMotion(?x, ?motion) -> HorizontalEllipticalMotion(?motion)")

    r16 = create_rule(name="WhiskPowderSemiLiquid",
                      rule="WhiskingTask(?x) ^ PowderIngredient(?ing1) ^ hasIngredient(?x, ?ing1)"
                           "^ SemiLiquidIngredient(?ing2) ^ hasIngredient(?x, ?ing2) "
                           "^Motion(?motion) ^ performMotion(?x, ?motion) -> WhirlstormMotion(?motion)")

    r17 = create_rule(name="WhiskPowder",
                      rule="WhiskingTask(?x) ^ PowderIngredient(?ing1) ^ hasIngredient(?x, ?ing1)"
                           "^ Motion(?motion) ^ performMotion(?x, ?motion) -> WhirlstormMotion(?motion)")
    r22 = create_rule(name="WhiskLiquid",
                      rule="WhiskingTask(?x) ^ LiquidIngredient(?ing1) ^ hasIngredient(?x, ?ing1)"
                           "^ Motion(?motion) ^ performMotion(?x, ?motion) -> WhirlstormMotion(?motion)")

    r23 = create_rule(name="WhiskDryLiquid",
                      rule="WhiskingTask(?x) ^ LiquidIngredient(?ing1) ^ hasIngredient(?x, ?ing1)"
                           "^ PowderIngredient(?ing2) ^ hasIngredient(?x, ?ing2)"
                           "^ Motion(?motion) ^ performMotion(?x, ?motion) -> WhirlstormMotion(?motion)")

    r24 = create_rule(name="WhiskLiquidSemiLiquid",
                      rule="WhiskingTask(?x) ^ LiquidIngredient(?ing1) ^ hasIngredient(?x, ?ing1)"
                           "^ SemiLiquidIngredient(?ing2) ^ hasIngredient(?x, ?ing2)"
                           "^ Motion(?motion) ^ performMotion(?x, ?motion) -> WhirlstormMotion(?motion)")


    """
    FOLDING TASK
    """
    r25 = create_rule(name="Folding",
                      rule="FoldingTask(?x) ^ Ingredient(?ing1) ^ hasIngredient(?x, ?ing1)"
                           "^ Motion(?motion) ^ performMotion(?x, ?motion) -> FoldingMotion(?motion)")
