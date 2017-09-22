line1 = eval(input('geef je leeftijd:'))
line2 = input('heb je een nederlands paspoort:')
if line1 >=18 and 'ja' in line2:
    print('gefeliciteerd u mag stemmen')
if  line1 <=18 and 'nee' in line2:
    print('no brur vaka jij mag niet stemmen')
if line1 >=18 and 'ja' in line2:
    print('no brur jij mag niet stemmen')

