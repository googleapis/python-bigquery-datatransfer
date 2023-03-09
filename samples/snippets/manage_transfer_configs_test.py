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

from . import manage_transfer_configs


def test_list_configs(capsys, project_id, transfer_config_name):
    manage_transfer_configs.list_configs({"project_id": project_id})
    out, _ = capsys.readouterr()
    assert "Got the following configs:" in out
    assert transfer_config_name in out


def test_update_config(capsys, transfer_config_name):
    manage_transfer_configs.update_config(
        {
            "new_display_name": "name from test_update_config",
            "transfer_config_name": transfer_config_name,
        }
    )
    out, _ = capsys.readouterr()
    assert "Updated config:" in out
    assert transfer_config_name in out
    assert "name from test_update_config" in out


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
        {"transfer_config_name": transfer_config_name}
    )
    out, _ = capsys.readouterr()
    assert "Started transfer runs:" in out
    # Run IDs should include the transfer name in their path.
    assert transfer_config_name in out
    # Check that there are runs for 5, 4, 3, and 2 days ago.
    print("TEST SCHEDULE BACKFILL", *runs, sep="\n")
    import datetime
    now = datetime.datetime.now(datetime.timezone.utc)
    start_time = now - datetime.timedelta(days=5)
    end_time = now - datetime.timedelta(days=2)

    # Some data sources, such as scheduled_query only support daily run.
    # Truncate start_time and end_time to midnight time (00:00AM UTC).
    start_time = datetime.datetime(
        start_time.year, start_time.month, start_time.day, tzinfo=datetime.timezone.utc
    )
    end_time = datetime.datetime(
        end_time.year, end_time.month, end_time.day, tzinfo=datetime.timezone.utc
    )
    from google.cloud.bigquery_datatransfer_v1 import StartManualTransferRunsRequest
    requested_time_range = StartManualTransferRunsRequest.TimeRange(
        start_time=start_time,
        end_time=end_time,
    )
    print("TEST STIME, ETIME", start_time, end_time)
    print("REQUESTED TIME RANGE", requested_time_range) 
    
    assert len(runs) == 5 # hoping to cause this to fail


def test_schedule_backfill_manual_transfer(capsys, transfer_config_name):
    runs = manage_transfer_configs.schedule_backfill_manual_transfer(
        {"transfer_config_name": transfer_config_name}
    )
    out, _ = capsys.readouterr()
    assert "Started manual transfer runs:" in out
    # Run IDs should include the transfer name in their path.
    assert transfer_config_name in out
    # Check that there are runs for 5, 4, 3, and 2 days ago.
    print("TEST SB MANUAL TRANSFER", *runs, sep="\n")
    import datetime
    now = datetime.datetime.now(datetime.timezone.utc)
    start_time = now - datetime.timedelta(days=5)
    end_time = now - datetime.timedelta(days=2)

    # Some data sources, such as scheduled_query only support daily run.
    # Truncate start_time and end_time to midnight time (00:00AM UTC).
    start_time = datetime.datetime(
        start_time.year, start_time.month, start_time.day, tzinfo=datetime.timezone.utc
    )
    end_time = datetime.datetime(
        end_time.year, end_time.month, end_time.day, tzinfo=datetime.timezone.utc
    )
    from google.cloud.bigquery_datatransfer_v1 import StartManualTransferRunsRequest
    requested_time_range = StartManualTransferRunsRequest.TimeRange(
        start_time=start_time,
        end_time=end_time,
    )
    print("TEST STIME, ETIME", start_time, end_time)
    print("REQUESTED TIME RANGE", requested_time_range) 

    assert len(runs) == 4


def test_delete_config(capsys, transfer_config_name):
    # transfer_config_name fixture in conftest.py calls the delete config
    # sample. To conserve limited BQ-DTS quota we only make basic checks.
    assert len(transfer_config_name) != 0
