norway_text = "Automatisering akselererer %syeblikket " \
              "da roboter vil erobre planeten v%sr. (%s)" % ('ø', 'å', 'Æ')
form_call = 'Call-format: {}' .format(norway_text)
f_string = f'F-string: {norway_text}'

print(norway_text)
print(form_call)
print(f_string)

