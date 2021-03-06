# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
Transforms.PermutationFeatureImportance
"""

import numbers

from ..utils.entrypoints import EntryPoint
from ..utils.utils import try_set, unlist


def transforms_permutationfeatureimportance(
        data,
        predictor_model,
        metrics=None,
        use_feature_weight_filter=False,
        number_of_examples_to_use=None,
        permutation_count=1,
        **params):
    """
    **Description**
        Permutation Feature Importance (PFI)

    :param data: Input dataset (inputs).
    :param predictor_model: The path to the model file (inputs).
    :param use_feature_weight_filter: Use feature weights to pre-
        filter features (inputs).
    :param number_of_examples_to_use: Limit the number of examples to
        evaluate on (inputs).
    :param permutation_count: The number of permutations to perform
        (inputs).
    :param metrics: The PFI metrics (outputs).
    """

    entrypoint_name = 'Transforms.PermutationFeatureImportance'
    inputs = {}
    outputs = {}

    if data is not None:
        inputs['Data'] = try_set(
            obj=data,
            none_acceptable=False,
            is_of_type=str)
    if predictor_model is not None:
        inputs['PredictorModel'] = try_set(
            obj=predictor_model,
            none_acceptable=False,
            is_of_type=str)
    if use_feature_weight_filter is not None:
        inputs['UseFeatureWeightFilter'] = try_set(
            obj=use_feature_weight_filter,
            none_acceptable=True,
            is_of_type=bool)
    if number_of_examples_to_use is not None:
        inputs['NumberOfExamplesToUse'] = try_set(
            obj=number_of_examples_to_use,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if permutation_count is not None:
        inputs['PermutationCount'] = try_set(
            obj=permutation_count,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if metrics is not None:
        outputs['Metrics'] = try_set(
            obj=metrics,
            none_acceptable=False,
            is_of_type=str)

    input_variables = {
        x for x in unlist(inputs.values())
        if isinstance(x, str) and x.startswith("$")}
    output_variables = {
        x for x in unlist(outputs.values())
        if isinstance(x, str) and x.startswith("$")}

    entrypoint = EntryPoint(
        name=entrypoint_name, inputs=inputs, outputs=outputs,
        input_variables=input_variables,
        output_variables=output_variables)
    return entrypoint
