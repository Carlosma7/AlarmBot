
# AlarmBot

Hi! Welcome to AlarmBot!

The project is an easy house alarm managed by a Telegram Bot.

<p align="center"><img src="https://raw.githubusercontent.com/Carlosma7/AlarmBot/main/img/logo.png"/></p> 

## Table of contents:

:medal_sports: [Badges](#badges)

:bird: [Description](#description)

:clapper: [Demo](#demo)

:notebook_with_decorative_cover: [User manual](#user-manual)

:gear: [Install](#install)

:couple: [How to contribute](#how-to-contribute)

:man: [Author](#author)

:copyright: [License](#license)

## Badges

**Project**.

[![Language](https://img.shields.io/badge/Language-Python-red.svg)](https://www.python.org/) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![Uvicorn](https://img.shields.io/badge/API-Uvicorn-violet.svg)](https://core.telegram.org/) [![Telegram](https://img.shields.io/badge/API-Telegram-cyan.svg)](https://core.telegram.org/) [![Framework](https://img.shields.io/badge/Framework-Telebot-red.svg)](https://github.com/eternnoir/pyTelegramBotAPI)

**Checks**.

[![Build Status](https://github.com/Carlosma7/AlarmBot/workflows/Pylint/badge.svg)](https://github.com/Carlosma7/AlarmBot/actions?query=workflow%3APylint)

## Description

**AlarmBot** comes up as a personal project that aspires to define an useful and simple Telegram Bot to manage a home alarm system. It just defines the registration system and the API to notify users via Telegram, not the alarm trigger.

For that purpose, it will use the [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) library to define a Telegram Bot, together with [FastAPI](https://fastapi.tiangolo.com/) as the framework for the API that triggers notifications, together with [Uvicorn](https://www.uvicorn.org/) as ASGI web server.

## Demo

<p align="center"><img src="https://github.com/Carlosma7/AlarmBot/blob/main/img/demo.gif?raw=true"/></p>

## User manual

**AlarmBot** is a simple system whose deployment just depends on a **.env** file that contains a **Token** from Telegram Bot (if you don't know how to obtain one, follow this [official tutorial](https://core.telegram.org/bots#6-botfather)).

Now, the available commands to work with AlarmBot are listed:

**Execute AlarmBot**
Starts a Telegram Bot and defines a FastAPI API with Uvicorn.

```shell
invoke execute
```

**Stop AlarmBot**
Stops the execution by killing the related processes.

```shell
invoke stop
```

**Clean AlarmBot**
Cleans the python caché and log files from both APIs.

```shell
invoke clean
```
 	
## Install

To install all dependencies you just need to execute the following:

```shell
pip3 install -r requirements.txt
```

## How to contribute

**AlarmBot** is an open source project that is open for new contributions if you want to. To contribute to the project you can [contact me](#author) or just open a new *pull request*. Thanks in advance!

## Author

**Carlos Morales Aguilera**

<img src="https://avatars.githubusercontent.com/u/14914668?v=4" width=200px/>

:octocat: [GitHub](https://github.com/Carlosma7)
:email: [Email](carlos7ma@gmail.com)
:busts_in_silhouette: [LinkedIn](https://www.linkedin.com/in/carlos-morales-aguilera/)

## License 

[LICENSE](https://github.com/Carlosma7/Twitter-Social-Analyzer/blob/main/LICENSE)

**GPLv3**: The permissions under this strong copyleft license are conditional on making the full source code of the licensed works and modifications, including larger works using a licensed work, available under the same license. Copyright and licensing notices should be retained. Taxpayers provide an express grant of patent rights.

**Permissions**:

* Commercial use.
* Distribution.
* Modification.
* Use of patent.
* Private use.

**Conditions**:

* Reveal source.
* License and copyright notice.
* Same license.
* State changes.

**Limitations**:

* Responsibility.
* Warranty.
