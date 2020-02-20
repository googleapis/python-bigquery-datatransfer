# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import time

from google.cloud import bigquery_datatransfer_v1
from google.cloud.bigquery_datatransfer_v1.proto import datatransfer_pb2


class TestSystemDataTransferService(object):
    def test_list_data_sources(self):
        project_id = os.environ["PROJECT_ID"]

        client = bigquery_datatransfer_v1.DataTransferServiceClient()
        parent = client.project_path(project_id)
        response = client.list_data_sources(parent)
