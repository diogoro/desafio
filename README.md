# desafio

## Proposta

A solução proposta são 3 micro serviços acessando as bases A, B e C. Dado os requisitos de cada a proposta é que a base A ficará no Amazon Aurora, a base B ficará no Amazon DynamoDB e a base C no Amazon ElastiCache for Redis.
Os micros serviços que acessarão as bases A e B devido a restrição de segurança deverão implementar autorização via JWT para suprir esse requisito. O micro serviço que acessa a base C pode ser acessado sem token.
Os micro serviços deverão serem desenvolvidos na linguagem python e publicados em imagens docker no serviço Amazon Elastic Container Service.

![](https://github.com/diogoro/desafio/blob/master/solucao.png)

## Aplicação

A aplicação desenvolvida é o micro serviço que acessa a base C, que serve para manter os eventos financeiros de um CPF. O arquivo Desafio.postman_collection.json pode ser usado para testes da aplicação.
Para executar a aplicação é necessário ter na máquina o docker e o docker-compose;
A aplicação está implementado em uma imagem docker e usando outra imagem docker do redis.

## Instuções para executar:

`$ git clone git@github.com:diogoro/desafio.git`

`$ cd desafio`

`$ docker-compose up`

O serviço estará funcionando no endereço http://127.0.0.1:5000/financeEvent/

### Stack
- Python 3.8
- Flask
- Redis
- Docker
