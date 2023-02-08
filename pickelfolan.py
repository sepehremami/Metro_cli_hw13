import pickle
with open('username_list.list', 'rb') as f:
    content = pickle.load(f)

print(content)
