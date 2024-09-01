function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}

function findInArray(mas, find){
    if (mas.find((element) => element === find)){
        return 'Yes';
    } else return 'No';
    
}

function rand() {
    let mas = new Array(5);
    for (let i = 0; i < mas.length; i++){
        mas[i] = getRandomInt(10);
    }
    console.log(mas);

    // Сумма элементов массива
    console.log(`Сумма элементов - ${mas.reduce(function(a,b){
        return a + b;
    }, 0)}`);

    // Минимальное значиние в массиве
    console.log(`Минимальное значение - ${Math.min(...mas)}`);

    //Проверка есть ли число 3
    console.log(`Есть ли тройка? - ${findInArray(mas,3)}`);
}

rand();