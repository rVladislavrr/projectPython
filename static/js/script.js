
document.querySelector('.openbtn').onclick = function () {
    document.getElementById("mySidenav").classList.add('active');
};

document.querySelector('.closebtn').onclick = function () {
    document.getElementById("mySidenav").classList.remove('active');

};

document.addEventListener('click', function (event) {
    let menu = document.getElementById("mySidenav");
    let openButton = document.querySelector('.openbtn');

    if (event.target !== openButton && !menu.contains(event.target)) {
        menu.classList.remove('active');
    }
});
window.addEventListener('scroll', function () {
    let additionalContent = document.getElementById('additional-content');
    let scrollPosition = window.scrollY;

    if (scrollPosition > 100) { // Показать дополнительный контент, когда пользователь прокрутил вниз на 100px
        additionalContent.style.opacity = 1;
    }
});

window.onscroll = function () {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById('scrollToTopButton').style.display = 'block';
    } else {
        document.getElementById('scrollToTopButton').style.display = 'none';
    }
};

document.getElementById('scrollToTopButton').onclick = function () {
    document.body.scrollTop = 0; // Для поддержки старых браузеров
    document.documentElement.scrollTop = 0; // Для современных браузеров
};

