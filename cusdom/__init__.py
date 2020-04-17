# -*- coding: utf-8 -*-
#
# Fichier nécessaire pour que  cusdom  soit un package :
# D’après la réponse de *Loki* au topic
# What is __init__.py for?
# https://stackoverflow.com/questions/448271
# il y a deux types de packages :
# 1. Les « regular package » qui sont les package traditionnel c’était
#    le seul type de package 3.2−.
#    Un regular-package est typiquement un répertoire contenant un __init__.py
#    Quand un regular-package est importé, le  __init__.py
#    est implicitement exécuté, et les objets qui y sont définis
#    sont ajoutés du « package namespace ».
#    Le fichier  __init__.py  peut contenir n’importe quel code Python.
# 2. Les « namespace package » (3.3+) n’ont pas besoin d’un  __init__.py
