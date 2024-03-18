from concurrent import futures
import time

import grpc
import greet_pb2
import greet_pb2_grpc


class GreeterServicer(greet_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        print(f"Request made: \n{request}")

        hello_reply = greet_pb2.HelloReply()
        hello_reply.message = f"{request.greeting} {request.name}"

        return hello_reply

    def ParrotSaysHello(self, request, context):
        print(f"Request made: \n{request}")

        for i in range(3):
            hello_reply = greet_pb2.HelloReply()
            hello_reply.message = f"{i+1}. {request.greeting} {request.name}"
            yield hello_reply
            time.sleep(3)

    def ChattyClientSaysHello(self, request_iterator, context):
        delayed_reply = greet_pb2.DelayedReply()
        for i, request in enumerate(request_iterator):
            print(f"Request made: \n{request}")

            hello_reply = greet_pb2.HelloReply()
            hello_reply.message = f"{i+1}. {request.greeting} {request.name}"
            delayed_reply.message.append(hello_reply)

        return delayed_reply

    def InteractingHello(self, request_iterator, context):
        for request in request_iterator:
            print(f"InteractingHello Request Made: \n{request}")

            hello_reply = greet_pb2.HelloReply()
            hello_reply.message = f"{request.greeting} {request.name}"

            yield hello_reply


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greet_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port("localhost:50000")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
