$(document).ready(function() {

//-----------   CAROUSEL IN SHOWCASE PAGE     -----------
    var multipleCardCarousel = document.querySelector("#carouselShowcasePage");
    var carousel = new bootstrap.Carousel(multipleCardCarousel, {interval: false,});
    var carouselWidth = $(".carousel-inner-showcase")[0].scrollWidth;
    var cardWidth = $(".carousel-item").width() + 10;
    var scrollPosition = 0;
    var animationSpeed = 600;

    $("#carouselShowcasePage .carousel-control-next").on("click", function () {
        if (scrollPosition < carouselWidth - cardWidth * 4) {
            scrollPosition += cardWidth;
            $("#carouselShowcasePage .carousel-inner-showcase").animate(
                { scrollLeft: scrollPosition },
                animationSpeed
            );
        } else {}
        });

    $("#carouselShowcasePage .carousel-control-prev").on("click", function () {
        if (scrollPosition > 0) {
            scrollPosition -= cardWidth;
            $("#carouselShowcasePage .carousel-inner-showcase").animate(
                { scrollLeft: scrollPosition },
                animationSpeed
            );
        }
        });
//-----------   CAROUSEL IN SHOWCASE PAGE     -----------

    var modal_sizes_windows = document.getElementsByClassName("choose-size-showcase");
    var i;
    for (i = 0; i < modal_sizes_windows.length; i++) {
        modal_sizes_windows[i].addEventListener("click", function() {
            $.ajax({
                url: '/category/' + $(this).data('id') +'/sizes/',
                type: 'post',
                success: function(data) {
                if (data.success) {
                $('#modal-sizes').html(data.html);
                }
                },
            });
    })};

});