class Casier:
    """
     Classe casier

    """

    ###################################
    #####  MÉTHODE CONSTRUCTEUR  #####
    ###################################


    def __init__(self,p_num_casier="",p_grandeur="",p_bloc="",p_prix=20):
        """
                Méthode de type Constructeur avec paramètres et valeurs par défaut
                Définition des attributs publics d'un étudiant
        """
        self.__num_casier = p_num_casier
        self.grandeur = p_grandeur
        self.bloc = p_bloc
        self.__prix = p_prix

        ##################################################
        ####   Propriétés, accesseurs et mutateurs    ####
        ####                                          ####
        ##################################################

        # Propriété numéro casier
    def _get_num_casier(self):
            """
               Accesseur de l'attribut privé  __num__casier
            """
            return self.__num_casier

    def _set_num_casier(self, p_num_casier):
            """
            Mutateur de l'attribur privé __num_casier
            """
            chaine_casier = p_num_casier
            if chaine_casier[0].isalpha and chaine_casier[1:5].isnumeric() is True:
                self.__num_etud = p_num_casier

    Num_casier = property(_get_num_casier, _set_num_casier)

      # Propriété prix
    def _get_prix(self,v):
            """
               Accesseur de l'attribut privé  __num__casier
            """
            self.__prix = v
    PrixCasier = property(_get_prix)