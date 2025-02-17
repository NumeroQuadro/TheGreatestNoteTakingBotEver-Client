# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import NotesService_pb2 as NotesService__pb2

GRPC_GENERATED_VERSION = '1.66.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in NotesService_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class NotesServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddUser = channel.unary_unary(
                '/notes_service.NotesService/AddUser',
                request_serializer=NotesService__pb2.AddUserRequest.SerializeToString,
                response_deserializer=NotesService__pb2.AddUserResponse.FromString,
                _registered_method=True)
        self.LinkNoteWithUser = channel.unary_unary(
                '/notes_service.NotesService/LinkNoteWithUser',
                request_serializer=NotesService__pb2.LinkNoteWithUserRequest.SerializeToString,
                response_deserializer=NotesService__pb2.LinkNoteWithUserResponse.FromString,
                _registered_method=True)
        self.AddNoteSpecificDetails = channel.unary_unary(
                '/notes_service.NotesService/AddNoteSpecificDetails',
                request_serializer=NotesService__pb2.AddNoteSpecificDetailsRequest.SerializeToString,
                response_deserializer=NotesService__pb2.AddNoteSpecificDetailsResponse.FromString,
                _registered_method=True)
        self.AddNote = channel.unary_unary(
                '/notes_service.NotesService/AddNote',
                request_serializer=NotesService__pb2.AddNoteRequest.SerializeToString,
                response_deserializer=NotesService__pb2.AddNoteResponse.FromString,
                _registered_method=True)
        self.AddDescription = channel.unary_unary(
                '/notes_service.NotesService/AddDescription',
                request_serializer=NotesService__pb2.AddDescriptionRequest.SerializeToString,
                response_deserializer=NotesService__pb2.AddDescriptionResponse.FromString,
                _registered_method=True)
        self.AddComment = channel.unary_unary(
                '/notes_service.NotesService/AddComment',
                request_serializer=NotesService__pb2.AddCommentRequest.SerializeToString,
                response_deserializer=NotesService__pb2.AddCommentResponse.FromString,
                _registered_method=True)
        self.GetUserByTelegramId = channel.unary_unary(
                '/notes_service.NotesService/GetUserByTelegramId',
                request_serializer=NotesService__pb2.GetUserByTelegramIdRequest.SerializeToString,
                response_deserializer=NotesService__pb2.GetUserResponse.FromString,
                _registered_method=True)
        self.GetUserById = channel.unary_unary(
                '/notes_service.NotesService/GetUserById',
                request_serializer=NotesService__pb2.GetUserByIdRequest.SerializeToString,
                response_deserializer=NotesService__pb2.GetUserResponse.FromString,
                _registered_method=True)
        self.GetNoteById = channel.unary_unary(
                '/notes_service.NotesService/GetNoteById',
                request_serializer=NotesService__pb2.GetNoteByIdRequest.SerializeToString,
                response_deserializer=NotesService__pb2.GetNoteResponse.FromString,
                _registered_method=True)
        self.GetNoteByShortName = channel.unary_unary(
                '/notes_service.NotesService/GetNoteByShortName',
                request_serializer=NotesService__pb2.GetNoteByShortNameRequest.SerializeToString,
                response_deserializer=NotesService__pb2.GetNoteResponse.FromString,
                _registered_method=True)
        self.GetNoteByUrl = channel.unary_unary(
                '/notes_service.NotesService/GetNoteByUrl',
                request_serializer=NotesService__pb2.GetNoteByUrlRequest.SerializeToString,
                response_deserializer=NotesService__pb2.GetNoteResponse.FromString,
                _registered_method=True)
        self.GetNotesSpecificDetails = channel.unary_unary(
                '/notes_service.NotesService/GetNotesSpecificDetails',
                request_serializer=NotesService__pb2.GetNotesSpecificDetailsRequest.SerializeToString,
                response_deserializer=NotesService__pb2.GetNotesSpecificDetailsResponse.FromString,
                _registered_method=True)
        self.GetDescription = channel.unary_unary(
                '/notes_service.NotesService/GetDescription',
                request_serializer=NotesService__pb2.GetDescriptionRequest.SerializeToString,
                response_deserializer=NotesService__pb2.GetDescriptionResponse.FromString,
                _registered_method=True)
        self.GetComment = channel.unary_unary(
                '/notes_service.NotesService/GetComment',
                request_serializer=NotesService__pb2.GetCommentRequest.SerializeToString,
                response_deserializer=NotesService__pb2.GetCommentResponse.FromString,
                _registered_method=True)
        self.GetUsersNotes = channel.unary_unary(
                '/notes_service.NotesService/GetUsersNotes',
                request_serializer=NotesService__pb2.GetUsersNotesRequest.SerializeToString,
                response_deserializer=NotesService__pb2.GetUsersNotesResponse.FromString,
                _registered_method=True)
        self.RemoveNote = channel.unary_unary(
                '/notes_service.NotesService/RemoveNote',
                request_serializer=NotesService__pb2.RemoveNoteRequest.SerializeToString,
                response_deserializer=NotesService__pb2.RemoveNoteResponse.FromString,
                _registered_method=True)
        self.RemoveUser = channel.unary_unary(
                '/notes_service.NotesService/RemoveUser',
                request_serializer=NotesService__pb2.RemoveUserRequest.SerializeToString,
                response_deserializer=NotesService__pb2.RemoveUserResponse.FromString,
                _registered_method=True)


class NotesServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LinkNoteWithUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddNoteSpecificDetails(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddNote(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddDescription(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddComment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserByTelegramId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNoteById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNoteByShortName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNoteByUrl(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNotesSpecificDetails(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDescription(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetComment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUsersNotes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveNote(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NotesServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddUser': grpc.unary_unary_rpc_method_handler(
                    servicer.AddUser,
                    request_deserializer=NotesService__pb2.AddUserRequest.FromString,
                    response_serializer=NotesService__pb2.AddUserResponse.SerializeToString,
            ),
            'LinkNoteWithUser': grpc.unary_unary_rpc_method_handler(
                    servicer.LinkNoteWithUser,
                    request_deserializer=NotesService__pb2.LinkNoteWithUserRequest.FromString,
                    response_serializer=NotesService__pb2.LinkNoteWithUserResponse.SerializeToString,
            ),
            'AddNoteSpecificDetails': grpc.unary_unary_rpc_method_handler(
                    servicer.AddNoteSpecificDetails,
                    request_deserializer=NotesService__pb2.AddNoteSpecificDetailsRequest.FromString,
                    response_serializer=NotesService__pb2.AddNoteSpecificDetailsResponse.SerializeToString,
            ),
            'AddNote': grpc.unary_unary_rpc_method_handler(
                    servicer.AddNote,
                    request_deserializer=NotesService__pb2.AddNoteRequest.FromString,
                    response_serializer=NotesService__pb2.AddNoteResponse.SerializeToString,
            ),
            'AddDescription': grpc.unary_unary_rpc_method_handler(
                    servicer.AddDescription,
                    request_deserializer=NotesService__pb2.AddDescriptionRequest.FromString,
                    response_serializer=NotesService__pb2.AddDescriptionResponse.SerializeToString,
            ),
            'AddComment': grpc.unary_unary_rpc_method_handler(
                    servicer.AddComment,
                    request_deserializer=NotesService__pb2.AddCommentRequest.FromString,
                    response_serializer=NotesService__pb2.AddCommentResponse.SerializeToString,
            ),
            'GetUserByTelegramId': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserByTelegramId,
                    request_deserializer=NotesService__pb2.GetUserByTelegramIdRequest.FromString,
                    response_serializer=NotesService__pb2.GetUserResponse.SerializeToString,
            ),
            'GetUserById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserById,
                    request_deserializer=NotesService__pb2.GetUserByIdRequest.FromString,
                    response_serializer=NotesService__pb2.GetUserResponse.SerializeToString,
            ),
            'GetNoteById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetNoteById,
                    request_deserializer=NotesService__pb2.GetNoteByIdRequest.FromString,
                    response_serializer=NotesService__pb2.GetNoteResponse.SerializeToString,
            ),
            'GetNoteByShortName': grpc.unary_unary_rpc_method_handler(
                    servicer.GetNoteByShortName,
                    request_deserializer=NotesService__pb2.GetNoteByShortNameRequest.FromString,
                    response_serializer=NotesService__pb2.GetNoteResponse.SerializeToString,
            ),
            'GetNoteByUrl': grpc.unary_unary_rpc_method_handler(
                    servicer.GetNoteByUrl,
                    request_deserializer=NotesService__pb2.GetNoteByUrlRequest.FromString,
                    response_serializer=NotesService__pb2.GetNoteResponse.SerializeToString,
            ),
            'GetNotesSpecificDetails': grpc.unary_unary_rpc_method_handler(
                    servicer.GetNotesSpecificDetails,
                    request_deserializer=NotesService__pb2.GetNotesSpecificDetailsRequest.FromString,
                    response_serializer=NotesService__pb2.GetNotesSpecificDetailsResponse.SerializeToString,
            ),
            'GetDescription': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDescription,
                    request_deserializer=NotesService__pb2.GetDescriptionRequest.FromString,
                    response_serializer=NotesService__pb2.GetDescriptionResponse.SerializeToString,
            ),
            'GetComment': grpc.unary_unary_rpc_method_handler(
                    servicer.GetComment,
                    request_deserializer=NotesService__pb2.GetCommentRequest.FromString,
                    response_serializer=NotesService__pb2.GetCommentResponse.SerializeToString,
            ),
            'GetUsersNotes': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUsersNotes,
                    request_deserializer=NotesService__pb2.GetUsersNotesRequest.FromString,
                    response_serializer=NotesService__pb2.GetUsersNotesResponse.SerializeToString,
            ),
            'RemoveNote': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveNote,
                    request_deserializer=NotesService__pb2.RemoveNoteRequest.FromString,
                    response_serializer=NotesService__pb2.RemoveNoteResponse.SerializeToString,
            ),
            'RemoveUser': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveUser,
                    request_deserializer=NotesService__pb2.RemoveUserRequest.FromString,
                    response_serializer=NotesService__pb2.RemoveUserResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'notes_service.NotesService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('notes_service.NotesService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class NotesService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/notes_service.NotesService/AddUser',
            NotesService__pb2.AddUserRequest.SerializeToString,
            NotesService__pb2.AddUserResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def LinkNoteWithUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/notes_service.NotesService/LinkNoteWithUser',
            NotesService__pb2.LinkNoteWithUserRequest.SerializeToString,
            NotesService__pb2.LinkNoteWithUserResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def AddNoteSpecificDetails(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/notes_service.NotesService/AddNoteSpecificDetails',
            NotesService__pb2.AddNoteSpecificDetailsRequest.SerializeToString,
            NotesService__pb2.AddNoteSpecificDetailsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def AddNote(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/notes_service.NotesService/AddNote',
            NotesService__pb2.AddNoteRequest.SerializeToString,
            NotesService__pb2.AddNoteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def AddDescription(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/notes_service.NotesService/AddDescription',
            NotesService__pb2.AddDescriptionRequest.SerializeToString,
            NotesService__pb2.AddDescriptionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def AddComment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/notes_service.NotesService/AddComment',
            NotesService__pb2.AddCommentRequest.SerializeToString,
            NotesService__pb2.AddCommentResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetUserByTelegramId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/notes_service.NotesService/GetUserByTelegramId',
            NotesService__pb2.GetUserByTelegramIdRequest.SerializeToString,
            NotesService__pb2.GetUserResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetUserById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/notes_service.NotesService/GetUserById',
            NotesService__pb2.GetUserByIdRequest.SerializeToString,
            NotesService__pb2.GetUserResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetNoteById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/notes_service.NotesService/GetNoteById',
            NotesService__pb2.GetNoteByIdRequest.SerializeToString,
            NotesService__pb2.GetNoteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetNoteByShortName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/notes_service.NotesService/GetNoteByShortName',
            NotesService__pb2.GetNoteByShortNameRequest.SerializeToString,
            NotesService__pb2.GetNoteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetNoteByUrl(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/notes_service.NotesService/GetNoteByUrl',
            NotesService__pb2.GetNoteByUrlRequest.SerializeToString,
            NotesService__pb2.GetNoteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetNotesSpecificDetails(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/notes_service.NotesService/GetNotesSpecificDetails',
            NotesService__pb2.GetNotesSpecificDetailsRequest.SerializeToString,
            NotesService__pb2.GetNotesSpecificDetailsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetDescription(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/notes_service.NotesService/GetDescription',
            NotesService__pb2.GetDescriptionRequest.SerializeToString,
            NotesService__pb2.GetDescriptionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetComment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/notes_service.NotesService/GetComment',
            NotesService__pb2.GetCommentRequest.SerializeToString,
            NotesService__pb2.GetCommentResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetUsersNotes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/notes_service.NotesService/GetUsersNotes',
            NotesService__pb2.GetUsersNotesRequest.SerializeToString,
            NotesService__pb2.GetUsersNotesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RemoveNote(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/notes_service.NotesService/RemoveNote',
            NotesService__pb2.RemoveNoteRequest.SerializeToString,
            NotesService__pb2.RemoveNoteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RemoveUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/notes_service.NotesService/RemoveUser',
            NotesService__pb2.RemoveUserRequest.SerializeToString,
            NotesService__pb2.RemoveUserResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
