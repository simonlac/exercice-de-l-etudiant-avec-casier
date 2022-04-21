class Cours:
    """
    classe cours

    """

    ###################################
    #####  MÉTHODE CONSTRUCTEUR  #####
    ###################################

    def __init__(self, p_sigle_cours="", p_titre_cours="", p_nb_heure="",):
        """
                Méthode de type Constructeur avec paramètres et valeurs par défaut
                Définition des attributs publics d'un étudiant
        """
        self.__sigle_cours = p_sigle_cours
        self.__titre_cours= p_titre_cours
        self.__nb_heure = p_nb_heure
    ##################################################
    ####   Propriétés, accesseurs et mutateurs    ####
    ###                                          ####
    ##################################################

    # Propriété numéro casier
    def _get_sigle_cours(self):
            """
               Accesseur de l'attribut privé  __num__casier
            """
            return self.__sigle_cours

    def _set_sigle_cours(self, p_sigle_cours):
            """
            Mutateur de l'attribur privé __num_casier
            """
            chaine_casier = p_sigle_cours
            if chaine_casier[0].isalpha and chaine_casier[1:5].isnumeric() is True:
                self.__num_etud = p_sigle_cours

    sigle_du_cours = property(_get_sigle_cours, _set_sigle_cours)

    # Propriété NomEtud
    def _get_titre(self):
        """
           Accesseur de l'attribut privé  __num__etud
        """
        return self.__titre_cours

    def _set_titre(self, p_titre_cours):
        """
        Mutateur de l'attribur privé __num_etud
        """
        if p_titre_cours.isalpha():
            self.__titre_cours = p_titre_cours
        elif p_titre_cours < 60:
            self.__titre_cours = p_titre_cours

    Titre_du_cours = property(_get_titre, _set_titre)
