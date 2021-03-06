# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#    xierpa server
#    Copyright (c) 2014+  buro@petr.com, www.petr.com, www.xierpa.com
#
#    X I E R P A  3
#    Distribution by the MIT License.
#
# -----------------------------------------------------------------------------
#
#    Contributed by Erik van Blokland and Jonathan Hoefler
#    Original from filibuster.
#
# FILIBUSTER.ORG!

"""
        living
--------------------------------------------------------------------
"""

__version__ = '3.0.0'
__author__ = "someone"

content = {
    'creditcard': [
        '<#p_cc_flavor#><#p_cc_sx#>',
        '<#p_cc_flavor#><#p_cc_flavor#><#p_cc_sx#>',
        '<#p_cc_quality#> <#p_cc_flavor#><#p_cc_sx#>',
        '<#p_cc_quality#> <#p_cc_flavor#><#p_cc_sx#>',
    ],
    'creditcard_accepted': [
        '<#company#> welcomes <#creditcard#>',
        '<#company#> prefers <#creditcard#>',
        'We welcome <#creditcard#>',
        'We prefer <#creditcard#>',
        '<#creditcard#> preferred!',
        '<#creditcard#> accepted.',
        'Pay with <#creditcard#>',
    ],
    'creditcard_issued': [
        '<#p_cc_issuer#> <#creditcard#>',
        u'<#p_cc_issuer#>’s <#creditcard#>',
        '<#creditcard#>, by <#p_cc_issuer#>',
    ],
    'creditcard_number': [
        '<#figs#><#figs#><#figs#><#figs#> <#figs#><#figs#><#figs#><#figs#> <#figs#><#figs#><#figs#><#figs#> <#figs#><#figs#><#figs#><#figs#>',
    ],
    'creditcard_validuntil': [
        '<#time_months#> <#time_comingyears#>',
    ],
    'p_acronym': [
        '<#alphabet_caps#><#alphabet_caps#>',
        '<#alphabet_caps#><#alphabet_caps#><#alphabet_caps#>',
    ],
    'p_cc_flavor': [
        '<#p_cc_flavor_common#>',
        '<#p_cc_flavor_nonsense#>',
        '<#name_japanese#>',
        '<#p_cc_flavor_religious#>',
        '<#p_cc_flavor_super#>',
        '<#p_cc_flavor_count#>',
        '<#p_cc_flavor_sweet#>',
        '<#p_cc_flavor_shop#>',
        '<#p_cc_flavor_money#>',
        '<#p_cc_flavor_modern#>',
        '<#p_cc_flavor_currency#>',
        '<#p_cc_flavor_locale#>',
        '<#p_cc_flavor_odd#>',
        '<#p_cc_flavor_others#>',
    ],
    'p_cc_flavor_common': [
        'Direct',
        'Media',
        'Uni',
        'Family',
        'Member',
        'Diner',
    ],
    'p_cc_flavor_count': [
        'Twin',
        'Bi',
        'Duo',
        'Tri',
        'Trio',
        'Quatro',
        'Penta',
    ],
    'p_cc_flavor_currency': [
        'Dime',
        '<#sci_transition_metals#>Dollar',
        'Dollar',
        'Sterling',
        'Change',
    ],
    'p_cc_flavor_locale': [
        'Euro',
        'Asia',
        'US',
        'HK',
    ],
    'p_cc_flavor_modern': [
        'Com',
        'Phone',
        'Smart',
        'Swipe',
        'Compu',
        'Terminal',
        'Electro',
        'Plasti',
        'Chem',
        'Chemi',
        'Chemo',
        'Net',
        'Web',
        'SET',
        'Inter',
    ],
    'p_cc_flavor_money': [
        'Buy',
        'Cash',
        'Kash',
        'Money',
        'Pecunia',
        'Debet',
        'Debt',
        'Specu',
        'Pin',
        'Chipper',
    ],
    'p_cc_flavor_nonsense': [
        'Exi',
        'Minto',
        'Exo',
        'Mondo',
        'Fina',
    ],
    'p_cc_flavor_odd': [
        'Gas',
        'Petro',
        'Petroli',
    ],
    'p_cc_flavor_others': [
        '<#p_acronym#>',
        '<#p_co_creative#>',
        '<#p_co_mediaprefix#>',
        '<#p_business_name#>',
        '<#p_cc_quality#>',
    ],
    'p_cc_flavor_religious': [
        'Pure',
        'Reli',
        'Holy',
        'Spiri',
        'God',
        'Noble',
    ],
    'p_cc_flavor_shop': [
        'Excel',
        'Access',
        'XS',
        'Fast',
        'Digi',
        'E',
        'Shop',
        'Store',
        'Market',
    ],
    'p_cc_flavor_super': [
        'Super',
        'Hyper',
        'Ultra',
        'Kid',
        'Major',
        'Minor',
    ],
    'p_cc_flavor_sweet': [
        'Courtesy',
        'Polite',
        'Nice',
        'Comfort',
        'Friendly',
        'Friendli',
    ],
    'p_cc_issuer': [
        '<#company#>',
        '<#eurobank#>',
        '<#usbank#>',
        '<#name_japanese#>',
    ],
    'p_cc_quality': [
        'Personal',
        'Home',
        'Business',
        'Corporate',
        '<#sci_popularelements#>',
        '<#sci_popularelements#>',
        '<#sci_popularelements#>',
        '<#sci_popularelements#>',
    ],
    'p_cc_sx': [
        'Card',
        'Card',
        'Card',
        'Card',
        'Credit',
        'Express',
    ],
    }

