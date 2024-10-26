const express = require('express');
const app = express();
app.use(express.json());

const { personScheme, idScheme } = require('./validation/schema');
const { checkBody, checkParams } = require('./validation/validator');
const { getPersons, putData, uniqueID } = require('./data/data');

const port = 3000;
let persons;

app.get('/persons',getPersons(), (req, res) => {
    res.send(req.locals);
});

app.get('/persons/:id', checkParams(idScheme), getPersons(), (req, res) => {
    persons = req.locals;

    const person = persons.find((person) => person.id === Number(req.params.id));

    if (person){
        res.send({ person });
    }else {
        res.status(404);
        res.send({ person: null});
    }
});

app.post('/persons',getPersons(), checkBody(personScheme), (req, res) => {
    persons = req.locals;

    let id = uniqueID(persons);

    persons.push({
        id: id,
        ...req.body
    });

    putData(persons);

    res.send({
        id: id
    });
});

app.put('/persons/:id', checkParams(idScheme), checkBody(personScheme), getPersons(), (req, res) => {
    persons = req.locals;

    const person = persons.find((person) => person.id === Number(req.params.id));

    if(person) {
        person.firstName = req.body.firstName;
        person.secondName = req.body.secondName;
        person.age = req.body.age;
        person.city = req.body.city;

        res.send({ person });

        putData(persons);
    }else {
        res.status(404);
        res.send({ person: null});
    }
});

app.delete('/persons/:id', checkParams(idScheme), getPersons(), (req, res) => {
    persons = req.locals;

    const person = persons.find((person) => person.id === Number(req.params.id));

    if(person) {
        const personeIndex = persons.indexOf((person));
        persons.splice(personeIndex, 1);
        console.log(persons);
        putData(persons);
        res.send({ person });
    }else {
        res.status(404);
        res.send({ person: null});
    }
})

app.use((req, res) => {
    res.status(404).send({
        "message": 'URL not found'
    });
});


app.listen(port, () => console.log(`Example app listening on port ${port}!`));

