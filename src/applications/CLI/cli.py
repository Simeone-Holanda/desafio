import click
import pandas as pd
from src.domains.tag import Tag
from src.applications.card import CreateCard
from src.interfaces.card import CreateCardInterface


@click.command()
@click.argument('file',default='')
def import_csv(file):
    if file != '':
        data = pd.read_csv(file)
        for num_line,linha in enumerate(data['text']):
            line_tag = str(data['tag'][num_line])
            print(line_tag, "-="*30)
            if ';' in line_tag:
                print("Aqui - ",line_tag)
                line_tags = line_tag.split(';')
                list_interface_tag = list(map(lambda tag_name: Tag(id= Tag.generate_id(), name=tag_name),line_tags)) # criando a interface de tags
                interface_card = CreateCardInterface(text=linha,tags=list_interface_tag)
            else:
                tag = Tag(id= Tag.generate_id(), name=line_tag)
                interface_card = CreateCardInterface(text=linha,tags=tag)
            CreateCard.run(interface_card)
    else:
        pass