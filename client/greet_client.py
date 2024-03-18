import time

import grpc
import greet_pb2
import greet_pb2_grpc


def get_client_stream_requests():
    while True:
        name = input("Enter a name or nothing to stop: ")

        if name == "":
            break

        hello_request = greet_pb2.HelloRequest(greeting="Hola", name=name)
        yield hello_request
        time.sleep(1)


def run():
    with grpc.insecure_channel("localhost:50000") as channel:
        stub = greet_pb2_grpc.GreeterStub(channel)
        print("1. SayHello - Unary")
        print("2. ParrotHello - Server side streaming")
        print("3. ChattyClientSaysHello - Client side streaming")
        print("4. InteractingHello - Both streaming")
        rpc_call = input("Which would yo like to make: ")

        if rpc_call == "1":
            hello_request = greet_pb2.HelloRequest(greeting="Hola", name="Pepe")
            hello_reply = stub.SayHello(hello_request)
            print(f"SayHello Response received: \n{hello_reply.message}")

        elif rpc_call == "2":
            hello_request = greet_pb2.HelloRequest(greeting="Hola", name="Pepe")
            hello_replies = stub.ParrotSaysHello(hello_request)
            for hello_reply in hello_replies:
                print(f"ParrotSaysHello Response received: \n{hello_reply.message}")

        elif rpc_call == "3":
            delayed_reply = stub.ChattyClientSaysHello(get_client_stream_requests())

            print(f"ChattyClientSaysHello Response received:")
            print(delayed_reply.message[0].message)
            print(type(delayed_reply.message[0].message))

        elif rpc_call == "4":
            responses = stub.InteractingHello(get_client_stream_requests())

            for response in responses:
                print(f"InteractingHello response received: \n{response.message}")
                print(response)


if __name__ == "__main__":
    run()
