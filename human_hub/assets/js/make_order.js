$(document).ready(function() {
//-----------   CHECKOUT     -----------

    function get_loc_lang() {
        return window.location.toString().substr(window.location.toString().indexOf(window.location.host)
            + window.location.host.toString().length + 1,2);
    };

    var loclang = get_loc_lang();
    var checkout = document.getElementById("pop-order-checkout");
    document.getElementById("info-block").hidden = true;

    checkout.addEventListener("click", function() {
        document.getElementById("info-block").hidden = true;
        var checkout_form = document.getElementById("checkout-html-form");
        var formData = JSON.stringify($("#checkout-html-form").serializeArray());
        var new_check = 'X'
        if (document.getElementById("pop-order-checkout").innerHTML == 'X') {} else {

        $.ajax({
            url: '/' + loclang + '/orders/cart/checkout/',
            type: 'post',
            data: 'form=' + formData,
            success: function(data) {
            if (data.success) {
                if (data.payment) {
                document.getElementById("info-block").hidden = true;
                console.log(data.payment);
                var wayforpay = new Wayforpay();
                    var pay = function () {
                        wayforpay.run({
                                merchantAccount : data.payment.account,
                                merchantDomainName : data.payment.domain,
                                merchantTransactionType: data.payment.tr_type,
                                authorizationType : data.payment.auth_type,
                                merchantSignature : data.payment.sign,
                                returnUrl : data.payment.return_url,
                                serviceUrl: data.payment.url,
                                orderReference : data.payment.order_id,
                                orderDate : data.payment.order_date,
                                amount : data.payment.amount,
                                currency : data.payment.currency,
                                productName : [data.payment.products],
                                productPrice : data.payment.prices,
                                productCount : data.payment.counts,
                                clientFirstName : data.payment.first_name,
                                clientLastName : data.payment.last_name,
                                clientPhone: data.payment.phone,
                                language: data.payment.lang,
                                straightWidget: true
                            },
                            function (response) {
                            },
                            function (response) {
                            },
                            function (response) {
                            }
                        );
                    }
                    pay();
                };
                $("#hb-cart-total").html(data.cart_amount);
                document.getElementById("info-block").hidden = false;
                document.getElementById("info-block").innerHTML = data.info_block;
                document.getElementById("pop-order-checkout").innerHTML = new_check;
                var new_checkout = document.getElementById("new_check");
                checkout.addEventListener("click", function() {
                $("#hb-order-modal").modal('hide')});
                }
                else {document.getElementById("info-block").hidden = false;
                    document.getElementById("info-block").innerHTML = data.info_block};
        }})}
    });
//-----------   CHECKOUT     -----------
});