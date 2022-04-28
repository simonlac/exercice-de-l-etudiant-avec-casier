class Local:
    def __init__(self,p_type_local = "",p_nb_local = "", p_lieu_local = "A" or "B" or "C",p_dimension_local = 0,p_nbr_places = 0):
        self.__type = p_type_local
        self.__nb_local = p_nb_local
        self.__lieu_local = p_lieu_local
        self.__dimensions_local = p_dimension_local
        self.__nbr_places = p_nbr_places

    def _get_type_local(self):
        """
           Accesseur de l'attribut privé  _type local
        """
        return self.__type

    def _set_type_local(self, p_type_local):
        """
        Mutateur de l'attribur privé __num_casier
        """

        if p_type_local == "Technique" or p_type_local == "Normal":
            print()
    type_local = property(_get_type_local,_set_type_local)

    def _get_nb_local(self):
            """
               Accesseur de l'attribut privé  __nb_local
            """
            return self.__nb_local

    def _set_nb_local(self, p_nb_local):
            """
            Mutateur de l'attribur privé nb_local
            """
            chaine_nb = p_nb_local
            if chaine_nb[0].isalpha and chaine_nb[1] == "-" and chaine_nb[2:5].isnumeric() is True:
                self.__nb_local = p_nb_local
    nb_local = property(_get_nb_local,_set_nb_local)