import urllib.request
import re
import string
import sys
from collections import namedtuple as _namedtuple
from flask import Flask

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

app = Flask(__name__)

@app.route('/<string:name>')
def get_closest(name):
#     resource = urllib.request.urlopen('https://docs.google.com/document/d/e/2PACX-1vSQWXUs-TaSndX5RzkBk1Yyd3OjbFv_YxfNu5GVUNCNSkimZKoD1lXCX0fhrq_EzFphG5gDPIlwbyUA/pub')
#     content =  resource.read().decode(resource.headers.get_content_charset())
#     comp = content.split('&#39;', 1)[1].split('</span>', 1)[0]
    
    return name
    
#     input_data = ' '.join(name.split('-'))
#     # return input_data
 
#     dd = {}
#     for val in brands:
#         dd[val] = token_set_ratio(input_data, val)

#     brand = sorted(dd, key=dd.get, reverse=True)[0]
#     brand_stop = brands[brands.index(brand)-1]

#     dd = {}
#     for val in (brand + ' ' + comp.split(brand, 1)[1]).split(brand_stop)[0].split('|||'):
#         dd[val] = token_set_ratio(input_data, val)

#     return sorted(dd, key=dd.get, reverse=True)[0]


@app.route('/')
def get_home():
#     resource = urllib.request.urlopen('https://docs.google.com/document/d/e/2PACX-1vSQWXUs-TaSndX5RzkBk1Yyd3OjbFv_YxfNu5GVUNCNSkimZKoD1lXCX0fhrq_EzFphG5gDPIlwbyUA/pub')
#     content =  resource.read().decode(resource.headers.get_content_charset())
#     comp = content.split('&#39;', 1)[1].split('</span>', 1)[0]
    
    return 'waiting'


# brands = ['Versace',
# 'Van Cleef & Arpels',
# 'Valentino',
# 'Tom Ford',
# 'Tod\'s',
# 'Tiffany & Co.',
# 'The Row',
# 'Telfar',
# 'Stella McCartney',
# 'Salvatore Ferragamo',
# 'Saint Laurent',
# 'Rolex',
# 'Ralph Lauren Collection',
# 'Proenza Schouler',
# 'Prada',
# 'Off White',
# 'Nancy Gonzalez',
# 'Mulberry',
# 'Miu Miu',
# 'Mark Cross',
# 'Mansur Gavriel',
# 'M2Malletier',
# 'Louis Vuitton',
# 'Loewe',
# 'Lanvin',
# 'Judith Leiber',
# 'Jimmy Choo',
# 'Jacquemus',
# 'Hermes',
# 'Harry Winston',
# 'Gucci',
# 'Goyard',
# 'Givenchy',
# 'Fendi',
# 'Dolce & Gabbana',
# 'Delvaux',
# 'Christian Louboutin',
# 'Christian Dior',
# 'Chloe',
# 'Chanel',
# 'Celine',
# 'Cartier',
# 'Bvlgari',
# 'Burberry',
# 'Bottega Veneta',
# 'Balenciaga',
# 'Alexander Wang',
# 'Alexander McQueen',
# 'Alaia',
# '3.1 Phillip Lim']

# PY3 = sys.version_info[0] == 3
# if PY3:
#     string = str

# def token_set_ratio(s1, s2, force_ascii=True, full_process=True):
#     return _token_set(s1, s2, partial=False, force_ascii=force_ascii, full_process=full_process)


# def _token_set(s1, s2, partial=True, force_ascii=True, full_process=True):
#     if not full_process and s1 == s2:
#         return 100

#     p1 = full_process_func(s1, force_ascii=force_ascii) if full_process else s1
#     p2 = full_process_func(s2, force_ascii=force_ascii) if full_process else s2

#     if not validate_string(p1):
#         return 0
#     if not validate_string(p2):
#         return 0

#     tokens1 = set(p1.split())
#     tokens2 = set(p2.split())

#     intersection = tokens1.intersection(tokens2)
#     diff1to2 = tokens1.difference(tokens2)
#     diff2to1 = tokens2.difference(tokens1)

#     sorted_sect = " ".join(sorted(intersection))
#     sorted_1to2 = " ".join(sorted(diff1to2))
#     sorted_2to1 = " ".join(sorted(diff2to1))

#     combined_1to2 = sorted_sect + " " + sorted_1to2
#     combined_2to1 = sorted_sect + " " + sorted_2to1

#     sorted_sect = sorted_sect.strip()
#     combined_1to2 = combined_1to2.strip()
#     combined_2to1 = combined_2to1.strip()

#     ratio_func = ratio

#     pairwise = [
#         ratio_func(sorted_sect, combined_1to2),
#         ratio_func(sorted_sect, combined_2to1),
#         ratio_func(combined_1to2, combined_2to1)
#     ]
#     return max(pairwise)

# def full_process_func(s, force_ascii=False):
#     if force_ascii:
#         s = asciidammit(s)
#     string_out = StringProcessor.replace_non_letters_non_numbers_with_whitespace(s)
#     string_out = StringProcessor.to_lower_case(string_out)
#     string_out = StringProcessor.strip(string_out)
#     return string_out

# class StringProcessor(object):
#     regex = re.compile(r"(?ui)\W")

#     @classmethod
#     def replace_non_letters_non_numbers_with_whitespace(cls, a_string):
#         return cls.regex.sub(" ", a_string)

#     strip = staticmethod(string.strip)
#     to_lower_case = staticmethod(string.lower)
#     to_upper_case = staticmethod(string.upper)


# def asciidammit(s):
#     if type(s) is str:
#         return asciionly(s)
#     elif type(s) is unicode:
#         return asciionly(s.encode('ascii', 'ignore'))
#     else:
#         return asciidammit(unicode(s))

# def asciionly(s):
#     if PY3:
#         return s.translate(translation_table)
#     else:
#         return s.translate(None, bad_chars)

# PY3 = sys.version_info[0] == 3

# bad_chars = str("").join([chr(i) for i in range(128, 256)])  # ascii dammit!
# if PY3:
#     translation_table = dict((ord(c), None) for c in bad_chars)
#     unicode = str

# def validate_string(s):
#     try:
#         return len(s) > 0
#     except TypeError:
#         return False

# def intr(n):
#     return int(round(n))

# def ratio(s1, s2):
#     s1, s2 = make_type_consistent(s1, s2)

#     m = SequenceMatcher(None, s1, s2)
#     return intr(100 * m.ratio())


# def make_type_consistent(s1, s2):
#     if isinstance(s1, str) and isinstance(s2, str):
#         return s1, s2

#     elif isinstance(s1, unicode) and isinstance(s2, unicode):
#         return s1, s2

#     else:
#         return unicode(s1), unicode(s2)





# class SequenceMatcher:
#     def __init__(self, isjunk=None, a='', b='', autojunk=True):
#         self.isjunk = isjunk
#         self.a = self.b = None
#         self.autojunk = autojunk
#         self.set_seqs(a, b)

#     def set_seqs(self, a, b):
#         self.set_seq1(a)
#         self.set_seq2(b)

#     def set_seq1(self, a):
#         if a is self.a:
#             return
#         self.a = a
#         self.matching_blocks = self.opcodes = None

#     def set_seq2(self, b):
#         if b is self.b:
#             return
#         self.b = b
#         self.matching_blocks = self.opcodes = None
#         self.fullbcount = None
#         self.__chain_b()


#     def __chain_b(self):
#         b = self.b
#         self.b2j = b2j = {}

#         for i, elt in enumerate(b):
#             indices = b2j.setdefault(elt, [])
#             indices.append(i)
#         self.bjunk = junk = set()
#         isjunk = self.isjunk
#         if isjunk:
#             for elt in b2j.keys():
#                 if isjunk(elt):
#                     junk.add(elt)
#             for elt in junk: 
#                 del b2j[elt]

#         self.bpopular = popular = set()
#         n = len(b)
#         if self.autojunk and n >= 200:
#             ntest = n // 100 + 1
#             for elt, idxs in b2j.items():
#                 if len(idxs) > ntest:
#                     popular.add(elt)
#             for elt in popular:
#                 del b2j[elt]

#     def ratio(self):
#         matches = sum(triple[-1] for triple in self.get_matching_blocks())
#         return _calculate_ratio(matches, len(self.a) + len(self.b))


#     def get_matching_blocks(self):
#         if self.matching_blocks is not None:
#             return self.matching_blocks
#         la, lb = len(self.a), len(self.b)
#         queue = [(0, la, 0, lb)]
#         matching_blocks = []
#         while queue:
#             alo, ahi, blo, bhi = queue.pop()
#             i, j, k = x = self.find_longest_match(alo, ahi, blo, bhi)
#             if k:
#                 matching_blocks.append(x)
#                 if alo < i and blo < j:
#                     queue.append((alo, i, blo, j))
#                 if i+k < ahi and j+k < bhi:
#                     queue.append((i+k, ahi, j+k, bhi))
#         matching_blocks.sort()

#         i1 = j1 = k1 = 0
#         non_adjacent = []
#         for i2, j2, k2 in matching_blocks:
#             if i1 + k1 == i2 and j1 + k1 == j2:
#                 k1 += k2
#             else:
#                 if k1:
#                     non_adjacent.append((i1, j1, k1))
#                 i1, j1, k1 = i2, j2, k2
#         if k1:
#             non_adjacent.append((i1, j1, k1))

#         non_adjacent.append( (la, lb, 0) )
#         self.matching_blocks = list(map(Match._make, non_adjacent))
#         return self.matching_blocks

#     def find_longest_match(self, alo=0, ahi=None, blo=0, bhi=None):
#         a, b, b2j, isbjunk = self.a, self.b, self.b2j, self.bjunk.__contains__
#         if ahi is None:
#             ahi = len(a)
#         if bhi is None:
#             bhi = len(b)
#         besti, bestj, bestsize = alo, blo, 0
#         j2len = {}
#         nothing = []
#         for i in range(alo, ahi):
#             j2lenget = j2len.get
#             newj2len = {}
#             for j in b2j.get(a[i], nothing):
#                 if j < blo:
#                     continue
#                 if j >= bhi:
#                     break
#                 k = newj2len[j] = j2lenget(j-1, 0) + 1
#                 if k > bestsize:
#                     besti, bestj, bestsize = i-k+1, j-k+1, k
#             j2len = newj2len
#         while besti > alo and bestj > blo and \
#               not isbjunk(b[bestj-1]) and \
#               a[besti-1] == b[bestj-1]:
#             besti, bestj, bestsize = besti-1, bestj-1, bestsize+1
#         while besti+bestsize < ahi and bestj+bestsize < bhi and \
#               not isbjunk(b[bestj+bestsize]) and \
#               a[besti+bestsize] == b[bestj+bestsize]:
#             bestsize += 1
#         while besti > alo and bestj > blo and \
#               isbjunk(b[bestj-1]) and \
#               a[besti-1] == b[bestj-1]:
#             besti, bestj, bestsize = besti-1, bestj-1, bestsize+1
#         while besti+bestsize < ahi and bestj+bestsize < bhi and \
#               isbjunk(b[bestj+bestsize]) and \
#               a[besti+bestsize] == b[bestj+bestsize]:
#             bestsize = bestsize + 1

#         return Match(besti, bestj, bestsize)

# def _calculate_ratio(matches, length):
#     if length:
#         return 2.0 * matches / length
#     return 1.0

# Match = _namedtuple('Match', 'a b size')


app.run(port=5001)

# with open(input_file, 'r') as file:
#     text = file.read()

# comp = text.replace('\'\\\n}', '').replace('{\\rtf1\\ansi\\ansicpg1252\\cocoartf2636\n\\cocoatextscaling0\\cocoaplatform0{\\fonttbl\\f0\\fswiss\\fcharset0 Helvetica;}\n{\\colortbl;\\red255\\green255\\blue255;}\n{\\*\\expandedcolortbl;;}\n\\paperw11900\\paperh16840\\margl1440\\margr1440\\vieww34360\\viewh19280\\viewkind0\n\\pard\\tx566\\tx1133\\tx1700\\tx2267\\tx2834\\tx3401\\tx3968\\tx4535\\tx5102\\tx5669\\tx6236\\tx6803\\pardirnatural\\partightenfactor0\n\n\\f0\\fs24 \\cf0 ', '').split('|||')






# import urllib  # the lib that handles the url stuff
# result = []

# data = urllib.request.urlopen('https://docs.google.com/document/d/e/2PACX-1vSQWXUs-TaSndX5RzkBk1Yyd3OjbFv_YxfNu5GVUNCNSkimZKoD1lXCX0fhrq_EzFphG5gDPIlwbyUA/pub')
# for line in data:            # file lines are iterable
#     result.append(line)      # keep each line, or parse, etc.



