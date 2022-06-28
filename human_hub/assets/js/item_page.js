$(document).ready(function() {
// choose size massage element
document.getElementById("must-choose").hidden = true
// choose size massage element

//carousel
    var bigimage = $("#big");
    var thumbs = $("#thumbs");
    var syncedSecondary = true;

    bigimage.owlCarousel({
        items: 1,
        slideSpeed: 2000,
        nav: true,
        autoplay: true,
        dots: false,
        loop: true,
        responsiveRefreshRate: 200,
        navText: [
            '<i class="fa fa-arrow-left" aria-hidden="true"></i>',
            '<i class="fa fa-arrow-right" aria-hidden="true"></i>'
        ]
    }).on("changed.owl.carousel", syncPosition);

    thumbs.on("initialized.owl.carousel", function() {
        thumbs
          .find(".owl-item")
          .eq(0)
          .addClass("current");
    }).owlCarousel({
        items: 4,
        dots: true,
        nav: true,
        navText: [
            '<i class="fa fa-arrow-left" aria-hidden="true"></i>',
            '<i class="fa fa-arrow-right" aria-hidden="true"></i>'
        ],
        smartSpeed: 200,
        slideSpeed: 500,
        slideBy: 4,
        responsiveRefreshRate: 100
    })
    .on("changed.owl.carousel", syncPosition2);

    function syncPosition(el) {
        var count = el.item.count - 1;
        var current = Math.round(el.item.index - el.item.count / 2 - 0.5);

        if (current < 0) {
            current = count;
        }
        if (current > count) {
            current = 0;
        }
        thumbs
            .find(".owl-item")
            .removeClass("current")
            .eq(current)
            .addClass("current");
        var onscreen = thumbs.find(".owl-item.active").length - 1;
        var start = thumbs
        .find(".owl-item.active")
        .first()
        .index();
        var end = thumbs
        .find(".owl-item.active")
        .last()
        .index();

        if (current > end) {
                thumbs.data("owl.carousel").to(current, 100, true);
            }
            if (current < start) {
                thumbs.data("owl.carousel").to(current - onscreen, 100, true);
            }
    }

    function syncPosition2(el) {
        if (syncedSecondary) {
            var number = el.item.index;
            bigimage.data("owl.carousel").to(number, 100, true);
        }
    }

    thumbs.on("click", ".owl-item", function(e) {
        e.preventDefault();
        var number = $(this).index();
        bigimage.data("owl.carousel").to(number, 300, true);
    });
//carousel

var size_item_id = 0;
var all_sizes = document.getElementsByClassName("size-class");
var i;

for (i = 0; i < all_sizes.length; i++) {
    all_sizes[i].addEventListener("click", function() {
    size_item_id = $(this).data('id');
    document.getElementById("must-choose").hidden = true;
    })};



//add to cart
    add_to_cart = document.getElementById('add_to_cart')
    add_to_cart.addEventListener('click', () => {
        document.getElementById("must-choose").hidden = true;
        $.ajax({
            url: '/orders/cart/' + $('#add_to_cart').data('id') +'/'+ size_item_id + '/add/',
            type: 'post',
            success: function(data) {
            if (data.success) {
            $("#hb-cart-total").html(data.cart_amount);
            size_item_id = 0;
            location.reload();
            } else {document.getElementById("must-choose").hidden = false}
            },
        });
    });
//add to cart
});
