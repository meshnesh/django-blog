jQuery(document).ready(function ($) {  
  var cw = $('.dbimgs').width();
  $('.dbimgs').css({'height':cw+'px'});
   var trigger = $('.ck-nav-trigger'),
       wrapper = $('.ck-nav-wrapper'),
       section = $('.ck-section');
   trigger.on('click', function () {
       wrapper.toggleClass('move0');
       trigger.toggleClass('move50');
       section.toggleClass('move30');
   });
});
