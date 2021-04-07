from bson.objectid import ObjectId
from connection import Connection
from competitors import *
from customerReviews import *
import pandas as pd


class CompetitorsAdding:
    def __init__(self, df):
        self.df = df

    def competitor_iteration(self):
        for index, row in self.df.iterrows():
            competitor = Competitor()
            competitor.competitor_name = row['Company']
            competitor.url = row['Url1']
            competitor.org_vals = OrgValues(place=row['Country'], shares=row['Public/private'], cb_rank=row['CB'])
            competitor.product = Product(
                first_product=FirstProduct(energy=row['Energy_p'], wavelength=row['Wavelength_p']),
                second_product=SecondProduct(energy=row['Energy_f'], wavelength=row['Wavelength_f']),
                third_product=ThirdProduct(avg_delivery=row['Shipment'], avg_price=row['Price'],
                                           technical=ThirdProductTech(energy=row['Energy'],
                                                                      wavelength=row['Wavelength'])))
            competitor.technology = Technology(sphere=row['Total_medicine'],
                                               tech=row['Total_x'] + row['Total_y'],
                                               conference_presence=row['Spie_company'])

            competitor.save()


if __name__ == '__main__':
    # Connecting to database collection
    conn = Connection()
    db_cursor = conn.connect()
    collection = db_cursor['Competitors']

    # Adding data
    df = pd.read_excel(r'C:\Users\maxim\OneDrive\Desktop\folder\diplom\data\parsing\final_companies.xlsx')
    obj = CompetitorsAdding(df)
    obj.competitor_iteration()
    print('Competitors added!')