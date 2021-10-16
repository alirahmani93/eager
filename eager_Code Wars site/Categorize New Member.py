### Categorize New Member
## LINK ## https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/solutions/python
data = [(45, 12),(55,21),(19, -2),(104, 20)]
def open_or_senior(data): 
    m=[]
    for p in data:
        if p[0] >=55 and p[1]>7:
            m.append('Senior')
        else: m.append('Open')
    return m


"""
#samples of solution

def openOrSenior(data):
    return list(map(lambda d: 'Senior' if 7 < d[1] and 55 <= d[0] else 'Open', data))

def openOrSenior(data):
  return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]

def openOrSenior(data):
    return [['Open', 'Senior'][age >= 55 and handicap > 7] for age, handicap in data]]
"""
