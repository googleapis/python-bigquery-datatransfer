# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
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
#
# Generated code. DO NOT EDIT!
#
# Snippet for UpdateTransferConfig
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-bigquery-datatransfer


# [START bigquerydatatransfer_generated_bigquery_datatransfer_v1_DataTransferService_UpdateTransferConfig_async]
from google.cloud import bigquery_datatransfer_v1


async def sample_update_transfer_config():
    # Create a client
    client = bigquery_datatransfer_v1.DataTransferServiceAsyncClient()

    # Initialize request argument(s)
    transfer_config = bigquery_datatransfer_v1.TransferConfig()
    transfer_config.destination_dataset_id = "destination_dataset_id_value"

    request = bigquery_datatransfer_v1.UpdateTransferConfigRequest(
        transfer_config=transfer_config,
    )

    # Make the request
    response = await client.update_transfer_config(request=request)

    # Handle the response
    print(response)

# [END bigquerydatatransfer_generated_bigquery_datatransfer_v1_DataTransferService_UpdateTransferConfig_async]
