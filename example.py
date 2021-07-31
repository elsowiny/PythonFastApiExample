from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Person(BaseModel):
    name: str
    age: int
    address: Optional[str] = None

people = {
    1:{
        "name":"John",
        "age":25,
        "address":"New York"

    },
    2:{
        "name":"Jack",
        "age":24,
        "address":"New York"
    },
    3:{
        "name":"Joe",
        "age":26,
        "address":"New York"
    },
    4:{
        "name":"Jack",
        "age":24,
        "address":"New Mexico"
    },
    5:{
        "name":"Jill",
        "age":25,
        "address":"New York"
    },
    6:{
        "name":"Jane",
        "age":58,
        "address":"Britain"
    },
    7:{
        "name":"Jake",
        "age":2,
        "address":"USA"
    },
    8:{
        "name":"Jake",
        "age":13,
        "address":"China"
    },
    9:{
        "name":"Joanna",
        "age":4,
        "address":"USA"
    },
    10:{
        "name":"Jilly Jane",
        "age":46,
        "address":"Lithuana",
        "job":"Teacher" #?
    },
    11:{
        "name":"Sherief",
        "age":12,
        "address":"Brazil"
    },
    13:{
        "name":"Magnus Carlson",
        "age":18,
        "address":"Sweden"
    },
    14:{
        "name":"Molly",
        "age":18,
        "address":"USA"
    },
    15:{
        "name":"Molly",
        "age":1,
        "address":"Australia"
    },
    16:{
        "name":"Molly",
        "age":3,
        "address":"Iceland"
    },
    17:{
        "name":"Mohammed",
        "age":18,
        "address":"Saudia Arabia"
    },
    18:{
        "name":"Steven",
        "age":13,
        "address":"Bolivia"
    }
}

@app.get("/")
def home():
    return {"message": " World"}

@app.get("/about")
def about():
    return {"message": " About"}

@app.get("/get-person/{person_id}")
def get_person(person_id: int = Path(None, description="The id of the person you want")):
    return people.get(person_id)

@app.get('/get-people')
def get_people( ):
    """Returns
    -------
    
        List of all people in the database
    """
    return people

@app.get("/get-by-name")
def get_by_name(name: str):
    """Returns
    -------
    
        List of all people with the given name
    """
    ppl = []
    
    for person_id in people:
        person = people[person_id]
        if person['name'].lower()==name.lower():
            ppl.append(person)
    if ppl:
        return ppl
    else:
        return {"message": "No person with that name"}

@app.post('/create-person')
def create_person(person: Person):
    """Creates a new person in the database
    """
    person_id = len(people) + 2
    people[person_id] = person
    return people[person_id]
