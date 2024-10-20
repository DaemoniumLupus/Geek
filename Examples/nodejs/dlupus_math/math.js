/**
 * Принимает переменные a, b, c из уравнения вида "ax^2 + bx + c = 0" 
 * @param {Number} a 
 * @param {Number} b 
 * @param {Number} c 
 * @returns {string}
 */
function square(a, b, c) {
    var discriminant = b * b - 4 * a * c;
    if (discriminant < 0) {
        return 'Уравнение не имеет реальных корней';
    } else if (discriminant === 0) {
        return 'Уравнение имеет один корень: ' + (-b / (2 * a));
    } else {
        var root1 = (-b + Math.sqrt(discriminant)) / (2 * a);
        var root2 = (-b - Math.sqrt(discriminant)) / (2 * a);
        return 'Уравнение имеет два корня: ' + root1 + ' и ' + root2;
    }
}

module.exports = {square};