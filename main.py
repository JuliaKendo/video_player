import os
from dotenv import load_dotenv
from livereload import Server


def main():
    load_dotenv()
    server_ip = os.getenv('SERVER_IP')
    server_port = os.getenv('SERVER_PORT')

    server = Server()
    server.watch('index.html')
    server.serve(root='.', host=server_ip, port=server_port)


if __name__ == "__main__":
    main()
