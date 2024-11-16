from django.core.management.base import BaseCommand
from django.db import transaction
from app.models import UniversityProgram, University


class Command(BaseCommand):
   help = 'Clean and standardize university names in UniversityProgram model'

   def get_university_mappings(self):
       return {
           '177': 'Westsächsische Hochschule Zwickau',
           '176': 'Universität zu Lübeck',
           '175': 'Universität Hamburg',
           '174': 'Universität Tübingen',
           '173': 'Universität Stuttgart',
           '172': 'Universität Siegen',
           '171': 'Universität Rostock',
           '170': 'Universität Regensburg',
           '169': 'Universität Potsdam',
           '168': 'Universität Passau',
           '167': 'Westfälische Wilhelms-Universität Münster',
           '166': 'Universität Konstanz',
           '165': 'Universität Koblenz',
           '164': 'Universität Kassel',
           '163': 'Universität Hildesheim',
           '162': 'Georg-August-Universität Göttingen',
           '161': 'Albert-Ludwigs-Universität Freiburg',
           '160': 'Universität Duisburg-Essen',
           '159': 'Universität Bremen',
           '158': 'Universität Bonn',
           '157': 'Universität Bayreuth',
           '156': 'Universität Bamberg',
           '155': 'Universität Augsburg',
           '154': 'Hochschule Emden/Leer',
           '153': 'Hochschule Ulm',
           '152': 'Universität Trier',
           '151': 'Technische Universität Ilmenau',
           '150': 'Technische Universität Braunschweig',
           '149': 'Technische Hochschule Köln',
           '148': 'Technische Hochschule Köln',
           '147': 'Technische Hochschule Ingolstadt',
           '146': 'Technische Universität München',
           '145': 'Technische Universität München',
           '144': 'Technische Universität Darmstadt',
           '143': 'Technische Hochschule Würzburg-Schweinfurt',
           '142': 'Hochschule Augsburg',
           '141': 'Technische Universität Dortmund',
           '140': 'Fachhochschule Südwestfalen',
           '139': 'Universität des Saarlandes',
           '138': 'SRH Hochschule Leipzig',
           '137': 'SRH Hochschule Heidelberg',
           '136': 'SRH Hochschule Hamburg',
           '135': 'SRH Hochschule Berlin',
           '134': 'Ruhr-Universität Bochum',
           '133': 'Hochschule Rhein-Waal',
           '132': 'Hochschule Rhein-Waal',
           '131': 'Rheinisch-Westfälische Technische Hochschule Aachen',
           '130': 'Rheinland-Pfälzische Technische Universität Kaiserslautern-Landau',
           '129': 'Philipps-Universität Marburg',
           '128': 'Universität Paderborn',
           '127': 'Otto-von-Guericke-Universität Magdeburg',
           '126': 'Ostbayerische Technische Hochschule Amberg-Weiden',
           '125': 'Universität Osnabrück',
           '124': 'Technische Hochschule Ostwestfalen-Lippe',
           '123': 'Ostbayerische Technische Hochschule Regensburg',
           '122': 'Hochschule Neubrandenburg',
           '121': 'Gottfried Wilhelm Leibniz Universität Hannover',
           '120': 'Fachhochschule Kiel',
           '119': 'Christian-Albrechts-Universität zu Kiel',
           '118': 'Karlsruher Institut für Technologie',
           '117': 'Julius-Maximilians-Universität Würzburg',
           '116': 'Hochschule Hof',
           '115': 'Hochschule für Technik Stuttgart',
           '114': 'Hochschule der Bayerischen Wirtschaft',
           '113': 'Hochschule München',
           '112': 'Hochschule Bonn-Rhein-Sieg',
           '111': 'Hochschule Bielefeld',
           '110': 'Hochschule Heilbronn',
           '109': 'Ruprecht-Karls-Universität Heidelberg',
           '108': 'Hochschule Furtwangen',
           '107': 'Hochschule Fulda',
           '106': 'Friedrich-Schiller-Universität Jena',
           '105': 'Frankfurt University of Applied Sciences',
           '104': 'Fachhochschule Wedel',
           '103': 'Fachhochschule Aachen',
           '102': 'Friedrich-Alexander-Universität Erlangen-Nürnberg',
           '101': 'Technische Universität Dresden',
           '100': 'Technische Hochschule Deggendorf',
           '99': 'Technische Hochschule Deggendorf',
           '98': 'Hochschule Darmstadt',
           '97': 'Hochschule Coburg',
           '96': 'Technische Universität Chemnitz',
           '95': 'Hochschule Bremerhaven',
           '94': 'Brandenburgische Technische Universität Cottbus-Senftenberg',
           '93': 'Bauhaus-Universität Weimar',
           '92': 'Hochschule Ansbach',
           '91': 'Hochschule Anhalt',
           '90': 'Hochschule Aalen'
       }

   def handle(self, *args, **options):
       mappings = self.get_university_mappings()

       with transaction.atomic():
           updated_count = 0
           not_found_count = 0

           for uni_id, new_name in mappings.items():
               try:
                   university = University.objects.get(pk=uni_id)
                   old_name = university.name
                   university.name = new_name
                   university.save()
                   updated_count += 1
                   self.stdout.write(
                       f'Updated ID {uni_id}: {old_name} -> {new_name}'
                   )
               except University.DoesNotExist:
                   not_found_count += 1
                   self.stdout.write(
                       f'University with ID {uni_id} not found'
                   )

           self.stdout.write(
               f'\nCompleted university name updates:'
               f'\nTotal mapped: {len(mappings)}'
               f'\nUpdated: {updated_count}'
               f'\nNot found: {not_found_count}'
           )