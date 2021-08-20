# Bot service

## Logica do back-end
   <p> Toda a arquitetura foi dividida em 5 pastas que são a forma toda a base sendo elas as aplications, domians, interfaces, infrastructure e api.</p>

* Responsabilidades:

    * intefaces - Prototipar dados de entrada nas apis junto com a função JSONPayload(), com isso podemos controlar se os tipos de dados estão entrando no formado correto.
    
    * api - Responsável por guarda nossos endpoints e e consumir a camada de applications. 

    * applications - Responsável por guarda toda a regra do serviço, nela temos as operações que se comunicão com a camada de infrastructure e domains para criar, atualizar, buscar e remover dados.
    
    * domains - Responsável pelo modelo dos objetos do nosso serviço e funções próprias, diferente da camada de interfaces, essa iremos consumir para cria objetos que serão tratados na camada de aplicação aplicando as regras de negócio.

    * infrastructure - Responsável por configurações e criação dos nossos repositorios. Nessa camada foi criado uma classe BaseRepository() com as operações principais do banco, onde passamos por herança para cada um dos nossos repositórios dessa forma mantemos por exemplo no repositório de cards apenas as operações extras que a camada de aplicação deseja consumir.
    

## Database
 - Foi usado o MongoDb para armazenar dados dividindo cards e tags em collections separadas, porem mantendo as relações de ids entre as tags e os cards. Então um diferentes cards irão poder ter a mesma tag com id e nome.

## Prerequisitos
  - Recomendo adicionar o python e o node as variáveis de ambientes do sistema na hora da instalação
- <a href="https://www.mongodb.com/try/download/community"> MongoDb</a> 
- <a href="https://www.python.org/downloads/">Python3</a> 
- <a href="https://nodejs.org/en/download">NodeJs</a>
- VueJs
  - npm install vue (digite no terminal)
  
## Executando o back-end
1. **Clone este repositório**

   ```
   git clone https://github.com/Simeone-Holanda/service_python.git
   ```
   ```
   cd desafio
   ```
2. **Configure seu MongoDb** <br>
    <p>Recomendo usar o xampp pela sua facilidade de configuração do mysql. Em seguida abra seu xampp e inicie os serviços do apache e do mysql, apos isso va até o arquivo settings.py no seguinte caminho cd/service_python/util/settings.py e adicione suas configurações para a conexão com o database e as demais constantes do projeto.</p>

   * Configurações padrão do arquivo setting.py :

     HOST = 'localhost'<br>
     USER = 'root'<br>
     PASSWD = ''<br>
     DB_NAME='name_db'<br><br>
   

3. **Crie e entre em um ambiente virtual** <br>
    Este passo é **opcional**, porém é recomendado para manter o projeto com suas dependencias e bibliotecas separados dos demais projetos que possa haver, onde ele será executado.
    ```
    pip3 install virtualenv
    ```
    ```
    python3 -m virtualenv venv
    ```
4. **Instale todas as bibliotecas necessarias para a execução do programa** <br>  
   ```
   pip3 install -r requirements.txt
   ```
5. **Execute o back-end**
   ```
   python server.py csv-exemplo.csv
   ```
   ou apenas: 
   ```
    python server.py
   ```
## Executando o front-end
1. **Instale o CLI**
  ```
  npm install -g @vue/cli
  ```
2. **Execute o front-end**
  ``` 
  cd front-end
  ```
  ```
  npm run serve
  ```