# while loop works inside a for loop the following is how for loop works inside

def traverse_items_dict(data):
    it = iter(data)
    while True:
        try:
            K,V = next(it)
            print(K,V)
        except StopIteration:
            print("done")
            break

traverse_items_dict({"shashwat":50,"ram":78,"hema":73})
