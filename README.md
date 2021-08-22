# Desafio
- O desáfio proposto se encontra <a href="https://github.com/producao-conteudo/desafio">aqui</a>.

## Lógica do back-end
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
   cd desafio/back-end/
   ```

2. **Crie e entre em um ambiente virtual** <br>
    Este passo é **opcional**, porém é recomendado para manter o projeto com suas dependencias e bibliotecas separados dos demais projetos que possa haver, onde ele será executado.

    ```
    pip install virtualenv
    ```
    ```
    python -m virtualenv venv
    ```
    **Entrando no ambiente virtual:** <br>
    windows:
    ```
    . venv/Scripts/activate
    ```
    No linux vai ser algo assim:
    ```
    . venv/bin/activate
    ```
3. **Instale todas as bibliotecas necessarias para a execução do programa** <br>  
   ```
   pip install -r requirements.txt
   ```
4. **Execute o back-end** <br>
   **Execute passando um csv para iniciar com alguns cards, deixei um exemplo para teste fique avontade**
   ```
   python server.py csv-exemplo.csv
   ```
   ou apenas: 
   ```
    python server.py
   ```
5. **Veja a documentação nesse endpoint**
  - http://127.0.0.1:8000/v1/reference/

## Executando o front-end
1. **Instale o CLI** <br>
  **Abra um novo terminal na pasta raiz do projeto(não feche o back-end deixe ele executando)**
  ```
  cd front-end/
  ```
2. **Caso ainda não tenha o vue instalado instale agora**
  ```
  npm install -g @vue/cli
  ```
3. **Instale as dependências**
  ```
   npm install
  ```
4. **Execute o front-end**

  ```
  npm run serve
  ```