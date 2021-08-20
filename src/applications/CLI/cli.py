import click
import pandas as pd
from src.app import app
from src.domains.tag import Tag
from src.applications.card import CreateCard
from src.interfaces.card import CreateCardInterface


@click.command()
@click.argument('file',default='')
def start_service(file):
    """ Usando CLI podemos receber um csv com cards prontos para mostrar no front de cara
        Exemplo de como o csv deve estar:
            text,tag
            Lorem ipsum dolor sit amet., tag1;tag2;tag3
            Mauris fringilla non quam vel lacinia,tag3
            Cras in tempus libero,

        [NOTE] - Todas as tags separada por ; .
    """
    if file != '':
        data = pd.read_csv(file)
        print(data['tag'][2])
        for num_line,linha in enumerate(data['text']):
            line_tag = str(data['tag'][num_line])
            print(line_tag)
            if ';' in line_tag:
                line_tags = line_tag.split(';')
                list_interface_tag = list(map(lambda tag_name: Tag(id= Tag.generate_id(), name=tag_name),line_tags))
                interface_card = CreateCardInterface(text=linha,tags=list_interface_tag)
            else:
                tag = [Tag(id= Tag.generate_id(), name=line_tag)]
                interface_card = CreateCardInterface(text=linha,tags=tag)
                print(interface_card)
            CreateCard.run(interface_card)
        app.run(port=8000)
    else:
        app.run(port=8000)