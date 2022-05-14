#Docker que é e como usar ?
É uma plataforma que facilita a criação e administração de ambientes isolados.Ele possibilira o empacotamento de uma aplicação dentro de um container, se tornando portateil para qualquer outro host que contenha docker instalado.
#O que é uma imagem ?
A imagem é um arquivo.Da perspectiva de SO(Sistema Operacional), um containers é um processo com restriçoes.No entando ao invés de executar um único arquivo binário, um conteiner executa uma imagem. Uma imagem é um pacote de sistema de arquivos que contém todas as dependências necessarias para executar um processo.
#Oque é uma container ?
Um container docker é um ambiente isolado. um container contém um conjunto de processos que são executados a partirt de uma imagem esta que fornece todos os arquivos necessarios.Os containers compartilham o mesmo kermel e isolam os processos e aplicação do restante do sistema.
Containers é um processo docker.
#Oque é um Volume ?
 é um link da pasta do sistema operacional para o container , tudo que vc fizer em uma pasta acontece na outra;
 exemplo se eu remover um arquivo no continer ele remove na pasta local, e se vc remover da pasta local remove do container.
 *Para motificar o doc , precisa ter o mesmo usuario de criação ,caso não tenha usar sudo nano.
