# Copyright 2017 datawire. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from .tasks import task, sh

@task()
def istio(directory, ipranges=None):
    for name in os.listdir(directory):
        cmd = ["istioctl", "kube-inject", "-f", os.path.join(directory, name)]

        if ipranges is not None:
            cmd.extend(["--includeIPRanges", ",".join(ipranges)])

        munged = sh(*cmd).output
        with open(os.path.join(directory, name), 'write') as f:
            f.write(munged)
