$(document).ready(function() {

    var closebtns = document.getElementsByClassName("close-cart-item");
    var i;
    var tot_price = document.getElementById("cart_total_price").innerHTML;
    if (tot_price == 0) {
        document.getElementById("show-order-modal").hidden = true;
        };

    for (i = 0; i < closebtns.length; i++) {
        closebtns[i].addEventListener("click", function() {
            card = this.parentElement.parentElement
            card.parentElement.removeChild(card);
            $.ajax({
                url: '/orders/cart/' + $(this).data('id') + '/remove/',
                type: 'post',
                success: function(data) {
                if (data.success) {
                $("#cart_total_price").html(data.cart_total)
                $("#hb-cart-total").html(data.cart_amount)
                }
                },
            });
            tot = document.getElementById("cart_total_price");
      });
    };

});

