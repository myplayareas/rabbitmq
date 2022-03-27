# rabbitmq
Uma das formas de se diminuir o acoplamento entre componentes de uma aplicação é a utilização de um message broker, que é um padrão arquitetural para envio e recebimento de mensagens entre aplicações e componentes. Onde quem envia a mensagem e quem recebe a mensagem não precisa conhecer um ao outro, diminuindo o acoplamento. 

Existem diversas aplicações que implementam esse padrão, entre elas o RabbitMQ, que implementa o protocolo AMPQ (*Advanced Message Queuing Protocol*). O protocolo AMQP possibilita pub-sub (publicação/assinatura) e enfileiramento de mensagens assíncronas.

RabbitMQ - https://www.rabbitmq.com

Pika is a pure-Python implementation of the AMQP 0-9-1 protocol that tries to stay fairly independent of the underlying network support library.

Pika - https://pika.readthedocs.io/en/stable/

## Como viabilizar uma comunicação assíncrona e independente entre um produtor e dois consumidores?

Exemplo: Broker, Produtor, Consumidor1, Consumidor2, instantantes (t0 < t1 < t2 < t3 < t4 < t5). Como os serviços (Broker, Produtor, Consumidor1 e Consumidor2) rodam em aplicações e processos separados, a comunicação entre eles é feita de forma assíncrona e desacoplada.

t0: Inicializa o Broker: q = []

t1: Produtor->Broker: q = [message1]

t2: Produtor->Broker: q = [message1, message2]

t3: Consumidor1->Broker: q = [message1,message2]

t4: Consumidor2->Broker: q = [message2]

t5: Broker: q = []

```sequence
Produtor->Broker: message1
Produtor->Broker: message2
Consumidor1->Broker: message1
Consumidor2->Broker: message2
```

### Ativar o servidor que ficará responsável pelo controle de mensageria

Neste caso, existe apenas uma fila de mensagens que será usada para intermediar a produção das mensagens e consumo das mensagens

```
# Para rodar com docker, basta rodar a seguinte linha de comando:
$ docker run --rm -p 5672:5672 -p 8080:15672 rabbitmq:3-management
```

```
# Server1 - Broker
# http://ip-rabbitmq:8080
# user: guest, password: guest
# Crie a fila (q) que vai gerenciar as mensagens
```
### Ativar o servidor (Produtor) que vai produzir as mensagens para a fila

```
# Server2 - Produtor
# http://ip-produtor:8080
$ pip install pika
$ python produtor.py
# Produtor->Broker: message1
# Produtor->Broker: message2
```
### Ativar o servidor (Consumidor 1) que vai consumir as mensagens armazenadas na fila
```
# Server3 - Consumidor1
# http://ip-consumidor1:8080
$ pip install pika
$ python consumidor1.py
# Consumidor1->Broker: message1
```
### Ativar o servidor (Consumidor 2) que vai consumir as mensagens armazenadas na fila
```
# Server4 - Consumidor2
# http://ip-consumidor2:8080
$ pip install pika
$ python consumidor2.py
# Consumidor2->Broker: message2
```
