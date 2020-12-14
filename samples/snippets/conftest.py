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

import datetime
import uuid

import google.api_core.exceptions
import google.auth
from google.cloud import bigquery
from google.cloud import bigquery_datatransfer
import pytest


def temp_suffix():
    now = datetime.datetime.now()
    return f"{now.strftime('%Y%m%d%H%M%S')}_{uuid.uuid4().hex[:8]}"


@pytest.fixture(scope="session")
def default_credentials():
    return google.auth.default(["https://www.googleapis.com/auth/cloud-platform"])


@pytest.fixture(scope="session")
def service_account_name(default_credentials):
    credentials, _ = default_credentials
    # Note: this property is not available when running with user account
    # credentials, but only service account credentials are used in our test
    # infrastructure.
    return credentials.service_account_email


@pytest.fixture(scope="session")
def project_id(default_credentials):
    return os.environ["GOOGLE_CLOUD_PROJECT"]


@pytest.fixture(scope="session")
def bigquery_client(default_credentials):
    credentials, project_id = default_credentials
    return bigquery.Client(credentials=credentials, project=project_id)


@pytest.fixture(scope="session")
def transfer_client(default_credentials):
    credentials, _ = default_credentials
    return bigquery_datatransfer.DataTransferServiceClient(credentials=credentials)


@pytest.fixture
def to_delete_configs(transfer_client):
    to_delete = []
    yield to_delete
    for config_name in to_delete:
        try:
            transfer_client.delete_transfer_config(name=config_name)
        except google.api_core.exceptions.GoogleAPICallError:
            pass


@pytest.fixture(scope="module")
def dataset_id(bigquery_client, project_id):
    dataset_id = f"bqdts_{temp_suffix()}"
    bigquery_client.create_dataset(f"{project_id}.{dataset_id}")
    yield dataset_id
    bigquery_client.delete_dataset(dataset_id, delete_contents=True)
