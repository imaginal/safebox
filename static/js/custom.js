
$(document).ready(function(){
  /*!
   * IE10 viewport hack for Surface/desktop Windows 8 bug
   */
  (function () {
    'use strict';
    if (navigator.userAgent.match(/IEMobile\/10\.0/)) {
      var msViewportStyle = document.createElement('style')
      msViewportStyle.appendChild(
        document.createTextNode(
          '@-ms-viewport{width:auto!important}'
        )
      )
      document.querySelector('head').appendChild(msViewportStyle)
    }
  })();

  $(".navbar ul li a[href^='#']").on('click', function(e) {

     // prevent default anchor click behavior
     e.preventDefault();

     // store hash
     var hash = this.hash;

     // animate
     $('html, body').animate({
         scrollTop: $(hash).offset().top
       }, 500, function(){

         // when done, add hash to url
         // (default click behaviour)
         window.location.hash = hash;
       });

  });

});