import pandas as pd
from django.core.management.base import BaseCommand
from terror.models import Aatanki


class Command(BaseCommand):

    def handle(self, *args, **options):
        df=pd.read_csv('test.csv',sep=';')
        for index, row in df.iterrows():
            list_names = row["name"].split('ALIAS')
            for name in list_names:
                print(name)
                Aatanki.objects.create(name = name)
           




           

 