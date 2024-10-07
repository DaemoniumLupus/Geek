window ['json'] = [
    {
        "position":"one",
        "name": "LLERY X M'O CAPSULE",
        "text": "Known for her sculptural takes on traditional tailoring, Australian arbiter of cool Kym Ellery teams up with Moda Operandi.",
        "size": "XS",
        "color": "Blue",
        "price": "$52.00",
        "img": "../image/product1.jpg"
    },
    {
        "position":"two",
        "name": "LLERY X M'O CAPSULE",
        "text": "Known for her sculptural takes on traditional tailoring, Australian arbiter of cool Kym Ellery teams up with Moda Operandi.",
        "size": "XS",
        "color": "Black",
        "price": "$52.00",
        "img": "../image/product2.jpg"
    },
    {
        "position":"three",
        "name": "LLERY X M'O CAPSULE",
        "text": "Known for her sculptural takes on traditional tailoring, Australian arbiter of cool Kym Ellery teams up with Moda Operandi.",
        "size": "XS",
        "color": "Blue",
        "price": "$52.00",
        "img": "../image/product3.jpg"
    },
    {
        "position":"four",
        "name": "LLERY X M'O CAPSULE",
        "text": "Known for her sculptural takes on traditional tailoring, Australian arbiter of cool Kym Ellery teams up with Moda Operandi.",
        "size": "XS",
        "color": "Blue",
        "price": "$52.00",
        "img": "../image/product4.jpg"
    },
    {
        "position":"five",
        "name": "LLERY X M'O CAPSULE",
        "text": "Known for her sculptural takes on traditional tailoring, Australian arbiter of cool Kym Ellery teams up with Moda Operandi.",
        "size": "XS",
        "color": "Red",
        "price": "$52.00",
        "img": "../image/product5.jpg"
    },
    {
        "position":"six",
        "name": "LLERY X M'O CAPSULE",
        "text": "Known for her sculptural takes on traditional tailoring, Australian arbiter of cool Kym Ellery teams up with Moda Operandi.",
        "size": "XS",
        "color": "Green",
        "price": "$52.00",
        "img": "../image/product6.jpg"
    }
]

const position = {
    "one": " 1 / 1 / 2 / 2",
    "two": "2 / 1 / 3 / 2",
    "three": "3 / 1 / 4 / 2",
    "four": "4 / 1 / 5 / 2",
    "five": "3 / 1 / 4 / 2",
    "six": "3 / 2 / 4 / 3"
}

const htmlForSvg = `
                            <path
                                d="M21.9509 23.2667H21.8386C21.2294 23.2667 20.7177 22.7671 20.6735 22.1294C20.629 21.4607 21.1175 20.8785 21.7626 20.8346C21.788 20.8329 21.8145 20.832 21.8405 20.832C22.4575 20.832 22.9743 21.3219 23.0201 21.9487C23.0319 22.1971 22.9914 22.5514 22.736 22.8439L22.73 22.8507L22.7242 22.8575C22.5275 23.0912 22.2607 23.2321 21.9509 23.2667ZM8.21887 23.2604C7.5683 23.2604 7.03906 22.7174 7.03906 22.05C7.03906 21.3832 7.5683 20.8406 8.21887 20.8406C8.86945 20.8406 9.39868 21.3832 9.39868 22.05C9.39868 22.7174 8.86945 23.2604 8.21887 23.2604Z"
                                fill="white" />
                            <path
                                d="M21.876 22.2662C21.921 22.2549 21.9423 22.2339 21.96 22.2129C21.9678 22.2037 21.9756 22.1946 21.9835 22.1855C22.02 22.1438 22.0233 22.0553 22.0224 22.0105C22.0092 21.9044 21.9185 21.8315 21.8412 21.8315C21.8375 21.8315 21.8336 21.8317 21.8312 21.8318C21.7531 21.8372 21.6653 21.9409 21.6719 22.0625C21.6813 22.1793 21.7675 22.2662 21.8392 22.2662H21.876ZM8.21954 22.2599C8.31873 22.2599 8.39935 22.1655 8.39935 22.0496C8.39935 21.9341 8.31873 21.8401 8.21954 21.8401C8.12042 21.8401 8.03973 21.9341 8.03973 22.0496C8.03973 22.1655 8.12042 22.2599 8.21954 22.2599ZM21.9995 24.2662C21.9517 24.2662 21.8878 24.2662 21.8392 24.2662C20.7017 24.2662 19.7567 23.3545 19.6765 22.198C19.5964 20.9929 20.4937 19.9183 21.6953 19.8364C21.7441 19.8331 21.7928 19.8315 21.8412 19.8315C22.9799 19.8315 23.9413 20.7324 24.019 21.8884C24.0505 22.4915 23.8741 23.0612 23.4898 23.5012C23.1055 23.9575 22.5764 24.2177 21.9995 24.2662ZM8.21954 24.2599C7.01532 24.2599 6.03973 23.2709 6.03973 22.0496C6.03973 20.8291 7.01532 19.8401 8.21954 19.8401C9.42371 19.8401 10.3994 20.8291 10.3994 22.0496C10.3994 23.2709 9.42371 24.2599 8.21954 24.2599ZM21.1984 17.3938H9.13306C8.70013 17.3938 8.31586 17.1005 8.20331 16.6775L4.27753 2.24768H1.52173C0.993408 2.24768 0.560547 1.80859 0.560547 1.27039C0.560547 0.733032 0.993408 0.292969 1.52173 0.292969H4.99933C5.43134 0.292969 5.81561 0.586304 5.9281 1.01025L9.85394 15.4391H20.5576L24.1144 7.13379H12.2578C11.7286 7.13379 11.2957 6.69373 11.2957 6.15649C11.2957 5.61914 11.7286 5.17908 12.2578 5.17908H25.5886C25.9091 5.17908 26.2141 5.34192 26.3896 5.61914C26.566 5.89539 26.5984 6.23743 26.4697 6.547L22.0795 16.807C21.9193 17.1653 21.5827 17.3938 21.1984 17.3938Z"
                                fill="white" />
                            <path
                                d="M21.876 22.2662C21.921 22.2549 21.9423 22.2339 21.96 22.2129C21.9678 22.2037 21.9756 22.1946 21.9835 22.1855C22.02 22.1438 22.0233 22.0553 22.0224 22.0105C22.0092 21.9044 21.9185 21.8315 21.8412 21.8315C21.8375 21.8315 21.8336 21.8317 21.8312 21.8318C21.7531 21.8372 21.6653 21.9409 21.6719 22.0625C21.6813 22.1793 21.7675 22.2662 21.8392 22.2662H21.876ZM8.21954 22.2599C8.31873 22.2599 8.39935 22.1655 8.39935 22.0496C8.39935 21.9341 8.31873 21.8401 8.21954 21.8401C8.12042 21.8401 8.03973 21.9341 8.03973 22.0496C8.03973 22.1655 8.12042 22.2599 8.21954 22.2599ZM21.9995 24.2662C21.9517 24.2662 21.8878 24.2662 21.8392 24.2662C20.7017 24.2662 19.7567 23.3545 19.6765 22.198C19.5964 20.9929 20.4937 19.9183 21.6953 19.8364C21.7441 19.8331 21.7928 19.8315 21.8412 19.8315C22.9799 19.8315 23.9413 20.7324 24.019 21.8884C24.0505 22.4915 23.8741 23.0612 23.4898 23.5012C23.1055 23.9575 22.5764 24.2177 21.9995 24.2662ZM8.21954 24.2599C7.01532 24.2599 6.03973 23.2709 6.03973 22.0496C6.03973 20.8291 7.01532 19.8401 8.21954 19.8401C9.42371 19.8401 10.3994 20.8291 10.3994 22.0496C10.3994 23.2709 9.42371 24.2599 8.21954 24.2599ZM21.1984 17.3938H9.13306C8.70013 17.3938 8.31586 17.1005 8.20331 16.6775L4.27753 2.24768H1.52173C0.993408 2.24768 0.560547 1.80859 0.560547 1.27039C0.560547 0.733032 0.993408 0.292969 1.52173 0.292969H4.99933C5.43134 0.292969 5.81561 0.586304 5.9281 1.01025L9.85394 15.4391H20.5576L24.1144 7.13379H12.2578C11.7286 7.13379 11.2957 6.69373 11.2957 6.15649C11.2957 5.61914 11.7286 5.17908 12.2578 5.17908H25.5886C25.9091 5.17908 26.2141 5.34192 26.3896 5.61914C26.566 5.89539 26.5984 6.23743 26.4697 6.547L22.0795 16.807C21.9193 17.1653 21.5827 17.3938 21.1984 17.3938Z"
                                fill="white"`

const xmlns = "http://www.w3.org/2000/svg";

function items() {
    const productions = document.querySelector(".product-box");

    const boxHeading = document.createElement("h2");
    boxHeading.className = "product-box__heading";
    boxHeading.textContent = "Fetured Items";
    
    const boxText = document.createElement("p");
    boxText.className = "product-box__text";
    boxText.textContent = "Shop for items based on what we featured in this week";

    const boxContent = document.createElement("div");
    boxContent.className = "product-box__content";
    
    productions.appendChild(boxHeading);
    productions.appendChild(boxText);
    productions.appendChild(boxContent);


    json.forEach(element => {
        const product = document.createElement("div");
        product.className = `product ${element.position}`;

        const img = document.createElement("img");
        img.classList = "product__img";
        img.src = `${element.img}`;
        
        const content = document.createElement("div");
        content.className = "product__content";

        const productLink = document.createElement("a");
        productLink.className = "product__heading";
        productLink.textContent = `${element.name}`;

        const productText = document.createElement("p");
        productText.className = "product__text";
        productText.textContent = `${element.text}`;

        const productPrice = document.createElement("p");
        productPrice.className = "product__price";
        productPrice.textContent = `${element.price}`;

        const productAdd = document.createElement("btn");
        productAdd.classList = "product__add";

        const svg = document.createElementNS(xmlns, "svg");
        svg.innerHTML = htmlForSvg;
        svg.setAttributeNS(null, "viewBox", "0 0 27 25");
        svg.setAttributeNS(null, "width", 27);
        svg.setAttributeNS(null, "height", 25);

        //Ели попытаться поставить первым рисунок корзины то она пропадает
        productAdd.textContent = "Add to Cart";
        productAdd.appendChild(svg);
        
        boxContent.appendChild(product);
        product.appendChild(img);
        product.appendChild(content);
        product.appendChild(productAdd);
        content.appendChild(productLink);
        content.appendChild(productText);
        content.appendChild(productPrice);
    });
}

