# -*- coding: utf-8 -*-
"""
Script principal du package  cusdom  pour CUStom ranDOM

Soient des nombre aléatoires  X ~ U(0, 1).
Soit une distribution quelconque  f : R → [0, 1] : x ↦ f(x)
dont la fonction de répartition est  F : R → [0, 1] : x ↦ F(x), telle que
- F′(x) = f(x)
- F(x → −∞) → 0
- F(x → +∞) → 1
- F continue à droite
ces critère font de  F  une bijection de  R  dans  [0, 1]
donc  F  possède une inverse  F⁻¹  (mais pas formément sous forme close).
Alors, les nombres aléatoire  Y = F⁻¹(X)  auront pour densité de
probabilité la fonction  f  .
C’est la méthode de la transformée inverse :
    https://fr.wikipedia.org/wiki/M%C3%A9thode_de_la_transform%C3%A9e_inverse
Mais on ne peut pas l’utiliser ici car on ne connait que  f  (donc
on ne connait pas  F  et encore moins  F⁻¹ !), on utlisera 
la méthode de rejet
https://fr.wikipedia.org/wiki/M%C3%A9thode_de_rejet
---
2020-04-17@12:46:38, Création :
    lava@macta
    /Users/lava/zessais/git/3.5_Branches_distantes/A-team/cusdom/cusdom.py
"""

# def cusdom(disfun, size=1):
#     """
#     Calcul de  size  nombre aléatoire ayant  disfun
#     comme densité de probabilité (fonction de distribution).
#     Cette fonction utilise la méthode de rejet
#     ---
#     @disfun: (str) fonction de distribution, p-ex "(1+x**2)**-1"
#     @size: (int) nombre de nombres aléatoires à générer
#     """
#
#     from random import random
#
#     # Paire de VA uniforme dans [0, 1]
#     U, V = random(), random()
#
#     # Fonction de distribution
#     # /!\ Il faudra ajouter un  try  au cas où disfun est mauvaise
#     f = lambda x: eval(disfun)
#
#     # Méthode de rejet
#     while True:
#         if U <= f(V):
#             return U

def cusdom(distribution='uniforme', size=1):
    """
    Calcul de  size  nombres aléatoire ayant  distribution  come
    densité de probabilité.
    Cette fonction implémente la méthode de la transformée inverse
    pour les distributions suivantes :
    - loi exponentielle
        f(x) = 
        F(x) = 
        F⁻¹(y) = − ln(1 - y) / λ
    - loi de Cauchy
        f(x) = 
        F(x) = 
        F⁻¹(y) = tan(π y)
    - loi logistique
        f(x) = 
        F(x) = 
        F⁻¹(y) = − ln(y / (1 − y))
    - loi de Laplace
        f(x) = 
        F(x) = 
        F⁻¹(y) = − sgn(y) ln(1 − 2|y|)
    et la méthode de Box--Muller pour la loi normale :
    ---
    distribution (str): exponentielle, cauchy, logistique, laplace, normale
    size (int):
    return (list(float)): nombres aléatoires suivant  distribution
    """
    # TODO: utiliser re pour que, pex, exp convienne pour exponentielle
    from random import random
    from math import log as ln
    from math import tan, pi, sqrt, cos

    sign = lambda x: int(2.*float(x >= 0) - 1.)

    u = random()

    if distribution == 'exponentielle':
        lmbd = 1.
        return - ln(1 - u) / lmbd
    elif distribution == 'cauchy':
        return tan(pi * u)
    elif distribution == 'logistique':
        return - ln(u / (1. - u))
    elif distribution == 'laplace':
        return - sign(u) * ln(1. - 2.*abs(u))
    elif distribution == 'normale':
        v = random()
        return sqrt(-2.*ln(u)) * cos(2.*pi*v)
    else:
        raise Exception()

