class bioplastic_production:
    def __init__(self, TnMaiz_per_ha:float=3.39, almidon_per_gr_maiz:float=0.057, bioplastic_per_almidon:float=0.8741) -> None:
        """The default values are for the production with the minimum yield and
          efficiency reported in the literature."""
        self.gr_maiz_per_ha = TnMaiz_per_ha * 1000000
        self.gr_almidon_per_ha = self.gr_maiz_per_ha * almidon_per_gr_maiz
        self.Tn_bioplastic_per_ha = (self.gr_almidon_per_ha * bioplastic_per_almidon
                                    /1000000)
        self.Tn_bioplastic = 2.2 * (10**6)
        
  

    def set_bioplastic_population(million_Tn_bioplastic) -> None:
        self.Tn_bioplastic = million_Tn_bioplastic * (10**6)