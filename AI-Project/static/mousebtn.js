document.addEventListener('DOMContentLoaded', addListen, false);

function addListen(){
    document.body.addEventListener("mousemove", hoverMouse($('.accessory')));
    var time = new Date().getHours();
    console.log(time);
    if(time >= 6 && time <= 13) {
      $('#greeting').text("Good morning, welcome ");
    } else if (time > 13 && time <= 20) {
      $('#greeting').text("Good afternoon, welcome ");
    } else {
      $('#greeting').text("Good night, welcome ");
    }
  }



var hoverMouse = function($el) {
  $el.each(function() {
    var $self = $(this);
    var hover = false;
    var offsetHoverMax = $self.attr("offset-hover-max") || 0.7;
    var offsetHoverMin = $self.attr("offset-hover-min") || 0.5;

    var attachEventsListener = function() {
        
      $(window).on("mousemove", function(e) {
        //
        var hoverArea = hover ? offsetHoverMax : offsetHoverMin;

        // cursor
        var cursor = {
          x: e.clientX,
          y: e.clientY - $(window).scrollTop()
        };

        // size
        var width = $self.outerWidth();
        var height = $self.outerHeight();

        // position
        var offset = $self.offset();
        var elPos = {
          x: offset.left + width / 2,
          y: offset.top + height / 2
        };

        // comparaison
        var x = cursor.x - elPos.x;
        var y = cursor.y - elPos.y;

        // dist
        var dist = Math.sqrt(x * x + y * y);

        // mutex hover
        var mutHover = false;

        // anim
        if (dist < width * hoverArea) {
          mutHover = true;
          if (!hover) {
            hover = true;
          }
          onHover(x, y);
        }

        // reset
        if (!mutHover && hover) {
          onLeave();
          hover = false;
        }
      });
    };

    var onHover = function(x, y) {
      TweenMax.to($self, 0.2, {
        x: x * 0.15,
        y: y * 0.15,
        //scale: .9,
        //rotation: x * 0.05,
        ease: Power2.easeOut
      });
    };
    var onLeave = function() {
      TweenMax.to($self, 0.5, {
        x: 0,
        y: 0,
        scale: 1,
        rotation: 0,
        ease: Elastic.easeOut.config(0.9, 0.4)
      });
    };

    attachEventsListener();
  });
};

