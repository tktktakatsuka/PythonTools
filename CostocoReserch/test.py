import re

content = "   返金済み"
pattern = '.*返金済み.*'
result = re.fullmatch(pattern, str(content))

print(result)