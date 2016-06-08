# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Hewlett Packard Enterprise Development LP
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""
Sample test case for bash config
"""

import logging
from ipdb import set_trace

log = logging.getLogger(__name__)

TOPOLOGY = """
#
# +-------+                    +-------+
# |       |                    |       |
# |  ops1 <-------------------->  ops2 |
# |       |                    |       |
# +-------+                    +-------+
#
# Nodes
[type=openswitch name="OpenSwitch 1"] ops1
[type=openswitch name="OpenSwitch 2"] ops2
# Links
ops1:port1 -- ops2:port1
ops1:port2
"""


def test_bash_config(topology, step):

    ops1 = topology.get('ops1')
    ops2 = topology.get('ops2')
    assert ops1 is not None
    assert ops2 is not None
    step('Trying to fetch the ifconfig using bash prompt')
    result = ops1('ifconfig', shell='bash')
    log.debug("IFCONFIG on Switch 1 {}".format(result))
    result = ops2('ifconfig eth0', shell='bash')
    print("IFCONFIG on Switch 2 {}".format(result))
    result = ops2('sh version', shell='vtysh')
    set_trace()
    log.debug("RUNNING CONFIG on Switch 2 {}".format(result))
