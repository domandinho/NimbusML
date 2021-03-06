# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
RandomPartitionSelector
"""

__all__ = ["RandomPartitionSelector"]


from ...internal.core.ensemble.subset_selector.randompartitionselector import \
    RandomPartitionSelector as core
from ...internal.utils.utils import trace


class RandomPartitionSelector(core):
    """
    **Description**
        Randomly partitions the rows for each trainer in the ensemble

    :param feature_selector: The Feature selector.

    :param params: Additional arguments sent to compute engine.

    """

    @trace
    def __init__(
            self,
            feature_selector=None,
            **params):
        core.__init__(
            self,
            feature_selector=feature_selector,
            **params)

    def get_params(self, deep=False):
        """
        Get the parameters for this operator.
        """
        return core.get_params(self)
