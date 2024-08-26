import NotesService_pb2_grpc
import NotesService_pb2
import time
import grpc
from grpc import RpcError


def run():
    try:
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = NotesService_pb2_grpc.NotesServiceStub(channel)
            
            # Create the AddUserRequest object using keyword arguments
            request = NotesService_pb2.AddUserRequest(
                user_telegram_tag="osifdj",
                user_telegram_id=23
            )
            
            # Call AddUser with the request object
            response = stub.AddUser(request)
            print("Client received: " + response.user.user_telegram_tag)
    except RpcError as e:
        print(f"RPC error occurred: {e.code()} - {e.details()}")
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run()