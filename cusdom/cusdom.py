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
---
2020-04-17@12:46:38, Création :
    lava@macta
    /Users/lava/zessais/git/3.5_Branches_distantes/A-team/cusdom/cusdom.py
"""

