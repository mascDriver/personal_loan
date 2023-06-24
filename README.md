# Sistema de Gestão de Propostas de Empréstimo Pessoal

Este é o repositório do projeto "Sistema de Gestão de Propostas de Empréstimo Pessoal". Ele contém o código-fonte e os
recursos necessários para executar o sistema de forma local ou em um ambiente de produção.

## Tecnologias Utilizadas

- Django
- Django Rest Framework
- Django Celery
- RabbitMQ
- React

## Descrição

O Sistema de Gestão de Propostas de Empréstimo Pessoal é uma aplicação web desenvolvida com o framework Django. Ele
permite a criação, visualização e gerenciamento de propostas de empréstimo pessoal. Através da interface fornecida pelo
sistema, os usuários podem preencher formulários de propostas, acompanhar o status das solicitações e interagir com o
processo de aprovação.

O projeto utiliza o Django Rest Framework para fornecer uma API RESTful que permite a integração com outros sistemas e o
consumo de dados por aplicativos externos. O Django Celery é utilizado para processar tarefas assíncronas, como o envio
de e-mails de notificação ou a execução de cálculos complexos em segundo plano.

O RabbitMQ é utilizado como um serviço de mensageria para o processamento assíncrono de tarefas pelo Celery. Ele permite
a comunicação eficiente e confiável entre os diferentes componentes da aplicação.

O front-end do sistema é desenvolvido em React, proporcionando uma interface moderna e responsiva para os usuários
interagirem com as funcionalidades oferecidas.

## Executando o Sistema

Para executar o Sistema de Gestão de Propostas de Empréstimo Pessoal em seu ambiente local usando Docker Compose, siga
as etapas abaixo:

1. Clone este repositório em sua máquina:

    ```bash
    git clone https://github.com/mascDriver/personal_loan.git
    ```

2. Navegue até o diretório raiz do projeto:

    ```bash
    cd personal_loan
    ```

3. Execute o comando Docker Compose para construir e iniciar os contêineres:

    ```bash
    docker-compose up -d --build
    ```

Este comando irá baixar as imagens Docker necessárias, criar os contêineres e iniciar os serviços do sistema.

4. Aguarde até que todos os serviços estejam em execução. Após a conclusão, você poderá acessar o sistema através de seu
   navegador da web no endereço `http://localhost:3000`.

## Configuração

O Sistema de Gestão de Propostas de Empréstimo Pessoal utiliza variáveis de ambiente para sua configuração. As variáveis
de ambiente são definidas no arquivo `.env` localizado na raiz do projeto. Neste arquivo, você pode definir as
configurações específicas do seu ambiente, como chaves secretas, URLs de bancos de dados e outras variáveis necessárias.

Certifique-se de configurar corretamente as variáveis de ambiente no arquivo `.env` antes de executar o sistema com o
Docker Compose.

## Contribuição

Se você deseja contribuir para este projeto, siga as etapas abaixo:

1. Faça um fork deste repositório.
2. Crie um branch para sua nova funcionalidade ou correção de bug: `git checkout -


