def phase_invert(phase):
         dic ={' ':' ',  'A':'E',  'E':'I',  'I':'O',  'O':'U',  'U':'A',  'a':'e',  'e':'i', 'i':'o', 'o':'u', 'u':'a',  'B': 'C',  'C': 'D',  'D': 'F',  'F': 'G',  'G': 'H',  'H': 'J',  'J': 'K', 'K': 'L', 'L': 'M', 'M': 'N',  'N': 'P', 'P': 'Q',  'Q': 'R',  'R': 'S',  'S': 'T',  'T': 'V',  'V': 'W',  'W': 'X',  'X': 'Y',  'Y': 'Z',  'Z': 'B',  'b': 'c ',  'c': 'd',  'd': 'f',  'f': 'g',  'g': 'h',  'h': 'j',  'j': 'k',  'k': 'l',  'l': 'm',  'm': 'n',  'n': 'p',  'p': 'q',  'q': 'r',  'r': 's ',  's': 't',  't': 'v',  'v': 'w',  'w': 'x',  'x': 'y',  'y': 'z',  'z': 'b'}
         str_invert = ''
         for ch in phase:
                  str_invert = str_invert + dic[ch]
         return str_invert
print('Frase codificada: ', phase_invert(input('Frase a ser codificada: ')))
