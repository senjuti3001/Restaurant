$(function(){

    //back-To-Top//

    $('.back-To-Top').click(function(){
        $('html, body').animate({scrollTop:0}, 1500);

    })

    $(window).scroll(function(){
        var scrolling= $(this).scrollTop();
        if(scrolling>200){
            $('.back-To-Top').fadeIn();
        }
        else{
            $('.back-To-Top').fadeOut();
        }

        if(scrolling>150){
            $('.nav').addClass('bg');
        }
        else{
            $('.nav').removeClass('bg');
        }
    })

    //preloader//

    $(window).on('load', function(){
        $('.preloader').delay(500).fadeOut(500);
    })


    //smooth-scroll//


    var scroll = new SmoothScroll('a[href*="#"]', {
        speed: 1000
    });


})

let carts = document.querySelectorAll('.add-cart');

let products = [
    {
        name: 'Biriyani',
        tag: 'biriyani',
        price: 200,
        incart: 0,
    },
    {
        name: 'Desert',
        tag: 'desert',
        price: 350,
        incart: 0,
    },
    {
        name: 'Desert',
        tag: 'desert',
        price: 200,
        incart: 0,
    },
    {
        name: 'Biriyani',
        tag: 'biriyani',
        price: 200,
        incart: 0,
    },
];

for (let i=0; i < carts.length; i++){
    carts[i].addEventListener('click' , ()  => {
          cartNumbers(products[i]);
          totalCost(products[i]);
    })
}

function onLoadCartNumbers(){
    let productNumbers = localStorage.getItem('cartNumbers');

    if(productNumbers){
        document.querySelector('.cart span').textContent = productNumbers;
    }
}

function cartNumbers(product){
    let productNumbers = localStorage.getItem('cartNumbers');

    productNumbers = parseInt(productNumbers);
    
    if( productNumbers ){
        localStorage.setItem('cartNumbers' , productNumbers + 1);
        document.querySelector('.cart span').textContent = productNumbers + 1;
    }else{
        localStorage.setItem('cartNumbers' , 1);
        document.querySelector('.cart span').textContent =  1;
    }

    setItems(product)
    
}

function setItems(product) {
    let cartItems = localStorage.getItem('productsInCart');
    cartItems = JSON.parse(cartItems);

     if(cartItems != null){
        
        if(cartItems[product.tag] == undefined){
            cartItems = {
                ...cartItems,
                [product.tag]: product
            }
        }
        cartItems[product.tag].inCart +=1
     }
     else{
         product.inCart = 1;
         cartItems = {
             [product.tag]: product
         }
     }
    
    localStorage.setItem("productsInCart", JSON.stringify(cartItems));
}

function totalCost(product){
    // console.log("The product price is", product.price);
    let cartCost = localStorage.getItem('totalCost');

    console.log("My cartCost is", cartCost);
    console.log(typeof cartCost );

    if(cartCost != null){
        cartCost = parseInt(cartCost);
        localStorage.setItem("totalCost", cartCost + product.price);
    }
    else{
        localStorage.setItem("totalCost", product.price);
    }
}

onLoadCartNumbers();