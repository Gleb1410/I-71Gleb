PEOPLE = {
    "Fedorov": {
        "fname": "Глеб",
        "lname": "Федоров",
        "gname": "И-71",
        "pname": "Сафаров"

    },
    "Cherkashin": {
        "fname": "Никита",
        "lname": "Черкашин",
        "gname": "И-71",
        "pname": "Сафаров"

    }

}

def read_all():
    # Create the list of people from our data
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]

def read_one(lname):
    # Does the person exist in people?
    if lname in PEOPLE:
        person = PEOPLE.get(lname)

    # otherwise, nope, not found
    else:
        abort(
            404, "Person with last name {lname} not found".format(lname=lname)

        )

    return person

def create(person):
    lname = person.get("lname", None)
    fname = person.get("fname", None)
    gname = person.get("gname", None)
    pname = person.get("pname", None)

    # Does the person exist already?
    if lname not in PEOPLE and lname is not None:
        PEOPLE[lname] = {
            "lname": lname,
            "fname": fname,
            "gname": gname,
            "pname": pname,

        }
        return PEOPLE[lname], 201

    # Otherwise, they exist, that's an error
    else:
        abort(
            406,
            "Person with last name {lname} already exists".format(lname=lname),
        )

def update(lname, person):
    # Does the person exist in people?
    if lname in PEOPLE:
        PEOPLE[lname]["fname"] = person.get("fname")
        PEOPLE[lname]["gname"] = person.get("gname")
        return PEOPLE[lname]

    # otherwise, nope, that's an error
    else:
        abort(
            404, "Person with last name {lname} not found".format(lname=lname)
        )

def delete(lname):
    # Does the person to delete exist?
    if lname in PEOPLE:
        del PEOPLE[lname]
        return make_response(
            "{lname} successfully deleted".format(lname=lname), 200
        )

    # Otherwise, nope, person to delete not found
    else:
        abort(
            404, "Person with last name {lname} not found".format(lname=lname)
        )