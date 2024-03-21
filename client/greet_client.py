import time

import grpc
import greet_pb2
import greet_pb2_grpc

from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route("/")
def hello():
    return "Nicolas P"


@app.route("/get-game", methods=["GET", "POST"])
def SayGame():
    with grpc.insecure_channel("localhost:50051") as channel:
        game_name = request.args.get("name")
        stub = greet_pb2_grpc.GreeterStub(channel)
        game_request = greet_pb2.GameRequest(game=game_name)
        game_reply = stub.SayGame(game_request)

    return jsonify({"name": game_reply.message})


@app.route("/get-console", methods=["GET", "POST"])
def SayConsole():
    with grpc.insecure_channel("localhost:50051") as channel:
        game_name = request.args.get("name")
        console = request.args.get("console")
        stub = greet_pb2_grpc.GreeterStub(channel)
        console_request = greet_pb2.ConsoleRequest(game=game_name, console=console)
        console_reply = stub.SayConsole(console_request)

        values = []
        for reply in console_reply:
            values.append({"message": reply.message})

    return jsonify(values)


def get_client_stream_requests():
    while True:
        name = input("Enter a name or nothing to stop: ")

        if name == "":
            break

        hello_request = greet_pb2.HelloRequest(greeting="Hola", name=name)
        yield hello_request
        time.sleep(1)


def run():
    with grpc.insecure_channel("127.17.0.2:50051") as channel:
        stub = greet_pb2_grpc.GreeterStub(channel)
        print("1. SayHello - Unary")
        print("2. ParrotHello - Server side streaming")
        print("3. ChattyClientSaysHello - Client side streaming")
        print("4. InteractingHello - Both streaming")
        rpc_call = input("Which would you like to make: ")

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


def main():
    app.run()


if __name__ == "__main__":
    main()
