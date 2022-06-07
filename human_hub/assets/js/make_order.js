$(document).ready(function() {
//-----------   CHECKOUT     -----------
    const checkout = document.getElementById("pop-order-checkout");
    checkout.addEventListener('click', () => {
        if (worldwide.checked) {
            NovaPoshtaToBranch.parentElement.removeChild(NovaPoshtaToBranch);
            NovaPoshtaToDoor.parentElement.removeChild(NovaPoshtaToDoor);
            UkrposhtaToBranch.parentElement.removeChild(UkrposhtaToBranch);
            UkrposhtaToDoor.parentElement.removeChild(UkrposhtaToDoor);
            JustinToBranch.parentElement.removeChild(JustinToBranch);
        };
        if (novpostobranch.checked) {
            WorldWide.parentElement.removeChild(WorldWide);
            NovaPoshtaToDoor.parentElement.removeChild(NovaPoshtaToDoor);
            UkrposhtaToBranch.parentElement.removeChild(UkrposhtaToBranch);
            UkrposhtaToDoor.parentElement.removeChild(UkrposhtaToDoor);
            JustinToBranch.parentElement.removeChild(JustinToBranch);
        };
        if (novpostodoor.checked) {
            WorldWide.parentElement.removeChild(WorldWide);
            NovaPoshtaToBranch.parentElement.removeChild(NovaPoshtaToBranch);
            UkrposhtaToBranch.parentElement.removeChild(UkrposhtaToBranch);
            UkrposhtaToDoor.parentElement.removeChild(UkrposhtaToDoor);
            JustinToBranch.parentElement.removeChild(JustinToBranch);
        };
        if (urkpostobranch.checked) {
            WorldWide.parentElement.removeChild(WorldWide);
            NovaPoshtaToBranch.parentElement.removeChild(NovaPoshtaToBranch);
            NovaPoshtaToDoor.parentElement.removeChild(NovaPoshtaToDoor);
            UkrposhtaToDoor.parentElement.removeChild(UkrposhtaToDoor);
            JustinToBranch.parentElement.removeChild(JustinToBranch);
        };
        if (urkpostodoor.checked) {
            WorldWide.parentElement.removeChild(WorldWide);
            NovaPoshtaToBranch.parentElement.removeChild(NovaPoshtaToBranch);
            NovaPoshtaToDoor.parentElement.removeChild(NovaPoshtaToDoor);
            UkrposhtaToBranch.parentElement.removeChild(UkrposhtaToBranch);
            JustinToBranch.parentElement.removeChild(JustinToBranch);
        };
        if (justintobranch.checked) {
            WorldWide.parentElement.removeChild(WorldWide);
            NovaPoshtaToBranch.parentElement.removeChild(NovaPoshtaToBranch);
            NovaPoshtaToDoor.parentElement.removeChild(NovaPoshtaToDoor);
            UkrposhtaToBranch.parentElement.removeChild(UkrposhtaToBranch);
            UkrposhtaToDoor.parentElement.removeChild(UkrposhtaToDoor);
        };
    });
//-----------   CHECKOUT     -----------
});