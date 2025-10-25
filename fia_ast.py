# fia_ast.py

from abc import ABC, abstractmethod

class Noeud(ABC):
    """Classe de base abstraite pour tous les noeuds de l'AST."""
    @abstractmethod
    def accepter(self, visiteur):
        pass

class Programme(Noeud):
    def __init__(self, instructions):
        self.instructions = instructions # Liste de Noeuds

    def accepter(self, visiteur):
        return visiteur.visiter_programme(self)

class DeclarationVariable(Noeud):
    def __init__(self, nom, valeur=None):
        self.nom = nom
        self.valeur = valeur # Noeud expression

    def accepter(self, visiteur):
        return visiteur.visiter_declaration_variable(self)

class Assignation(Noeud):
    def __init__(self, cible, valeur):
        self.cible = cible # Noeud (Variable ou IndexAccess)
        self.valeur = valeur # Noeud expression

    def accepter(self, visiteur):
        return visiteur.visiter_assignation(self)

# NOUVELLE CLASSE POUR LES ASSIGNATIONS COMPOSÉES
class AssignationComposee(Noeud):
    def __init__(self, cible, operateur, valeur):
        self.cible = cible # Noeud (Variable ou IndexAccess)
        self.operateur = operateur # str (+=, -=, *=, /=, %=)
        self.valeur = valeur # Noeud expression

    def accepter(self, visiteur):
        return visiteur.visiter_assignation_composee(self)

class ExpressionBinaire(Noeud):
    def __init__(self, gauche, operateur, droite):
        self.gauche = gauche # Noeud expression
        self.operateur = operateur # str
        self.droite = droite # Noeud expression

    def accepter(self, visiteur):
        return visiteur.visiter_expression_binaire(self)

class ExpressionUnaire(Noeud):
    def __init__(self, operateur, operande):
        self.operateur = operateur
        self.operande = operande

    def accepter(self, visiteur):
        return visiteur.visiter_expression_unaire(self)

class Littéral(Noeud):
    def __init__(self, valeur):
        self.valeur = valeur # valeur brute (int, float, str, bool, list, None)

    def accepter(self, visiteur):
        return visiteur.visiter_litteral(self)

class Identifiant(Noeud):
    def __init__(self, nom):
        self.nom = nom

    def accepter(self, visiteur):
        return visiteur.visiter_identifiant(self)

class AppelFonction(Noeud):
    def __init__(self, nom_fonction, arguments):
        self.nom_fonction = nom_fonction # str
        self.arguments = arguments # Liste de Noeuds expressions

    def accepter(self, visiteur):
        return visiteur.visiter_appel_fonction(self)

class Condition(Noeud):
    def __init__(self, condition, bloc_si, bloc_sinon=None):
        self.condition = condition # Noeud expression
        self.bloc_si = bloc_si # Liste de Noeuds
        self.bloc_sinon = bloc_sinon # Liste de Noeuds optionnel

    def accepter(self, visiteur):
        return visiteur.visiter_condition(self)

class BoucleTantQue(Noeud):
    def __init__(self, condition, corps):
        self.condition = condition # Noeud expression
        self.corps = corps # Liste de Noeuds

    def accepter(self, visiteur):
        return visiteur.visiter_boucle_tant_que(self)

class BouclePour(Noeud):
    def __init__(self, init, condition, increment, corps):
        self.init = init # Noeud instruction
        self.condition = condition # Noeud expression
        self.increment = increment # Noeud instruction
        self.corps = corps # Liste de Noeuds

    def accepter(self, visiteur):
        return visiteur.visiter_boucle_pour(self)

# NOUVELLE CLASSE POUR LA BOUCLE POUR...DANS
class BouclePourDans(Noeud):
    def __init__(self, variable, iterable, corps):
        self.variable = variable # str (nom de la variable de boucle)
        self.iterable = iterable # Noeud expression (liste, dictionnaire, chaîne)
        self.corps = corps # Bloc

    def accepter(self, visiteur):
        return visiteur.visiter_boucle_pour_dans(self)

class Bloc(Noeud):
    def __init__(self, instructions):
        self.instructions = instructions # Liste de Noeuds

    def accepter(self, visiteur):
        return visiteur.visiter_bloc(self)

class Fonction(Noeud):
    def __init__(self, nom, parametres, corps):
        self.nom = nom # str
        self.parametres = parametres # Liste de str (noms des paramètres)
        self.corps = corps # Liste de Noeuds

    def accepter(self, visiteur):
        return visiteur.visiter_fonction(self)

class Retour(Noeud):
    def __init__(self, valeur=None):
        self.valeur = valeur # Noeud expression optionnel

    def accepter(self, visiteur):
        return visiteur.visiter_retour(self)

class AccesIndex(Noeud):
    def __init__(self, base, index):
        self.base = base # Noeud expression (la liste)
        self.index = index # Noeud expression (l'index)

    def accepter(self, visiteur):
        return visiteur.visiter_acces_index(self)

class AccesDictionnaire(Noeud):
    def __init__(self, base, cle):
        self.base = base # Noeud expression (le dictionnaire)
        self.cle = cle # Noeud expression (la clé)

    def accepter(self, visiteur):
        return visiteur.visiter_acces_dictionnaire(self)

class ExpressionStatement(Noeud):
    def __init__(self, expression):
        self.expression = expression

    def accepter(self, visiteur):
        return visiteur.visiter_expression_statement(self)

# Ajouter d'autres noeuds si nécessaire
