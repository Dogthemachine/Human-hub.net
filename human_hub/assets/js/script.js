$(document).ready(function() {

function get_loc_lang() {
    return window.location.toString().substr(window.location.toString().indexOf(window.location.host)
        + window.location.host.toString().length + 1,2);
};

loclang = get_loc_lang()

//-----------   FOOTER BUTTONS     -----------
    if (window.matchMedia("(max-width: 450px)").matches) {
        $('.btn-footer').removeClass('btn-sm');
        $('.btn-footer').removeClass('mx-3');
        $('.btn-footer').addClass('btn-footer-xs');
        $('.btn-footer').addClass('mx-2');
        $('.btn-footer').addClass('btn-xs');
        $('.btn-footer').addClass('btn-xs');
        $('.btn-footer-xs').removeClass('btn-footer');
    };

    if (window.matchMedia("(min-width: 980px)").matches) {
        $('.btn-footer').removeClass('mx-3');
        $('.btn-footer').addClass('mx-5');
    };

//-----------   FOOTER BUTTONS     -----------

//-----------   MAKE ORDER BUTTONS     -----------
    const cart = document.getElementById("show-cart-modal");
    cart.addEventListener('click', showCarModal);

    const choose_size = document.getElementsByClassName("size_button_font");
    for (var i = 0; i< choose_size.length; i++) {
        choose_size[i].onclick = addSizeToCart
    };

    function showCarModal() {
        $.ajax({
            url: '/' + loclang + '/orders/cart/',
            type: 'get',
            success: function(data) {
                $('#hb-cart-content').html(data.html);
            }
        });
    };

    function addSizeToCart() {
        $.ajax({
            url: '/orders/cart/',
            type: 'get',
            success: function(data) {
                $('#hb-cart-content').html(data.html);
            }
        });
    };
//-----------   MAKE ORDER BUTTONS     -----------

//-----------   MAKE ORDER MODAL WINDOW     -----------
    const makeorder = document.getElementById("show-order-modal");
    makeorder.addEventListener('click', showOrderModal);

    function showOrderModal() {
        $.ajax({
            url: '/' + loclang + '/orders/order',
            type: 'get',
            success: makeorderSuccess
        });
    };

    function makeorderSuccess(data) {
        $('#hb-order-content').html(data.html);

        const worldwide = document.getElementById("ordr-deliv-worldwide");
        const novpostobranch = document.getElementById("ordr-deliv-novpostobranch");
        const novpostodoor = document.getElementById("ordr-deliv-novpostodoor");
        const urkpostobranch = document.getElementById("ordr-deliv-urkpostobranch");
        const urkpostodoor = document.getElementById("ordr-deliv-urkpostodoor");
        const justintobranch = document.getElementById("ordr-deliv-justintobranch");

        const WorldWide = document.getElementById("collapseDeliveryWorldWide");
        const NovaPoshtaToBranch = document.getElementById("collapseDeliveryNovaPoshtaToBranch");
        const NovaPoshtaToDoor = document.getElementById("collapseDeliveryNovaPoshtaToDoor");
        const UkrposhtaToBranch = document.getElementById("collapseDeliveryUkrposhtaToBranch");
        const UkrposhtaToDoor = document.getElementById("collapseDeliveryUkrposhtaToDoor");
        const JustinToBranch = document.getElementById("collapseDeliveryJustinToBranch");

        const VisaMaster = document.getElementById("ordr-pay-visa-mstrcrd");
        const ApplePay = document.getElementById("ordr-pay-applepay");
        const Googlepay = document.getElementById("ordr-pay-googlepay");
        const Paypal = document.getElementById("ordr-pay-paypal");
        const ByCard = document.getElementById("ordr-pay-bycard");
        const CashOnDeliv = document.getElementById("ordr-pay-cash-on-del");


        NovaPoshtaToBranch.style.display = 'none';
        NovaPoshtaToDoor.style.display = 'none';
        UkrposhtaToBranch.style.display = 'none';
        JustinToBranch.style.display = 'none';
        UkrposhtaToDoor.style.display = 'none';
        WorldWide.style.display = 'none';

        VisaMaster.addEventListener('click', () => {
            if (VisaMaster.checked) {
                ApplePay.checked = false;
                Googlepay.checked = false;
                Paypal.checked = false;
                ByCard.checked = false;
                CashOnDeliv.checked = false;
            };
        });

        ApplePay.addEventListener('click', () => {
            if (ApplePay.checked) {
                VisaMaster.checked = false;
                Googlepay.checked = false;
                Paypal.checked = false;
                ByCard.checked = false;
                CashOnDeliv.checked = false;
            };
        });


        Googlepay.addEventListener('click', () => {
            if (Googlepay.checked) {
                VisaMaster.checked = false;
                ApplePay.checked = false;
                Paypal.checked = false;
                ByCard.checked = false;
                CashOnDeliv.checked = false;
            };
        });

        Paypal.addEventListener('click', () => {
            if (Paypal.checked) {
                VisaMaster.checked = false;
                ApplePay.checked = false;
                Googlepay.checked = false;
                ByCard.checked = false;
                CashOnDeliv.checked = false;
            };
        });

        ByCard.addEventListener('click', () => {
            if (ByCard.checked) {
                VisaMaster.checked = false;
                ApplePay.checked = false;
                Googlepay.checked = false;
                Paypal.checked = false;
                CashOnDeliv.checked = false;
            };
        });

        CashOnDeliv.addEventListener('click', () => {
            if (CashOnDeliv.checked) {
                VisaMaster.checked = false;
                ApplePay.checked = false;
                Googlepay.checked = false;
                Paypal.checked = false;
                ByCard.checked = false;
            };
        });

        worldwide.addEventListener('click', () => {
            if (worldwide.checked) {
                NovaPoshtaToBranch.style.display = 'none';
                NovaPoshtaToDoor.style.display = 'none';
                UkrposhtaToBranch.style.display = 'none';
                JustinToBranch.style.display = 'none';
                UkrposhtaToDoor.style.display = 'none';
                WorldWide.style.display = 'block';
                novpostobranch.checked = false;
                novpostodoor.checked = false;
                urkpostobranch.checked = false;
                urkpostodoor.checked = false;
                justintobranch.checked = false;
                } else {
            WorldWide.style.display = 'none';
            };
        });
        novpostobranch.addEventListener('click', () => {
            if (novpostobranch.checked) {
                WorldWide.style.display = 'none';
                NovaPoshtaToDoor.style.display = 'none';
                UkrposhtaToBranch.style.display = 'none';
                JustinToBranch.style.display = 'none';
                UkrposhtaToDoor.style.display = 'none';
                NovaPoshtaToBranch.style.display = 'block';
                worldwide.checked = false;
                novpostodoor.checked = false;
                urkpostobranch.checked = false;
                urkpostodoor.checked = false;
                justintobranch.checked = false;
                } else {
            NovaPoshtaToBranch.style.display = 'none';
            };
        });
        novpostodoor.addEventListener('click', () => {
            WorldWide.style.display = 'none';
            NovaPoshtaToBranch.style.display = 'none';
            UkrposhtaToBranch.style.display = 'none';
            JustinToBranch.style.display = 'none';
            UkrposhtaToDoor.style.display = 'none';
            NovaPoshtaToDoor.style.display = 'block';
            if (novpostodoor.checked) {
                WorldWide.style.display = 'none';
                NovaPoshtaToBranch.style.display = 'none';
                UkrposhtaToBranch.style.display = 'none';
                JustinToBranch.style.display = 'none';
                UkrposhtaToDoor.style.display = 'none';
                NovaPoshtaToDoor.style.display = 'block';
                novpostobranch.checked = false;
                worldwide.checked = false;
                urkpostobranch.checked = false;
                urkpostodoor.checked = false;
                justintobranch.checked = false;
                } else {
            NovaPoshtaToDoor.style.display = 'none';
            };
        });
        urkpostobranch.addEventListener('click', () => {
            if (urkpostobranch.checked) {
                WorldWide.style.display = 'none';
                NovaPoshtaToBranch.style.display = 'none';
                NovaPoshtaToDoor.style.display = 'none';
                JustinToBranch.style.display = 'none';
                UkrposhtaToDoor.style.display = 'none';
                UkrposhtaToBranch.style.display = 'block';
                novpostobranch.checked = false;
                novpostodoor.checked = false;
                worldwide.checked = false;
                urkpostodoor.checked = false;
                justintobranch.checked = false;
                } else {
            UkrposhtaToBranch.style.display = 'none';
            };
        });
        urkpostodoor.addEventListener('click', () => {
            if (urkpostodoor.checked) {
                WorldWide.style.display = 'none';
                NovaPoshtaToBranch.style.display = 'none';
                NovaPoshtaToDoor.style.display = 'none';
                UkrposhtaToBranch.style.display = 'none';
                JustinToBranch.style.display = 'none';
                UkrposhtaToDoor.style.display = 'block';
                novpostobranch.checked = false;
                novpostodoor.checked = false;
                urkpostobranch.checked = false;
                worldwide.checked = false;
                justintobranch.checked = false;
                } else {
            UkrposhtaToDoor.style.display = 'none';
            };
        });
        justintobranch.addEventListener('click', () => {
            if (justintobranch.checked) {
                WorldWide.style.display = 'none';
                NovaPoshtaToBranch.style.display = 'none';
                NovaPoshtaToDoor.style.display = 'none';
                UkrposhtaToBranch.style.display = 'none';
                UkrposhtaToDoor.style.display = 'none';
                JustinToBranch.style.display = 'block';
                novpostobranch.checked = false;
                novpostodoor.checked = false;
                urkpostobranch.checked = false;
                urkpostodoor.checked = false;
                worldwide.checked = false;
                } else {
            JustinToBranch.style.display = 'none';
            };
        });
   };
//-----------   MAKE ORDER MODAL WINDOW     -----------

$('.lang li').click(function () {
    var lang = this.id;
    var loc = window.location.toString().substring( 0, window.location.toString().indexOf(window.location.host)
        + window.location.host.toString().length + 1) + lang
        + window.location.toString().substring(window.location.toString().indexOf(window.location.host)
        + window.location.host.toString().length + 3);
    window.location = loc;
});


$('.val li').click(function () {
    var val = this.id;
    event.preventDefault();
      $.ajax({
          url: '/currency/' + val + '/',
          type: 'post',
          success: function() {
              location.reload();
          },
          error: function() {
          }
      });
});

});