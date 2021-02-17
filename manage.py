from os import getenv
import bottle
from app import create_app

app = create_app()


def run_app(port=8080):
    app.run(port=port)


if __name__ == '__main__':
    run_app()
