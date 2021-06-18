tagged_text = [('text', 'This is a ', '1.0'), ('tagon', 'BOLD', '1.10'), ('text', 'sample', '1.10'), ('tagoff', 'BOLD', '1.16'), ('text', ' of ', '1.16'), ('tagon', 'HIGHLIGHT', '1.20'), ('text', 'formatted', '1.20'), ('tagoff', 'HIGHLIGHT', '1.29'), ('text', ' text', '1.29'), ('mark', 'current', '1.34'), ('mark', 'tk::anchor1', '1.34'), ('mark', 'insert', '1.34'), ('text', '\n', '1.34')]

# print(type(text)) # list (of tuples)

text_str = ""

for index, tuple in enumerate(tagged_text):
  item_one = tuple[0]
  item_two = tuple[1]
  # print(index, item_one, item_two)
  # text_str += item_two

  if item_one == "text":
    print(item_two)
    text_str += item_two
  elif item_one == "tagon":
    new_index = index + 1
    # print(tagged_text[new_index][1])
    if item_two == "BOLD":
      print(tagged_text[new_index][1])
      # apply formatting & concat?
      tagged_text.remove(tagged_text[new_index]) # remove to avoid repeat
    elif item_two == "HIGHLIGHT":   
      print(tagged_text[new_index][1])
      # apply formatting & concat?      
      tagged_text.remove(tagged_text[new_index]) # remove to avoid repeat
  else: # taggoff
    pass
  

  
# print(tagged_text[0][1]) # This is a
# print(text_str)


