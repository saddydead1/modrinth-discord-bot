import logging
from bot.bot import Bot

def main() -> None:
    logging.basicConfig(level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s")

if __name__ == '__main__':
    main()
    Bot.init()