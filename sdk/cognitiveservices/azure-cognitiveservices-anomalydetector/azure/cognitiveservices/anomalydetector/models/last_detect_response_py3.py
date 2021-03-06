# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class LastDetectResponse(Model):
    """LastDetectResponse.

    All required parameters must be populated in order to send to Azure.

    :param period: Required. Frequency extracted from the series, zero means
     no recurrent pattern has been found.
    :type period: int
    :param suggested_window: Required. Suggested input series points needed
     for detecting the latest point.
    :type suggested_window: int
    :param expected_value: Required. Expected value of the latest point.
    :type expected_value: float
    :param upper_margin: Required. Upper margin of the latest point.
     UpperMargin is used to calculate upperBoundary, which equals to
     expectedValue + (100 - marginScale)*upperMargin. If the value of latest
     point is between upperBoundary and lowerBoundary, it should be treated as
     normal value. By adjusting marginScale value, anomaly status of latest
     point can be changed.
    :type upper_margin: float
    :param lower_margin: Required. Lower margin of the latest point.
     LowerMargin is used to calculate lowerBoundary, which equals to
     expectedValue - (100 - marginScale)*lowerMargin.
    :type lower_margin: float
    :param is_anomaly: Required. Anomaly status of the latest point, true
     means the latest point is an anomaly either in negative direction or
     positive direction.
    :type is_anomaly: bool
    :param is_negative_anomaly: Required. Anomaly status in negative direction
     of the latest point. True means the latest point is an anomaly and its
     real value is smaller than the expected one.
    :type is_negative_anomaly: bool
    :param is_positive_anomaly: Required. Anomaly status in positive direction
     of the latest point. True means the latest point is an anomaly and its
     real value is larger than the expected one.
    :type is_positive_anomaly: bool
    """

    _validation = {
        'period': {'required': True},
        'suggested_window': {'required': True},
        'expected_value': {'required': True},
        'upper_margin': {'required': True},
        'lower_margin': {'required': True},
        'is_anomaly': {'required': True},
        'is_negative_anomaly': {'required': True},
        'is_positive_anomaly': {'required': True},
    }

    _attribute_map = {
        'period': {'key': 'period', 'type': 'int'},
        'suggested_window': {'key': 'suggestedWindow', 'type': 'int'},
        'expected_value': {'key': 'expectedValue', 'type': 'float'},
        'upper_margin': {'key': 'upperMargin', 'type': 'float'},
        'lower_margin': {'key': 'lowerMargin', 'type': 'float'},
        'is_anomaly': {'key': 'isAnomaly', 'type': 'bool'},
        'is_negative_anomaly': {'key': 'isNegativeAnomaly', 'type': 'bool'},
        'is_positive_anomaly': {'key': 'isPositiveAnomaly', 'type': 'bool'},
    }

    def __init__(self, *, period: int, suggested_window: int, expected_value: float, upper_margin: float, lower_margin: float, is_anomaly: bool, is_negative_anomaly: bool, is_positive_anomaly: bool, **kwargs) -> None:
        super(LastDetectResponse, self).__init__(**kwargs)
        self.period = period
        self.suggested_window = suggested_window
        self.expected_value = expected_value
        self.upper_margin = upper_margin
        self.lower_margin = lower_margin
        self.is_anomaly = is_anomaly
        self.is_negative_anomaly = is_negative_anomaly
        self.is_positive_anomaly = is_positive_anomaly
