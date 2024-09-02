const en = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"];
const ru = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"];

let dayOfWeek = new Map();

for(let i = 0; i < en.length; i++){
    dayOfWeek.set(en[i],ru[i]);
}

console.log(dayOfWeek);