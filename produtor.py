#!/usr/bin/env python
import pika
import random
   
rabbitmq_host = '192.168.0.8'
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
channel = connection.channel()
   
channel.queue_declare(queue='hello')
  
print('Conectado ao canal 1 na fila hello')
print('Enviando as mensagens..')
qtd_mensagens = 1500000
  
for i in range(0,qtd_mensagens):
  numero = random.randrange(qtd_mensagens)
  conteudo = 'Hello ' + str(i) + ' - ' + str(numero)
  channel.basic_publish(exchange='', routing_key='hello', body=conteudo)
  print(" [x] Sent {}".format(conteudo))
  
connection.close()

print('Conexao fechada')
