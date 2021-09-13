from mendeley import Mendeley
import yaml
import os
import csv


config = {}


config['clientSecret'] = 'idravljCIiczdX8y'

mendeley = Mendeley(config['clientId'], config['clientSecret'])

session = mendeley.start_client_credentials_flow().authenticate()




with open('bangladesh 2016-2020 16501-17000.csv', encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)

    doi = []

    for row in reader:
        doi.append(row["DOI"])
        doi="".join(doi).split()
        print(doi)

        j = 0
        mysrting = " "
        i = 0

        for x in doi:
         

                    v = str(j)+".txt"
                    with open(v, mode='w') as file:
                        doc = session.catalog.by_identifier(
                            doi=x, view='stats')
                        print(session.catalog)
                 

                  =

                        print('"%s" has %s readers.' %
                              (doc.title,  doc.reader_count))

                        file.write(doc.title)
                        file.write(",READERS:  ")
                        file.write(str(doc.reader_count))
                        file.write('\n')
                        file.write(str(doc.reader_count_by_academic_status))
                        file.write('\n')
                        file.write(str(doc.reader_count_by_country))
                        file.write('\n')
                        file.write(str(doc.reader_count_by_subdiscipline))
                        file.write('\n')
                        j = j+1
            

            
