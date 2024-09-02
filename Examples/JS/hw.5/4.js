const products = [
    {
        id: 3,
        price: 127,
        photos: [
            "1.jpg",
            "2.jpg",
        ],
    },
    {
        id: 5,
        price: 499,
        photos: [],
    },
    {
        id: 10,
        price: 26,
        photos: [
            "3.jpg",
        ],
    },
    {
        id: 8,
        price: 78,
    },
];

console.log(products.filter(function (product)  {
        if (product.photos){
            if (product.photos != false){
                return true;
            }
        }
        return false;
    }
))


console.log(products.sort((a, b) => a.price > b.price));