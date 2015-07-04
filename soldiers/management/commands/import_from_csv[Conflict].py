from django.core.management.base import BaseCommand, CommandError
from soldiers.models import Soldier
import csv
import parsedatetime as pdt
import re
import datetime

# From: http://stackoverflow.com/a/11232512/977931
_digits = re.compile('\d')
def contains_digits(d):
    #print("-->", d, type(d))
    return bool(_digits.search(d))

class Command(BaseCommand):
    help = 'Imports soldier data from a CSV'

    def add_arguments(self, parser):
        parser.add_argument('file')

    def create_soldier(self, row):
        s = Soldier()
        #s.contributor = row[0].strip()
        #s.unique_id = int(row[1].strip())
        #s.pds_page_no = row[2].strip()
        #s.district = row[3].strip()
        #s.surname = row[4].strip()
        s.contributor = "Arun"
        s.unique_id = int(999)
        s.pds_page_no = row[2].strip()
        s.district = row[3].strip()
        s.surname = row[4].strip()
        s.name = row[5].strip()

        s.name = row[5].strip()
        s.rank = row[6].strip()
        s.desc = row[7] # Description
        s.unit_served = row[8].strip()
        s.service_no = row[9].strip()
        s.date_of_embarkation = row[10] # Assumes this is a already a date type
        s.died_in_service = row[11] 
        return s

    def handle(self, *args, **options):
        filename = options['file']
        self.stdout.write(filename)
        with open(filename, newline='', encoding='ISO-8859-1') as csvfile:
            r = csv.reader(csvfile)
            first_row = True
            for row in r:
                # Skip first row of columns
                if first_row:
                    first_row = False
                    continue
                date_of_embarkation = row[10].strip()
                #if date_of_embarkation and contains_digits(date_of_embarkation):
                #    p = pdt.Calendar()
                #    if date_of_embarkation.startswith("191"):
                #        date_of_embarkation = date_of_embarkation.replace(".", "-") 
                #        parsed_date_of_embarkation = datetime.datetime.strptime(date_of_embarkation, "%Y-%m-%d")
                #    else:
                #        parsed_date_of_embarkation = p.parse(date_of_embarkation)
                #    row[10] = parsed_date_of_embarkation
                #else:
                #    row[10] = None
                
                row[10] = None
                s = self.create_soldier(row)
                s.save()


