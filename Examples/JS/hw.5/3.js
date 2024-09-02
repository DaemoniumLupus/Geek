const products = [
    {
        id: 3,
        price: 200,
    },
    {
        id: 4,
        price: 900,
    },
    {
        id: 1,
        price: 1000,
    },
];

console.log(products);
// Не понял почему объект при первом вызове уже с измененной ценой
products.forEach((lower) => lower.price -= lower.price * 0.15);

console.log(products);