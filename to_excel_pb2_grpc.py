# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import to_excel_pb2 as to__excel__pb2


class GreeterStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Excel = channel.unary_unary(
                '/Greeter/Excel',
                request_serializer=to__excel__pb2.JsonFileRequest.SerializeToString,
                response_deserializer=to__excel__pb2.ExcelFileReply.FromString,
                )


class GreeterServicer(object):
    """The greeting service definition.
    """

    def Excel(self, request, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Excel': grpc.unary_unary_rpc_method_handler(
                    servicer.Excel,
                    request_deserializer=to__excel__pb2.JsonFileRequest.FromString,
                    response_serializer=to__excel__pb2.ExcelFileReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Greeter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Greeter(object):
    """The greeting service definition.
    """

    @staticmethod
    def Excel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Greeter/Excel',
            to__excel__pb2.JsonFileRequest.SerializeToString,
            to__excel__pb2.ExcelFileReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
