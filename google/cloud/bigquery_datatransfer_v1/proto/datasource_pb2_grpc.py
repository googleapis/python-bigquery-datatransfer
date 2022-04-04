# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.cloud.bigquery.datatransfer_v1.proto import (
    datasource_pb2 as google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datasource__pb2,
)
from google.cloud.bigquery.datatransfer_v1.proto import (
    transfer_pb2 as google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_transfer__pb2,
)
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class DataSourceServiceStub(object):
    """The Google BigQuery Data Transfer API allows BigQuery users to
    configure transfer of their data from other Google Products into BigQuery.
    This service exposes methods that should be used by data source backend.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
          channel: A grpc.Channel.
        """
        self.UpdateTransferRun = channel.unary_unary(
            "/google.cloud.bigquery.datatransfer.v1.DataSourceService/UpdateTransferRun",
            request_serializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datasource__pb2.UpdateTransferRunRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_transfer__pb2.TransferRun.FromString,
        )
        self.LogTransferRunMessages = channel.unary_unary(
            "/google.cloud.bigquery.datatransfer.v1.DataSourceService/LogTransferRunMessages",
            request_serializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datasource__pb2.LogTransferRunMessagesRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
        self.StartBigQueryJobs = channel.unary_unary(
            "/google.cloud.bigquery.datatransfer.v1.DataSourceService/StartBigQueryJobs",
            request_serializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datasource__pb2.StartBigQueryJobsRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
        self.FinishRun = channel.unary_unary(
            "/google.cloud.bigquery.datatransfer.v1.DataSourceService/FinishRun",
            request_serializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datasource__pb2.FinishRunRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
        self.CreateDataSourceDefinition = channel.unary_unary(
            "/google.cloud.bigquery.datatransfer.v1.DataSourceService/CreateDataSourceDefinition",
            request_serializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datasource__pb2.CreateDataSourceDefinitionRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datasource__pb2.DataSourceDefinition.FromString,
        )
        self.UpdateDataSourceDefinition = channel.unary_unary(
            "/google.cloud.bigquery.datatransfer.v1.DataSourceService/UpdateDataSourceDefinition",
            request_serializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datasource__pb2.UpdateDataSourceDefinitionRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datasource__pb2.DataSourceDefinition.FromString,
        )
        self.DeleteDataSourceDefinition = channel.unary_unary(
            "/google.cloud.bigquery.datatransfer.v1.DataSourceService/DeleteDataSourceDefinition",
            request_serializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datasource__pb2.DeleteDataSourceDefinitionRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
        self.GetDataSourceDefinition = channel.unary_unary(
            "/google.cloud.bigquery.datatransfer.v1.DataSourceService/GetDataSourceDefinition",
            request_serializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datasource__pb2.GetDataSourceDefinitionRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datasource__pb2.DataSourceDefinition.FromString,
        )
        self.ListDataSourceDefinitions = channel.unary_unary(
            "/google.cloud.bigquery.datatransfer.v1.DataSourceService/ListDataSourceDefinitions",
            request_serializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datasource__pb2.ListDataSourceDefinitionsRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datasource__pb2.ListDataSourceDefinitionsResponse.FromString,
        )


class DataSourceServiceServicer(object):
    """The Google BigQuery Data Transfer API allows BigQuery users to
    configure transfer of their data from other Google Products into BigQuery.
    This service exposes methods that should be used by data source backend.
    """

    def UpdateTransferRun(self, request, context):
        """Update a transfer run. If successful, resets
        data_source.update_deadline_seconds timer.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def LogTransferRunMessages(self, request, context):
        """Log messages for a transfer run. If successful (at least 1 message), resets
        data_source.update_deadline_seconds timer.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def StartBigQueryJobs(self, request, context):
        """Notify the Data Transfer Service that data is ready for loading.
        The Data Transfer Service will start and monitor multiple BigQuery Load
        jobs for a transfer run. Monitored jobs will be automatically retried
        and produce log messages when starting and finishing a job.
        Can be called multiple times for the same transfer run.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def FinishRun(self, request, context):
        """Notify the Data Transfer Service that the data source is done processing
        the run. No more status updates or requests to start/monitor jobs will be
        accepted. The run will be finalized by the Data Transfer Service when all
        monitored jobs are completed.
        Does not need to be called if the run is set to FAILED.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CreateDataSourceDefinition(self, request, context):
        """Creates a data source definition.  Calling this method will automatically
        use your credentials to create the following Google Cloud resources in
        YOUR Google Cloud project.
        1. OAuth client
        2. Pub/Sub Topics and Subscriptions in each supported_location_ids. e.g.,
        projects/{project_id}/{topics|subscriptions}/bigquerydatatransfer.{data_source_id}.{location_id}.run
        The field data_source.client_id should be left empty in the input request,
        as the API will create a new OAuth client on behalf of the caller. On the
        other hand data_source.scopes usually need to be set when there are OAuth
        scopes that need to be granted by end users.
        3. We need a longer deadline due to the 60 seconds SLO from Pub/Sub admin
        Operations. This also applies to update and delete data source definition.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateDataSourceDefinition(self, request, context):
        """Updates an existing data source definition. If changing
        supported_location_ids, triggers same effects as mentioned in "Create a
        data source definition."
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteDataSourceDefinition(self, request, context):
        """Deletes a data source definition, all of the transfer configs associated
        with this data source definition (if any) must be deleted first by the user
        in ALL regions, in order to delete the data source definition.
        This method is primarily meant for deleting data sources created during
        testing stage.
        If the data source is referenced by transfer configs in the region
        specified in the request URL, the method will fail immediately. If in the
        current region (e.g., US) it's not used by any transfer configs, but in
        another region (e.g., EU) it is, then although the method will succeed in
        region US, but it will fail when the deletion operation is replicated to
        region EU. And eventually, the system will replicate the data source
        definition back from EU to US, in order to bring all regions to
        consistency. The final effect is that the data source appears to be
        'undeleted' in the US region.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetDataSourceDefinition(self, request, context):
        """Retrieves an existing data source definition."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListDataSourceDefinitions(self, request, context):
        """Lists supported data source definitions."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_DataSourceServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "UpdateTransferRun": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateTransferRun,
            request_deserializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datasource__pb2.UpdateTransferRunRequest.FromString,
            response_serializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_transfer__pb2.TransferRun.SerializeToString,
        ),
        "LogTransferRunMessages": grpc.unary_unary_rpc_method_handler(
            servicer.LogTransferRunMessages,
            request_deserializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datasource__pb2.LogTransferRunMessagesRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        "StartBigQueryJobs": grpc.unary_unary_rpc_method_handler(
            servicer.StartBigQueryJobs,
            request_deserializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datasource__pb2.StartBigQueryJobsRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        "FinishRun": grpc.unary_unary_rpc_method_handler(
            servicer.FinishRun,
            request_deserializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datasource__pb2.FinishRunRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        "CreateDataSourceDefinition": grpc.unary_unary_rpc_method_handler(
            servicer.CreateDataSourceDefinition,
            request_deserializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datasource__pb2.CreateDataSourceDefinitionRequest.FromString,
            response_serializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datasource__pb2.DataSourceDefinition.SerializeToString,
        ),
        "UpdateDataSourceDefinition": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateDataSourceDefinition,
            request_deserializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datasource__pb2.UpdateDataSourceDefinitionRequest.FromString,
            response_serializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datasource__pb2.DataSourceDefinition.SerializeToString,
        ),
        "DeleteDataSourceDefinition": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteDataSourceDefinition,
            request_deserializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datasource__pb2.DeleteDataSourceDefinitionRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        "GetDataSourceDefinition": grpc.unary_unary_rpc_method_handler(
            servicer.GetDataSourceDefinition,
            request_deserializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datasource__pb2.GetDataSourceDefinitionRequest.FromString,
            response_serializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datasource__pb2.DataSourceDefinition.SerializeToString,
        ),
        "ListDataSourceDefinitions": grpc.unary_unary_rpc_method_handler(
            servicer.ListDataSourceDefinitions,
            request_deserializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datasource__pb2.ListDataSourceDefinitionsRequest.FromString,
            response_serializer=google_dot_cloud_dot_bigquery_dot_datatransfer__v1_dot_proto_dot_datasource__pb2.ListDataSourceDefinitionsResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "google.cloud.bigquery.datatransfer.v1.DataSourceService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
