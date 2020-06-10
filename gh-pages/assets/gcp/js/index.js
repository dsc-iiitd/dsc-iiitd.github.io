$(document).ready(function(){
    
    // Scroll on know more button click
    $('.know-more-button').click(function(){
        $('html, body').animate({
            scrollTop: $('.main-about').offset().top
        }, 500);
    })

    // Link click actions

    $('#close-modal').click(function(){
        $('.modal-main-data').fadeOut(300);
        $('.modal-main-app').fadeOut(300);
        $('.modal-main-ml').fadeOut(300);
        $('.modal').fadeOut(300);
        $('.tint').fadeOut(300);
    })

    $('.tint').click(function(){
        $('.modal-main-data').fadeOut(300);
        $('.modal-main-app').fadeOut(300);
        $('.modal-main-ml').fadeOut(300);
        $('.modal').fadeOut(300);
        $('.tint').fadeOut(300);
    })

    $('.data').click(function(){
        $('.modal-main-data').fadeIn(0);
        $('.tint').fadeIn(400)
        $('.modal').fadeIn(400);
    })

    $('.android').click(function(){
        $('.modal-main-app').fadeIn(0);
        $('.tint').fadeIn(400)
        $('.modal').fadeIn(400);
    })

    $('.ml').click(function(){
        $('.modal-main-ml').fadeIn(0);
        $('.tint').fadeIn(400)
        $('.modal').fadeIn(400);
    })


})
