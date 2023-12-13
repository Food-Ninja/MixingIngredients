from owlready2 import *

onto = get_ontology("http://www.ease-crc.org/ont/mixing")
onto.imported_ontologies.append(get_ontology("http://www.ease-crc.org/ont/SOMA.owl"))
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


    class performMotion(ObjectProperty):
        pass


    """
    MIXING RULES
    """
    r1 = create_rule(name="MixingPowderLiquid",
                     rule="MixingTask(?x) ^ DryPowderIngredient(?ing1) ^ LiquidIngredient(?ing2)"
                          "^Motion(?motion) -> WhirlstormMotion(?motion) ^ performMotion(?x, ?motion)")

    r2 = create_rule(name="MixingPowderWet",
                     rule="MixingTask(?x) ^ DryPowderIngredient(?ing1) ^ WetIngredient(?ing2)"
                          "^Motion(?motion) -> WhirlstormMotion(?motion) ^ performMotion(?x, ?motion)")

    r3 = create_rule(name="MixingWet",
                     rule="MixingTask(?x) ^  WetIngredient(?ing)"
                          "^Motion(?motion) -> WhirlstormMotion(?motion) ^ VerticalCircularMotion(?motion)"
                          " ^ performMotion(?x, ?motion)")

    r4 = create_rule(name="MixingPowder",
                     rule="MixingTask(?x) ^ DryPowderIngredient(?ing1)"
                          "^Motion(?motion) -> WhirlstormMotion(?motion) ^ performMotion(?x, ?motion)")

    r5 = create_rule(name="MixingLiquid",
                     rule="MixingTask(?x) ^ DryPowderIngredient(?ing1) ^ WetIngredient(?ing2)"
                          "^Motion(?motion) -> WhirlstormMotion(?motion) ^ performMotion(?x, ?motion)")

    r6 = create_rule(name="MixingLiquidWet",
                     rule="MixingTask(?x) ^ LiquidIngredient(?ing1) ^ WetIngredient(?ing2)"
                          "^Motion(?motion) -> WhirlstormMotion(?motion) ^ performMotion(?x, ?motion)")

    """
    STIRRING RULES
    """

    r7 = create_rule(name="StirPowderWet",
                     rule="StirringTask(?x) ^ DryPowderIngredient(?ing1) ^ WetIngredient(?ing2)"
                          "^Motion(?motion) -> WhirlstormMotion(?motion) ^ VerticalCircularMotion(?motion)"
                          " ^ performMotion(?x, ?motion)")

    r8 = create_rule(name="StirWet",
                     rule="StirringTask(?x) ^ WetIngredient(?ing)"
                          "^Motion(?motion) -> WhirlstormMotion(?motion) ^ CircularDivingToInner(?motion) "
                          "^ performMotion(?x, ?motion)")

    r9 = create_rule(name="StirLiquid",
                     rule="StirringTask(?x) ^ LiquidIngredient(?ing)"
                          "^Motion(?motion) -> CircularMotion(?motion) ^ performMotion(?x, ?motion)")

    r10 = create_rule(name="StirLiquidPowder",
                      rule="StirringTask(?x) ^LiquidIngredient(?ing1) ^ DryPowderIngredient(?ing2)"
                           "^Motion(?motion) -> WhirlstormMotion(?motion) ^ performMotion(?x, ?motion)")

    r11 = create_rule(name="StirLiquidWet",
                      rule="StirringTask(?x) ^LiquidIngredient(?ing1) ^ WetIngredient(?ing2)"
                           "^Motion(?motion) -> WhirlstormMotion(?motion) ^ performMotion(?x, ?motion)")

    """
    BEATING RULES
    """

    r12 = create_rule(name="BeatingWet",
                      rule="BeatingTask(?x) ^ WetIngredient(?ing)"
                           "^Motion(?motion) -> VerticalCircularMotion(?motion) ^ performMotion(?x, ?motion)")

    r13 = create_rule(name="BeatingPowderWet",
                      rule="BeatingTask(?x) ^ DryPowderIngredient(?ing1) ^ WetIngredient(?ing2)"
                           "^Motion(?motion) -> WhirlstormMotion(?motion) ^ performMotion(?x, ?motion)")

    r14 = create_rule(name="BeatingLiquidPowderWet",
                      rule="BeatingTask(?x) ^ LiquidIngredient(?ing1) ^ DryPowderIngredient(?ing2) "
                           "^ WetIngredient(?ing3) ^Motion(?motion) -> "
                           "WhirlstormMotion(?motion) ^ performMotion(?x, ?motion)")

    """
    WHISK RULES
    """

    r15 = create_rule(name="WhiskWet",
                      rule="WhiskTask(?x) ^ WetIngredient(?ing) ^Motion(?motion) -> "
                           "VerticalCircularMotion(?motion) ^ performMotion(?x, ?motion)")

    r16 = create_rule(name="WhiskPowderWet",
                      rule="WhiskTask(?x) ^ DryPowderIngredient(?ing1) ^ WetIngredient(?ing2) ^Motion(?motion) -> "
                           "WhirlstormMotion(?motion) ^ performMotion(?x, ?motion)")

    r17 = create_rule(name="WhiskPowder",
                      rule="WhiskTask(?x) ^ DryPowderIngredient(?ing) ^Motion(?motion) -> "
                           "WhirlstormMotion(?motion) ^ performMotion(?x, ?motion)")
