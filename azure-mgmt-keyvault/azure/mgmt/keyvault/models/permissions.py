# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Permissions(Model):
    """Permissions the identity has for keys and secrets.

    :param keys: Permissions to keys
    :type keys: list of str
    :param secrets: Permissions to secrets
    :type secrets: list of str
    """ 

    _attribute_map = {
        'keys': {'key': 'keys', 'type': '[str]'},
        'secrets': {'key': 'secrets', 'type': '[str]'},
    }

    def __init__(self, keys=None, secrets=None):
        self.keys = keys
        self.secrets = secrets
