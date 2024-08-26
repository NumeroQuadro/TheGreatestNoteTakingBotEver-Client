import grpc
from concurrent import futures
import NotesService_pb2
import NotesService_pb2_grpc

import NotesService_pb2_grpc
import NotesService_pb2

class NotesService(NotesService_pb2_grpc.NotesServiceServicer):
    def AddUser(self, request, context):
        # Example implementation
        user = NotesService_pb2.User(
            user_id=1,
            user_telegram_tag=request.user_telegram_tag,
            user_telegram_id=request.user_telegram_id
        )
        print('fucking fuck!')
        return NotesService_pb2.AddUserResponse(user=user)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    NotesService_pb2_grpc.add_NotesServiceServicer_to_server(NotesService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
