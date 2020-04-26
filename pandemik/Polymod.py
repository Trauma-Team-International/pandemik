_url = 'https://raw.githubusercontent.com/mikkokotila/version-controlled-data/master/data/polymod_social_contact_data.csv'

class Polymod:
    
    def __init__(self, data=None):
        
        import pandas as _pd
        
        if data is not None:
            self.data = data
        else:
            self.data = _pd.read_csv(_url)
            True

    def country_data(self, country_code='fi'):

        # get the country columns to drop it before return
        cols = []
        for col in self.data.columns:
            if 'country_' in col:
                cols.append(col)

        return p.data[p.data['country_' + country_code] == 1].drop(cols, 1)

    def _build_population(self,
                           population_size,
                           age_distribution=[15, 65, 20]):
            
        '''Returns a population expressed as a 1d array where
        each record is a member of the population.'''

        import numpy as np
        
        self.population = np.random.choice([1, 2, 3], size=population_size, p=np.array(age_distribution) / 100)

    def _build_contacts(self, data, probabilities=False):

        '''Returns participant level daily contact record 
        in absolute values or probabilities.'''

        temp = data.copy(deep=True)
        temp = temp.groupby('participant_id').sum()

        cols = ['contact_home',
                'contact_work',
                'contact_school',
                'contact_transport',
                'contact_leisure',
                'contact_other']

        temp = temp[cols]

        if probabilities:
            temp['contact_total'] = temp.sum(axis=1)

            for col in cols:
                temp[col] = temp[col] / temp['contact_total']

        return temp.dropna()

    
    def _build_age_groups(self, country_code):
        
        country_data = self.country_data(country_code)

        country_data['0-14'] = country_data.participant_age.between(0, 14).astype(int)
        country_data['15-64'] = country_data.participant_age.between(15, 64).astype(int)
        country_data['65-100'] = country_data.participant_age.between(64, 100).astype(int)
        self.age_young = country_data[country_data.participant_age.between(0, 14)]
        self.age_adult = country_data[country_data.participant_age.between(15, 64)]
        self.age_elderly = country_data[country_data.participant_age.between(64, 100)]
     
    def raw_daily_contacts(self, country_code='fi', probabilities=False):
        
        self._build_age_groups(country_code)
        
        if probabilities:

            young = self._build_contacts(self.age_young, True).values
            adult = self._build_contacts(self.age_adult, True).values
            elderly = self._build_contacts(self.age_elderly, True).values

        else:
            
            young = self._build_contacts(self.age_young).values
            adult = self._build_contacts(self.age_adult).values
            elderly = self._build_contacts(self.age_elderly).values

        return young, adult, elderly
    
    def total_daily_contacts(self,
                             population_size=1000,
                             country_code='fi',
                             multiplier=1,
                             age_distribution=[15, 65, 20]):
        
        import random
        import numpy as np
        
        self._build_age_groups(country_code)
        self._build_population(population_size=population_size, age_distribution=age_distribution)
    
        out = []

        young = (self.population == 1).sum() * multiplier
        adult = (self.population == 2).sum() * multiplier
        elderly = (self.population == 3).sum() * multiplier

        young_picks = self._build_contacts(self.age_young).values
        adult_picks = self._build_contacts(self.age_adult).values
        elderly_picks = self._build_contacts(self.age_elderly).values

        out = random.choices(young_picks.tolist(), k=young)
        out += random.choices(adult_picks.tolist(), k=adult)
        out += random.choices(elderly_picks.tolist(), k=elderly)

        return np.array(out).sum(0)
     
p = Polymod()
