$(document).ready(function() {

    console.log("HERE");
    $('#payment-save').on('click', function() {
        console.log("CLICK");
        var payment_sum = document.getElementById('payment_sum').value
        var order_id = $(this).data('order-id');
        var button_id = "order-payed-" + order_id;
        $.ajax({
            url: $(this).data('order-id') + '/payed-save/',
            type: 'post',
            data: 'sum=' + payment_sum,
            success: function(data) {
                 console.log("SUCCESS");
                 $("#cc-order-modal").modal('hide');
                 document.getElementById(button_id).hidden = true;
                 var elem_id = "cc-order-payment-" + order_id;
                 console.log(elem_id);
                 var container = document.getElementById(elem_id);
                 var content = payment_sum + " UAH" + "<br/>"
                 container.innerHTML= content;
            }
        });
    });
});

//location.reload();