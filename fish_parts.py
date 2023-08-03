# FISHES ARE STORED HERE

#! DEFAULT FISH:
#* |\_/---\ 
#* | _    ^>
#* |/ \---/

DEFAULT_TAIL = \
[
	'|\\',
	'| ',
	'|/',
]

DEFAULT_LOWER_BODY = \
[
	'_/-',
	'_  ',
    ' \\-',
]

DEFAULT_UPPER_BODY = \
[
	'--',
	'  ',
	'--',
]

DEFAULT_HEAD = \
[
	'\\ ',
	'^>',
	'/ ',
]

#! SMOL FISH:
#* ><>

SMOL_TAIL = \
[
	'>'
]

SMOL_LOWER_BODY = \
[
	'<',
]

SMOL_UPPER_BODY = \
[
	'',
]

SMOL_HEAD = \
[
	'>'
]

TAILS = [v for k, v in locals().items() if 'TAIL' in k]
L_BODIES = [v for k, v in locals().items() if 'LOWER_BODY' in k]
U_BODIES = [v for k, v in locals().items() if 'UPPER_BODY' in k]
HEADS = [v for k, v in locals().items() if 'HEAD' in k]


if __name__ == '__main__':
    print(TAILS)
    print(L_BODIES)
    print(U_BODIES)
    print(HEADS)