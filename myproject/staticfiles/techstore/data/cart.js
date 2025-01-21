export let cart =JSON.parse(localStorage.getItem('cart')); 
  
if(!cart){
  cart = [
    // {
    //   productId: "e43638ce-6aa0-4b85-b27f-e1d07eb678c6",
    //   quantity: 2,
    // },
    // {
    //   productId: "15b6fc6f-327a-4ec4-896f-486349e85a3d",
    //   quantity: 1,
    // },
  ];
}


// we need to save our cart with local storage so that it will not return to the previous value whenever we refresh our page or move to another page.

const saveToStorage = () => {
  localStorage.setItem('cart', JSON.stringify(cart));
}

export const addToCart = (productId) => {
  // checking if the product is in the cart
  let matchingItem;

  cart.forEach((item) => {
    if (productId === item.productId) {
      matchingItem = item;
    }
  });

  // increase the quantity by 1 if the product is in the cart if not add it to the cart
  if (matchingItem) {
    matchingItem.quantity += 1;
  } else {
    cart.push({
      productId: productId,
      quantity: 1,
    });
  }
  saveToStorage();
}

// To delete a product from thw cart

export const removeFromCart = (productId) => {
  // we need to create a  new array first
  const newCart = []

  // loop through the cart
  cart.forEach((cartItem) => {
    // we will add each cart item to the new array expect if it has the same productId
    if(cartItem.productId !== productId){
      newCart.push(cartItem);
    }
  });
  // replace cart with the new cart
  cart = newCart;

  saveToStorage();
}