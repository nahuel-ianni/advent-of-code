"""
Module: main
Manages the solution automation via the 'Elves' package.
"""
from elves.application import cli_app


def main():
    cli_app.app()


if __name__ == "__main__":
    main()
