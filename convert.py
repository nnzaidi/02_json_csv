import json

if __name__ == '__main__':
    try:
        with open('input.json','r') as f:
            data = json.loads(f.read())

        output = ','.join([*data[0]]) #keys of the dictionary
        for obj in data:
            output += f'\n{obj["Brand"]},{obj["Model"]},{obj["Year"]}' #extract the element for each key

        with open('output.csv','w') as f:
            f.write(output)

    except Exception as ex:
        print(f'Error : str{ex}')