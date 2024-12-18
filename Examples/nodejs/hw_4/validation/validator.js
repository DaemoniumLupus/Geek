function checkParams(schema) {
    return (req, res, next) => {
        const validationResult = schema.validate(req.params);
        if(validationResult.error) {
            return res.status(400).send(validationResult.error.datails);
        }
        next();
    }
}

function checkBody(schema) {
    return (req, res, next) => {
        const validationResult = schema.validate(req.body);
        if(validationResult.error) {
            return res.status(400).send(validationResult.error.datails);
        }
        next();
    }
}

module.exports = { checkBody, checkParams };