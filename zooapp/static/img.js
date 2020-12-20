function swapImages(){
    var $active = $('#images .active');
    var $next = ($('#images .active').next().length > 0) ? $('#images .active').next() : $('#images img:first');
    $active.fadeOut(function(){
      $active.removeClass('active');
      $next.fadeIn().addClass('active');
    });
  }