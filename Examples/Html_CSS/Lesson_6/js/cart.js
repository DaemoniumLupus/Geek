

function cart() {
    const products = document.querySelectorAll(".product__add");
    // console.log(products);

    
    
    
    
    products.forEach(product => {
        product.addEventListener("click", (event) => {
            const item = event.target.closest('.product');
            
            // cart.appendChild(cartBox);

            
            addToCart(item);
            // console.log(item.classList[1]);
        });
    });

    
}

function addToCart(product) {
    const cart = document.querySelector(".cart");
    
    let data = json.find(function(item){
        return item["position"] == product.classList[1];
    });

    console.log(document.querySelectorAll(".cart__box"));
    
    let cartBox;
    
    if (document.querySelectorAll(".cart__box").length == 0){
        console.log("ryt");
        cartBox = document.createElement("div");
        cartBox.className = "cart__box";
        const cartHead = document.createElement("h3");
        cartHead.className = "product-box__heading";
        cartHead.textContent = "Cart Items";
        cartBox.appendChild(cartHead);
    }else{
        cartBox = document.querySelector(".cart__box");
    }
    
    const item = document.createElement("div");
    item.className = "item";

    const img = document.createElement("img");
    img.className = "item__img"
    img.src = `${data.img}`;

    const itemContent = document.createElement("div");
    itemContent.className = "item__content";

    const itemHead = document.createElement("h3");
    itemHead.className = "item__heading"
    itemHead.textContent = `${data.name}`;

    const itemSize = document.createElement("p");
    itemSize.className = "item__text";
    itemSize.textContent = `Size: ${data.size}`;

    const itemColor = document.createElement("p");
    itemColor.className = "item__text";
    itemColor.textContent = `Color: ${data.color}`;
    

    const itemPrice = document.createElement("p");
    itemPrice.className = " item__text";
    itemPrice.innerHTML = `Price: <span class="item__color">${data.price}</span>`;


    const itemQuantity = document.createElement("div");
    itemQuantity.className = "item__text";
    itemQuantity.innerHTML = `
    Quantity: <input class="item__input" type="text" value="1">
    `;

    const itemDelete = document.createElement("button");
    itemDelete.className = "item__product-delete";
    itemDelete.addEventListener("click", (event) => {
        const item = event.target.closest('.item');
        item.remove();
        if(document.querySelectorAll(".item").length == 0){
            document.querySelector(".cart__box").remove();
        }
    })



    itemContent.appendChild(itemDelete);
    itemContent.appendChild(itemHead);
    itemContent.appendChild(itemPrice);
    itemContent.appendChild(itemColor);
    itemContent.appendChild(itemSize);
    itemContent.appendChild(itemQuantity);
    
    item.appendChild(img);
    item.appendChild(itemContent);
    
    cartBox.appendChild(item);

    cart.appendChild(cartBox);

    
    // console.log(cart);
}

