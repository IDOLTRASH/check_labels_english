import glob
import os
phones = ['aa', 'ae', 'ah', 'ao', 'ax', 'eh', 'er', 'ih', 'iy', 'uh', 'uw', 'aw', 'ay', 'a', 'ey', 'e', 'ow', 'o', 'oy', 'en', 'em', 'el', 'eng', 'ix', 'p', 'b', 't', 'd', 'k', 'g', 's', 'z', 'ch', 'jh', 'sh', 'zh', 'f', 'v', 'hh', 'th', 'dh', 'n', 'm', 'ng', 'w', 'y', 'r', 'l', 'q', 'dx', 'exh', 'axh', 'ct', 'cl', 'vf', 'pau', 'br']

for file in glob.glob('*.lab'):
    with open(file) as f:
        i = f.readline()
        line_count = 1
        while i:
            p = i.strip().split()
            i = f.readline()
            if p[-1] not in phones:
                print(f'In {file}: {p[-1]} is not in the list. At line {line_count}')

            if int(p[0]) == int(p[1]):
                print(f'In {file}: {p[-1]} has the same start and end. At line {line_count}')
            line_count += 1

os.system('pause')
