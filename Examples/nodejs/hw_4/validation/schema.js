const joi = require('joi');

const personScheme = joi.object({
    firstName: joi.string().min(1).required(),
    secondName: joi.string().min(1).required(),
    age: joi.number().min(0).max(150).required(),
    city: joi.string().min(1)
});

const idScheme = joi.object({
    id: joi.number().required()
});

module.exports = { personScheme, idScheme }