#partindo da imagem ubuntu
FROM ubuntu:latest 
# ao iniciar o container, o mesmo apresenta o console 
ENTRYPOINT ["/bin/bash"]
# docker build -t minha-imagem .
#docker run --name mi - it minha imagem 

