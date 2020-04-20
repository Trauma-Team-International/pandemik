class HofstedePlus:
    
    def __init__(self):
        
        '''Compute Hofsted+ score based on weights and inputs. Use
        this to initialize the object, which then gives you access
        to the features for computing score, changing the weights, and
        applying a randomness effect.
        
        '''
        
        # set 0 random effect as a default
        self.random_effect = 1
        
        # set the default values
        self.set_weights()

    def _get_values_from_dict(self, dictionary):
        
        '''Helper function for reading the input parameters
        on to an array.'''

        out = []
        for key in dictionary.keys():
            if key != 'self':
                out.append(dictionary[key])

        return out
    
    def set_randomness(self, distribution='normal', factor=.01):
        
        '''Set randomness effect to the score computation.
        
        distribution | str | 'normal', 'uniform', or 'gamma' distribution for the pick
        
        '''

        import numpy as np
        
        if distribution == 'normal':
            out = np.random.normal(1, factor)

        elif distribution == 'uniform':
            out = np.random.uniform(low=1-factor, high=1+factor)

        elif distribution == 'gamma':
            out = 1 + np.random.gamma(1, scale=factor)
            
        self.random_effect = out

    def set_weights(self,
                    weight_uncertainty_avoidance=1,
                    weight_long_term_orientation=1,
                    weight_power_distance=.25,
                    weight_individualism=.25,
                    weight_masculinity=.1,
                    weight_indulgence=.1,
                    weight_social_leakage=.1,
                    weight_individual_space=.1,
                    weight_ageing_society=.1,
                    weight_health_seeking_behavior=.1):
        
        '''Set and modify the weights used for computing the score.'''
        
        self.weights = self._get_values_from_dict(locals())
        self.weights = self.weights * self.random_effect


    def get_score(self,
                  uncertainty_avoidance=.85,
                  long_term_orientation=1,
                  power_distance=.6,
                  individualism=.18,
                  masculinity=.39,
                  indulgence=.29,
                  social_leakage=.8,
                  individual_space=.65,
                  ageing_society=.9,
                  health_seeking_behavior=.85):
        
        '''Compute the score based on input values.'''

        values = self._get_values_from_dict(locals())
        
        import numpy as np
        
        values = np.array(values) * self.random_effect
        out = np.dot(values, self.weights) / sum(self.weights)
        out = round(out, 2)

        return out
