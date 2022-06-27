$(document).ready(function() {
//-----------   CHECKOUT     -----------

//    const visa-mstrcrd = document.getElementById("ordr-pay-visa-mstrcrd");
//    const applepay = document.getElementById("ordr-pay-applepay");
//    const googlepay = document.getElementById("ordr-pay-googlepay");
//    const paypal = document.getElementById("ordr-pay-paypal");
//    const bycard = document.getElementById("ordr-pay-bycard");
//    const cash-on-del = document.getElementById("ordr-pay-cash-on-del");
//
//    visa-mstrcrd.addEventListener('click', () => {
//        if (visa-mstrcrd.checked) {
//            applepay.checked = false;
//            googlepay.checked = false;
//            paypal.checked = false;
//            bycard.checked = false;
//            cash-on-del.checked = false;
//        };
//    });
//
//    applepay.addEventListener('click', () => {
//        if (applepay.checked) {
//            visa-mstrcrd.checked = false;
//            googlepay.checked = false;
//            paypal.checked = false;
//            bycard.checked = false;
//            cash-on-del.checked = false;
//        };
//    });
//
//    googlepay.addEventListener('click', () => {
//        if (googlepay.checked) {
//            visa-mstrcrd.checked = false;
//            applepay.checked = false;
//            paypal.checked = false;
//            bycard.checked = false;
//            cash-on-del.checked = false;
//        };
//    });
//
//    paypal.addEventListener('click', () => {
//        if (paypal.checked) {
//            visa-mstrcrd.checked = false;
//            applepay.checked = false;
//            googlepay.checked = false;
//            bycard.checked = false;
//            cash-on-del.checked = false;
//        };
//    });
//
//    bycard.addEventListener('click', () => {
//        if (bycard.checked) {
//            visa-mstrcrd.checked = false;
//            applepay.checked = false;
//            googlepay.checked = false;
//            paypal.checked = false;
//            cash-on-del.checked = false;
//        };
//    });
//
//    cash-on-del.addEventListener('click', () => {
//        if (cash-on-del.checked) {
//            visa-mstrcrd.checked = false;
//            applepay.checked = false;
//            googlepay.checked = false;
//            paypal.checked = false;
//            bycard.checked = false;
//        };
//    });

    var checkout = document.getElementById("pop-order-checkout");
    document.getElementById("errors").hidden = true;

    checkout.addEventListener("click", function() {
        document.getElementById("errors").hidden = true;
        var checkout_form = document.getElementById("checkout-html-form");
        var formData = JSON.stringify($("#checkout-html-form").serializeArray());
        $.ajax({
            url: '/orders/cart/checkout/',
            type: 'post',
            data: 'form=' + formData,
            success: function(data) {
            if (data.success) {
            $("#hb-cart-total").html(data.cart_amount);
            $("#hb-order-modal").modal('hide')
            } else {document.getElementById("errors").hidden = false;
            console.log(data.errors)
            document.getElementById("errors").innerHTML = data.errors}
            },
        });

    });







//-----------   CHECKOUT     -----------
});