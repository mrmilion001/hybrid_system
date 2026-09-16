from advisory.models import Rule


def evaluate_rules(intent, parameters, sub_intent=None):
    """
    Evaluate active rules for the identified regulatory domain.

    Returns the rules whose conditions are satisfied.
    """

    rules = Rule.objects.filter(
        domain=intent,
        active=True
    )

    matched_rules = []

    for rule in rules:
        conditions = rule.conditions
        conditions_met = True

        for key, expected_value in conditions.items():

            # The domain is already used to select the rules.
            if key == "domain":
                continue

            # Minimum condition, e.g. cgpa_min
            if key.endswith("_min"):
                parameter_name = key[:-4]
                actual_value = parameters.get(parameter_name)

                if actual_value is None or actual_value < expected_value:
                    conditions_met = False
                    break

            # Maximum condition, e.g. cgpa_max
            elif key.endswith("_max"):
                parameter_name = key[:-4]
                actual_value = parameters.get(parameter_name)

                if actual_value is None or actual_value > expected_value:
                    conditions_met = False
                    break

            # Exact-match or complex condition
            else:
                if key == "intent":
                    actual_value = sub_intent
                else:
                    actual_value = parameters.get(key)

                # List membership, e.g. ['OMR', 'CBT']
                if isinstance(expected_value, list):
                    if actual_value not in expected_value:
                        conditions_met = False
                        break

                # Dictionary operator, e.g. {'not_in': ['OMR', 'CBT']}
                elif isinstance(expected_value, dict):
                    if "not_in" in expected_value:
                        if actual_value in expected_value["not_in"]:
                            conditions_met = False
                            break

                # Standard scalar equality
                else:
                    if actual_value != expected_value:
                        conditions_met = False
                        break

        if conditions_met:
            matched_rules.append({
                "rule_id": rule.rule_id,
                "name": rule.name,
                "actions": rule.actions,
                "stop_processing": rule.stop_processing,
                "requires_human_review": rule.requires_human_review,
            })

    return matched_rules