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

import google.api_core.exceptions
import pytest

from . import manage_transfer_configs


@pytest.fixture(scope="module")
def transfer_config_name(transfer_client, project_id, dataset_id):
    from . import scheduled_query

    transfer_config = scheduled_query.create_scheduled_query(
        {
            "project_id": project_id,
            "dataset_id": dataset_id,
        }
    )
    yield transfer_config.name
    transfer_client.delete_transfer_config(name=transfer_config.name)


@pytest.fixture
def temp_transfer_config_name(transfer_client, project_id, dataset_id):
    from . import scheduled_query

    transfer_config = scheduled_query.create_scheduled_query(
        {
            "project_id": project_id,
            "dataset_id": dataset_id,
        }
    )
    yield transfer_config.name
    try:
        transfer_client.delete_transfer_config(name=transfer_config.name)
    except google.api_core.exceptions.NotFound:
        pass


def test_list_configs(capsys, project_id, transfer_config_name):
    manage_transfer_configs.list_configs({"project_id": project_id})
    out, _ = capsys.readouterr()
    assert "Got the following configs:" in out
    assert transfer_config_name in out


def test_update_credentials_with_service_account(
    capsys, project_id, service_account_name, transfer_config_name
):
    manage_transfer_configs.update_credentials_with_service_account(
        {
            "project_id": project_id,
            "service_account_name": service_account_name,
            "transfer_config_name": transfer_config_name,
        }
    )
    out, _ = capsys.readouterr()
    assert "Updated config:" in out
    assert transfer_config_name in out


def test_schedule_backfill(capsys, transfer_config_name):
    runs = manage_transfer_configs.schedule_backfill(
        {
            "transfer_config_name": transfer_config_name,
        }
    )
    out, _ = capsys.readouterr()
    assert "Started transfer runs:" in out
    # Run IDs should include the transfer name in their path.
    assert transfer_config_name in out
    # Check that there are runs for 5, 4, 3, and 2 days ago.
    assert len(runs) == 4


def test_delete_config(capsys, temp_transfer_config_name):
    manage_transfer_configs.delete_config(
        {
            "transfer_config_name": temp_transfer_config_name,
        }
    )
    out, _ = capsys.readouterr()
    assert "Deleted" in out
    assert temp_transfer_config_name in out
