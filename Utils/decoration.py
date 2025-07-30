#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Not Delete, Copyright and MIT License, BY Thomas R. © 2025.

""" Sub script-modulo que irá usar as cores nas perguntas e respostas """

from colored import fg, attr

class Theme:
    """ Cores básicas """
    vermelho = fg('red')
    verde = fg('green')
    amarelo = fg('yellow')
    azul = fg('blue')
    magenta = fg('magenta')
    ciano = fg('cyan')
    
    """ Cores especiais """
    atencao = fg(208)  # Laranja
    
    """ Estilos """
    branco_negrito = f"{fg('white')}{attr('bold')}"
    
    """ Controle """
    reset = attr('reset')

color = Theme()
