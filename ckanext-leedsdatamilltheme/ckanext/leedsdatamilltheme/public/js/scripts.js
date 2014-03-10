$(function() {
	$('.pullout-sidebar-links .twitter-sidebar-link').on('click', function() {
		if( !$('.pullout-sidebar').data('closed') ) {
			if( $('.pullout .faqs').is(':visible') ) {
				$('.pullout .faqs').hide();
				$('.pullout .tweets').show();
				$('.faqs-sidebar-link').removeClass('active');
				$(this).addClass('active');
			} else {
				$('.pullout-sidebar').animate({right: "-35px" }, 1200, function() {
					$('.pullout .tweets, .pullout .faqs').hide();
					$('.twitter-sidebar-link, .faqs-sidebar-link').removeClass('active');
				}).data('closed', true);
			}
		} else {
			$('.faqs-sidebar-link').removeClass('active');
			$(this).addClass('active');
			$('.pullout .tweets, .pullout .faqs').hide();
			$('.pullout .tweets').show();
			$('.pullout-sidebar').animate({right: ($('.pullout').width() - 35)}, 1200).data('closed', false);
		}
		return false;
	});
	$('.pullout-sidebar-links .faqs-sidebar-link').on('click', function() {
		if( !$('.pullout-sidebar').data('closed') ) {
			if( $('.pullout .tweets').is(':visible') ) {
				$('.pullout .tweets').hide();
				$('.pullout .faqs').show();
				$('.twitter-sidebar-link').removeClass('active');
				$(this).addClass('active');
			} else {
				$('.pullout-sidebar').animate({right: "-35px" }, 1200, function() {
					$('.pullout .tweets, .pullout .faqs').hide();
					$('.twitter-sidebar-link, .faqs-sidebar-link').removeClass('active');
				}).data('closed', true);
			}
		} else {
			$('.twitter-sidebar-link').removeClass('active');
			$('.twitter-sidebar-link, .faqs-sidebar-link').removeClass('active');
			$(this).addClass('active');
			$('.pullout .tweets, .pullout .faqs').hide();
			$('.pullout .faqs').show();
			$('.pullout-sidebar').animate({right: ($('.pullout').width() - 35)}, 1200).data('closed', false);
		}
		return false;
	});

	$('.pullout .faqs li').addClass('closed');
	$('.pullout .faqs li').on('click', 'h3 a', function() {
		var closest = $(this).closest('li');
		if( closest.hasClass('open') ) {
			$('.pullout .faqs li').removeClass('open');
			closest.addClass('closed');
		} else {
			$('.pullout .faqs li').removeClass('open').addClass('closed');
			closest.addClass('open').removeClass('closed');
		}
		return false;
	});
	$('.section.navigation a').not('.section.navigation li:last-child a').on('click', function() {
		$('html, body').animate({
			scrollTop: $($(this).attr('href').replace('/', '')).offset().top
		}, 2000);
		return false;
	});
});
/*
 * SVGeezy.js 1.0
 *
 * Copyright 2012, Ben Howdle http://twostepmedia.co.uk
 * Released under the WTFPL license
 * http://sam.zoy.org/wtfpl/
 *
 * Date: Sun Aug 26 20:38 2012 GMT
 *  //call like so, pass in a class name that you don't want it to check and a filetype to replace .svg with
 *	svgeezy.init('nocheck', 'png');
*/
var svgeezy=function(){return{init:function(a,b){this.avoid=a||!1,this.filetype=b||"png",this.svgSupport=this.supportsSvg(),this.svgSupport||(this.images=document.getElementsByTagName("img"),this.imgL=this.images.length,this.fallbacks())},fallbacks:function(){for(;this.imgL--;)if(!this.hasClass(this.images[this.imgL],this.avoid)||!this.avoid){var a=this.images[this.imgL].getAttribute("src");if(null===a)continue;if("svg"==this.getFileExt(a)){var b=a.replace(".svg","."+this.filetype);this.images[this.imgL].setAttribute("src",b)}}},getFileExt:function(a){var b=a.split(".").pop();return-1!==b.indexOf("?")&&(b=b.split("?")[0]),b},hasClass:function(a,b){return(" "+a.className+" ").indexOf(" "+b+" ")>-1},supportsSvg:function(){return document.implementation.hasFeature("http://www.w3.org/TR/SVG11/feature#Image","1.1")}}}();
