$(document).ready(function() {

//-----------   CAROUSEL IN SHOWCASE PAGE     -----------
    var multipleCardCarousel = document.querySelector("#carouselShowcasePage");

    console.log('ENTRY IN carouselShowcasePage');

    console.log('if (window.matchMedia("(min-width: 768px)").matches)');
    var carousel = new bootstrap.Carousel(multipleCardCarousel, {interval: false,});
    var carouselWidth = $(".carousel-inner-showcase")[0].scrollWidth;
    var cardWidth = $(".carousel-item").width() + 10;
    var scrollPosition = 0;
    var animationSpeed = 600;

    $("#carouselShowcasePage .carousel-control-next").on("click", function () {
        console.log('$("#carouselShowcasePage .carousel-control-next").on("click", function ()');
        if (scrollPosition < carouselWidth - cardWidth * 4) {
            console.log('if (scrollPosition < carouselWidth - cardWidth * 4)');
            scrollPosition += cardWidth;
            $("#carouselShowcasePage .carousel-inner-showcase").animate(
                { scrollLeft: scrollPosition },
                animationSpeed
            );
        } else {console.log('if (scrollPosition < carouselWidth - cardWidth * 4 /// else)')}
        });

    $("#carouselShowcasePage .carousel-control-prev").on("click", function () {
        console.log('$("#carouselShowcasePage .carousel-control-prev").on("click", function ()');
        if (scrollPosition > 0) {
            console.log('$("#carouselShowcasePage .carousel-control-prev").on("click", function () +++ if (scrollPosition > 0)');
            scrollPosition -= cardWidth;
            $("#carouselShowcasePage .carousel-inner-showcase").animate(
                { scrollLeft: scrollPosition },
                animationSpeed
            );
        }
        });
//-----------   CAROUSEL IN SHOWCASE PAGE     -----------
});