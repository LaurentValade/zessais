# -*- coding: utf-8 -*-
"""
Test unitaire avec pytest de la fonction cusdom

Exemples :
    https://docs.pytest.org/en/latest/example/index.html
---
2020-04-17@18:48:35, Création :
    lava@macta
    /Users/lava/zessais/git/3.5_Branches_distantes/B-team/tests/test_cusdom.py
"""

from cusdom import cusdom
cusdom = cusdom.cusdom
# ^ Il y a 3 cusdom : dossier / script / fonction :
#   cusdom/cusdom.py::cusdom

def test_cusdom():
    for distribution in [
            'uniforme', 'exponentielle', 'logistique', 'laplace', 'normale']:
        assert type(cusdom(distribution)) is float

