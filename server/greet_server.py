from concurrent import futures
import time
import requests

import grpc
import greet_pb2
import greet_pb2_grpc


class GreeterServicer(greet_pb2_grpc.GreeterServicer):
    def SayGame(self, request, context):
        print(f"Request made: \n{request}")

        game_reply = greet_pb2.GameReply()
        headers = {
            "Client-ID": "vg18rbj94iklg3vc16q4dgf4hn0z0y",
            "Authorization": "Bearer wkvw7wngvvtgbmct4d70c932rcebhi",
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = f'fields name, involved_companies.company.name, platforms.name; search "{request.game}"; limit 1;'

        game = requests.post(
            "https://api.igdb.com/v4/games", headers=headers, data=data
        )
        print(game.json()[0]["name"])

        game_reply.message = f"{game.json()[0]['name']}"

        return game_reply

    def SayConsole(self, request, context):
        print(f"Request made: \n{request}")

        for i in range(3):
            game_reply = greet_pb2.GameReply()
            game_reply.message = f"{request.game} {i}. is in {request.console}"
            yield game_reply
            time.sleep(1)

    def StreamGames(self, request_iterator, context):
        for request in request_iterator:
            print(f"InteractingHello Request Made: \n{request}")

            game_reply = greet_pb2.HelloReply()
            game_reply.message = f"{request.greeting} {request.name}"

            yield game_reply


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greet_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
