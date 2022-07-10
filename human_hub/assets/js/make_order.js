$(document).ready(function() {
//-----------   CHECKOUT     -----------

    function get_loc_lang() {
        return window.location.toString().substr(window.location.toString().indexOf(window.location.host)
            + window.location.host.toString().length + 1,2);
    };

    var loclang = get_loc_lang();
    var checkout = document.getElementById("pop-order-checkout");
    document.getElementById("errors").hidden = true;

    checkout.addEventListener("click", function() {
        document.getElementById("errors").hidden = true;
        var checkout_form = document.getElementById("checkout-html-form");
        var formData = JSON.stringify($("#checkout-html-form").serializeArray());
        $.ajax({
            url: '/' + loclang + '/orders/cart/checkout/',
            type: 'post',
            data: 'form=' + formData,
            success: function(data) {
            if (data.success) {
            $("#hb-cart-total").html(data.cart_amount);
            $("#hb-order-modal").modal('hide')
            } else {document.getElementById("errors").hidden = false;
            document.getElementById("errors").innerHTML = data.errors}
            },
        });
    });







//-----------   CHECKOUT     -----------
});