const numbers = {
    keyin1: 1,
    keyin2: 2,
    keyin3: 3,
    keyin4: 4,
    keyin5: 5,
    keyin6: 6,
    keyin7: 7,
}

for(let number in numbers){
    if(numbers[number] >= 3){
        console.log(`${number}: ${numbers[number]}`);
    }
}