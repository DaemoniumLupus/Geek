const fs = require('fs');
const path = require('path');
const { error } = require('console');
const { func } = require('joi');


function getPersons() {
    return (req, res, next) =>{
        const data = fs.readFileSync(path.join(__dirname, 'persons.json'), "utf-8");
        if (!data){
            res.status(400).send(error);
        }else{
            req.locals = JSON.parse(data);
        }
        next();
    }   

};

function putData(persons) {
    const data = JSON.stringify(persons,null, 2);
    fs.writeFileSync(path.join(__dirname, 'persons.json'), data);

}

function uniqueID(persons) {
    let max = 0;
    persons.forEach(element => {
        if (element.id > max){
            max = element.id;
        }
    });
    return max += 1;
}

module.exports = { getPersons, putData, uniqueID };