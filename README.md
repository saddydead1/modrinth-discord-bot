# Modrinth Discord Bot

This is a discord bot that allows you to notify server members about the release of a new version of your mod.

## How does this work?
You install a docker image on your machine. Using `env` you set the `id of your mod`, the `id of the channel` to which messages will be sent and `your token`. When launched, the bot records the current versions and then makes a request to the modrinth api every minute.

## Installation

* Clone the repository
```bash
git clone https://github.com/saddydead1/modrinth-discord-bot
cd modrinth-discord-bot/
```
* Build a docker image
```bash
docker build -t modrinthbot .
```
* Start a docker container
```bash
docker run -d -e ID=<YOUR_MOD_ID> -e CHANNEL_ID=<YOUR_CHANNEL_ID> -e TOKEN=<YOUR_TOKEN> modrinthbot  
```
_or use docker compose **( recommended )**_

## Docker Compose

```yaml
version: "3.7"
services:
  bot:
    image: modrinthbot
    environment:
      - CHANNEL_ID=<YOUR_CHANNEL_ID>
      - ID=<YOUR_MOD_ID>
      - TOKEN=<YOUR_TOKEN>
    restart: always
```
