from utilities.configuration import get_query


def addBookPayload(isbn,BookID):
    body = {
        "name": "Learning Python",
        "isbn": isbn,
        "aisle": BookID,
        "author": "Jaifee foe"
    }
    return body


def buildPayLoadFormDB(query):
    addBody = {}
    tp = get_query(query)
    addBody['name'] = tp[0]
    addBody['isbn'] = tp[1]
    addBody['aisle'] = tp[2]
    addBody['author'] = tp[3]
    return addBody
