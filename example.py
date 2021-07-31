from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional
from localdata import people
app = FastAPI()

class Person(BaseModel):
    name: str
    age: int
    address: Optional[str] = None



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
