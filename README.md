# rabbitmq
Uma das formas de se diminuir o acoplamento entre componentes de uma aplicação é a utilização de um message broker, que é um padrão arquitetural para envio e recebimento de mensagens entre aplicações e componentes. Onde quem envia a mensagem e quem recebe a mensagem não precisam conhecer um ao outro, diminuindo o acoplamento. 

Existem diversas aplicações que implementam esse padrão, entre elas o RabbitMQ, que implementa o protocolo AMPQ — Advanced Message Queuing Protocol 

RabbitMQ - https://www.rabbitmq.com

Pika is a pure-Python implementation of the AMQP 0-9-1 protocol that tries to stay fairly independent of the underlying network support library.

Pika - https://pika.readthedocs.io/en/stable/

```
# Para rodar com docker, basta rodar a seguinte linha de comando:
$ docker run --rm -p 5672:5672 -p 8080:15672 rabbitmq:3-management
```

```
# Server1 - Broker
# http://ip-rabbitmq:8080
# user: guest, password: guest
```

```
# Server2 - Produtor
$ pip install pika
$ python produtor.py
```

```
# Server3 - Consumidor1
$ pip install pika
$ python consumidor1.py
```

```
# Server4 - Consumidor2
$ pip install pika
$ python consumidor2.py
```

