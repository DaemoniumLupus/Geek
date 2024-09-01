function string(i,x){
    if (i > 0){
        return string(i-1,x) + x;
    }else return x;
}

function gorka() {
    let x = '#';
    for(let i = 0; i <= 20; i++){
        console.log(`${string(i,x)}`);
    }
}

gorka();