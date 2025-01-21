import {addToCart, cart} from '../data/cart.js';
import {products} from '../data/products.js';
/*
STEP 2: GENERATE THE HTML

- To generate the html instead of writing the html manually

- we can loop through the array to generate the html

- we will create some html for each of the product

- we use Accumulator pattern, we loop through an array and each time we are adding to the result so we're accumulating the result by combining the html into a variable

- we take the html and put it on the web page using the DOM

- the benefit of generating the HTML is that if you want to add another product you dont have to copy and paste all of the HTML again, we can just go to the data and add the date for a new product
*/

let productsHTML = '';

products.forEach((product) => {
  productsHTML += `
    <div class="product-container">
      <div class="product-image-container">
        <img class="product-image"
          src="${product.image}">
      </div>

      <div class="product-name limit-text-to-2-lines">
        ${product.name}
      </div>

      <div class="product-rating-container">
        <img class="product-rating-stars"
          src="images/ratings/rating-${product.rating.stars * 10}.png">
        <div class="product-rating-count link-primary">
          ${product.rating.count}
        </div>
      </div>

      <div class="product-price">
        $${(product.priceCents / 100).toFixed(2)} 
      </div>

      <div class="product-quantity-container">
        <select>
          <option selected value="1">1</option>
          <option value="2">2</option>
          <option value="3">3</option>
          <option value="4">4</option>
          <option value="5">5</option>
          <option value="6">6</option>
          <option value="7">7</option>
          <option value="8">8</option>
          <option value="9">9</option>
          <option value="10">10</option>
        </select>
      </div>

      <div class="product-spacer"></div>

      <div class="added-to-cart">
        <img src="images/icons/checkmark.png">
        Added
      </div>

      <button class="add-to-cart-button button-primary js-add-to-cart" data-product-id="${product.id}">
        Add to Cart
      </button>
    </div>
  `;

});


document.querySelector('.js-products-grid').innerHTML = productsHTML;

/*
  step 3: MAKE IT INTERACTIVE

  - Loop through the button and add an eventlistner

  ** FIGURING OUT HOW TO ADD THE PRODUCT TO A CART AND WHAT IT LOOKS LIKE
  - A cart is basically just a list and inside the list we have the product we want to buy, and the quantity of the product.

  - it can be represented in Javascript as an Array and inside the array we have an object contaning the product and quantity

  -we will use an html attribute called data attribute which allows us to attach any information to an html element.. dataset property gives us all the data attributes that are attached to the button.
  its written in kabab case in the html and in camelcase in the JS

  - we first attach the product id to the button using a data attribute and when we click d button, we got the product it out and the we add the product to the cart

*/


document.querySelectorAll('.js-add-to-cart').forEach((button) => {
  button.addEventListener('click', () => {
    // getting the property inside the html data attribute of the add to cart button
    const productId = (button.dataset.productId);

    addToCart(productId);

    // to make the cart quantity at the top interactive
    // step 1: Calculate the quantity, the total number of products in our cart

    let cartQuantity = 0

    cart.forEach((item) => {
      cartQuantity += item.quantity;
    });
    
    document.querySelector('.js-cart-quantity').innerHTML = cartQuantity;
    // console.log(cartQuantity);
    // console.log(cart);
  });
});  