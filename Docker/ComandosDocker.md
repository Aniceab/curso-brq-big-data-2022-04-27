
INSTALAÇÃO E CONFIGURAÇÃO DO AMBIENTE
Como instalar Docker no Ubuntu

https://docs.docker.com/engine/install/ubuntu/

#Apos a instalação Criar um container (os container são construidos apartir de uma imagem docker.Por padrão extrai essa imagens do Docker hub).

Baixando e Executando Imagens

#Realiza o download de uma imagen direto do Docker Hub
    docker pull nome_da_imagen #(exemplo docker pull ubuntu)
#Criar prorpria imagem 
    docker build -t minha-imagem .   
Executa um container

#Se existir localmente executa, senão realiza o download, valida e executa
    docker run nome_da_imagen

    dica: para executar o container em background sem travar o terminado use o comando -d, exemplo:
    
    docker run -d nome_da_imagen
    docker run hello-word #  comando run roda um container
    docker run --rm -it -p 80:80 strm/helloworld-http #(rm  serve para remover o container quando parar )
    docker start #quando o containers ja existe e vamos startar ele 
    docker stop # para a execução do contaires
#Lista todos os containers

     docker ps
     docker ps -a # lista inclusive containeres que não estão em execução
     container ls 
     container ls -a # lista inclusive containeres que não estão em execução
     docker ps  # lista  os containeres que estão em execução
     docker ps -a # lista inclusive containeres que não estão em execução

CONFIGURANDO PORTAS
#Mostrar o mapeamento de portas do container

    docker port id_do_container

#Mapeando portas ao criar o container

    docker run -d -P nome_da_imagen

#Detecta portas do container e vincula portas do host automaticamente

    docker run -d -p port_host:porta_container nome_da_imagen

#atribui uma porta especifica do host para uma porta do container

#paravisualização do portainer via web 
    docker run -d  -p 9003:9000 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce 

INTERAGINDO COM O CONTAINER
#Executando um comando no modo interativo

docker exec -it id_do_container comando

por exemplo, execute o comando:

docker exec -it id_do_container bash em um container ubuntu para acessar o terminal de forma interativa

outro exemplo:

doccker exec -it <NOME ou ID> /bin/bash # entra dentreo do container

Exibindo logs do Container

docker logs <Nome ou ID>  



