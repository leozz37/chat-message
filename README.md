# Python chat message

Simple server and client using websocket, built for studies purpose.

### Getting started

Clone this repository to "safe place" on your machine.

`$ git clone https://github.com/leozz37/chat-message.git`

`$ cd chat-message`

### Prerequisites

Make sure you have [Python](https://www.python.org/downloads/) and [Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/) (optional) installed.
Besides that, this application only uses libs that comes with Python.

### The basics

This application requires a [Server](src/Server.py) running, then you can have multiples [Clients](src/Client.py)
running at the same time and exchange messages between them. A host and port is required for the server, you can use _localhost_ and any port that makes you happy (_5000_ is the default one). You can set them up on the [config file](src/ServerConfig.json).

### Running

#### Server

For the server, you can either run the .py file by hand or use docker for it.

##### Docker

First build the container

`$ docker build -t chat-server .`

Run the container

`$ docker run -it -d --rm -p 5000:5000 --name=server-chat chat-server`

##### File

Run the Server

`$ python3 src/Server.py`

#### Client

Run the Client file

`$ python3 src/Client.py`

### Author

Feel free to make any changes or adaptations. Any questions I'll be anwsering on my email

- Leonardo Lima - _leonardoaugusto287@gmail.com_


### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.


