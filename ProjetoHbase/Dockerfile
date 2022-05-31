FROM Hbase 

# RUN serve para rodar um comado shell script na criacao da imagem docker
RUN apt-get update && apt-get install python3-pip -y \ 
    && apt-get install nano -y
# ao iniciar o container, o mesmo apresenta o console 
ENTRYPOINT ["/bin/bash"]
#docker build -t minha-imagem .
#docker run --name mi -it minha-imagem