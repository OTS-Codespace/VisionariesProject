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
        <img class="product-image" src="${product.image}">
      </div>

      <div class="product-name limit-text-to-2-lines">
        ${product.name}
      </div>

      <div class="product-rating-container">
        <img class="product-rating-stars" src="images/ratings/rating-${product.rating.stars * 10}.png">
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
    const productId = button.dataset.productId;

    // Check if the product already exists in the cart
    let productInCart = cart.find(item => item.productId === productId);

    if (productInCart) {
      // If the product is already in the cart, just increase the quantity
      productInCart.quantity++;
    } else {
      // If the product is not in the cart, add it with quantity 1
      cart.push({
        productId: productId,
        quantity: 1
      });
    }

    // Now update the cart quantity displayed in the header
    updateCartQuantityDisplay();

    // Re-render the cart summary
    renderCartSummary();
  });
});

// Function to update cart quantity in the header
function updateCartQuantityDisplay() {
  let totalQuantity = 0;
  cart.forEach(item => totalQuantity += item.quantity);
  document.querySelector('.js-cart-quantity').innerText = totalQuantity;
}

// Function to render the cart summary on the checkout page
function renderCartSummary() {
  let cartSummaryHTML = '';

  cart.forEach((cartItem) => {
    const productId = cartItem.productId;
    let matchingProduct = products.find(product => product.id === productId);

    cartSummaryHTML += `
      <div class="cart-item-container js-cart-item-container-${matchingProduct.id}">
        <div class="delivery-date">Delivery date: Tuesday, June 21</div>
        <div class="cart-item-details-grid">
          <img class="product-image" src="${matchingProduct.image}">
          <div class="cart-item-details">
            <div class="product-name">${matchingProduct.name}</div>
            <div class="product-price">$${(matchingProduct.priceCents / 100).toFixed(2)}</div>
            <div class="product-quantity">
              <span>Quantity: <span class="quantity-label">${cartItem.quantity}</span></span>
              <span class="update-quantity-link link-primary">Update</span>
              <span class="delete-quantity-link link-primary js-delete-link" data-product-id="${matchingProduct.id}">
                Delete
              </span>
            </div>
          </div>
        </div>
      </div>
    `;
  });

  document.querySelector('.js-order-summary').innerHTML = cartSummaryHTML;

  // Add remove event listeners after rendering
  document.querySelectorAll('.js-delete-link').forEach((link) => {
    link.addEventListener('click', () => {
      const productId = link.dataset.productId;
      removeFromCart(productId);
    });
  });
}

function removeFromCart(productId) {
  // Remove the product from the cart
  cart = cart.filter(item => item.productId !== productId);

  // Update the cart display after removal
  renderCartSummary();
  updateCartQuantityDisplay();
}