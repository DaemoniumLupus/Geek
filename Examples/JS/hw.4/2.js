function mas() {
    let array = [1,2,3,4,5,6,7];
    console.log(array);
    for (let i = 0; i < array.length; i++){
        if (array[i] === 4){
            array.splice(i,2);
        }
    }
    console.log(array);

}

mas();