import sys

from app.greeting import greet


def main() -> None:
    print(greet(sys.argv[1] if len(sys.argv) > 1 else "world"))


if __name__ == "__main__":
    main()
