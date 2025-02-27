import json

# gets data from a table
def fetch(tableName):
    with open(f"playerDB/{tableName}.json", "r") as file:
        data = json.load(file)

    return data


# posts data to a table
def post(tableName, data):
    with open(f"playerDB/{tableName}.json", "w") as file:
        json.dump(data, file, indent = 4, sort_keys = True)



# function deals with getting data from any table based on the table's name and any parameters
def getData(tableName, **kwargs):
    # fetches the data from the table
    data = fetch(tableName)

    # declaring variable to hold any matches
    result = []

    # loops through every record
    for record in data:
        match = True

        # for each parameter checks whether the record passes the parameters
        for key, value in kwargs.items():
            if record[key] != value:
                match = False

        # if passes all parameter tests, record is appended to result
        if match == True:
            result.append(record)
            
    return result



# checks whether a certain value is unique
def isUnique(key, value, *args):
    # fetches data from users table
    data = fetch("users")

    if len(args) == 0:
        # if the value for a certain key (username or email) is found in another record
        # it returns false to show that the value is not unique
        for record in data:
            if record[key] == value:
                return False
            
    else:
        for record in data:
            if record[key] == value and record["id"] != args[0]:
                return False
        
    return True



# inserts data into a table
def insert(tableName, record):
    # fetch data
    data = fetch(tableName)

    # id is an increasing value and is thus the length of the current table
    # -> id indexing starts at 0
    id = len(data)

    if not hasattr(record, "id"):
        # ensures the id field is filled
        record["id"] = id

    # adds the record
    data.append(record)

    # adds data to table
    post(tableName, data)

    return id



# alter the record within a table
def update(tableName, record, id):
    # gets data
    data = fetch(tableName)

    if not hasattr(record, "id"):
        # ensures id field is filled
        record["id"] = id

    # places the record at the right place
    # -> id is equivalent to the record's position
    data[id] = record

    # posts data to table
    post(tableName, data)
