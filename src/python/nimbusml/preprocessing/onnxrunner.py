# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
OnnxRunner
"""

__all__ = ["OnnxRunner"]


from sklearn.base import TransformerMixin

from ..base_transform import BaseTransform
from ..internal.core.preprocessing.onnxrunner import OnnxRunner as core
from ..internal.utils.utils import trace


class OnnxRunner(core, BaseTransform, TransformerMixin):
    """
    **Description**
        Applies an ONNX model to a dataset.

    :param columns: see `Columns </nimbusml/concepts/columns>`_.

    :param model_file: Path to the onnx model file.

    :param input_columns: Name of the input column.

    :param output_columns: Name of the output column.

    :param gpu_device_id: GPU device id to run on (e.g. 0,1,..). Null for CPU.
        Requires CUDA 9.1.

    :param fallback_to_cpu: If true, resumes execution on CPU upon GPU error.
        If false, will raise the GPU execption.

    :param params: Additional arguments sent to compute engine.

    """

    @trace
    def __init__(
            self,
            model_file,
            input_columns=None,
            output_columns=None,
            gpu_device_id=None,
            fallback_to_cpu=False,
            columns=None,
            **params):

        if columns:
            params['columns'] = columns
        if columns:
            input_columns = sum(
                list(
                    columns.values()),
                []) if isinstance(
                list(
                    columns.values())[0],
                list) else list(
                    columns.values())
        if columns:
            output_columns = list(columns.keys())
        BaseTransform.__init__(self, **params)
        core.__init__(
            self,
            model_file=model_file,
            input_columns=input_columns,
            output_columns=output_columns,
            gpu_device_id=gpu_device_id,
            fallback_to_cpu=fallback_to_cpu,
            **params)
        self._columns = columns

    def get_params(self, deep=False):
        """
        Get the parameters for this operator.
        """
        return core.get_params(self)
