// this is Javascript
$(document).ready(function(){
	$(".section").hide();
	$(".home").show();
	$(".navbar-toggler").on("click", function(){
		$(".navbar-collapse").show();
	});
	
	$(".navigate").on("click", function(){
		let classs = "."+$(this).attr('id');
		$(".section").hide();
		$(classs).show();
		$(".navbar-collapse").slideUp();
		
	});
	
	// Get the current page URL
	const url = window.location.href;

	// Extract the hash part
	const section = url.split("#")[1]; // Splitting manually
	if(section){
		let nav_link = $('#'+section).attr('title');
		let classs = "."+ nav_link;
		$(".section").hide();
		$(classs).show();
		//alert(classs);
	}
});

document.querySelectorAll('.faq-question').forEach((button) => {
  button.addEventListener('click', () => {
    const faqItem = button.parentElement;

    // Toggle the active class
    faqItem.classList.toggle('active');

    // Close others if needed
    document.querySelectorAll('.faq-item').forEach((item) => {
      if (item !== faqItem) {
        item.classList.remove('active');
      }
    });
  });
});


////////////////Here we placed the Geolocation code/////////////////////////////////////
let map;
let geocoder;

function initMap() {
	// Get the current location of the user and set as the center of the map
	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(function(position) {
			const currentPosition = {
				lat: position.coords.latitude,
				lng: position.coords.longitude
			};

			map = new google.maps.Map(document.getElementById('map'), {
				center: currentPosition,
				zoom: 13
			});

			new google.maps.Marker({
				map: map,
				position: currentPosition,
				title: "Your location"
			});

			/*alert(currentPosition.lat+','+currentPosition.lng);
			let cord = "'"+currentPosition.lat+","+currentPosition.lng+"'";
			document.getElementById("cord").innerHTML = cord;
			if(page_id == 1){
				setInterval('load("cord", "lib/profile.php", '+cord+')',16000);
			}else{
				setInterval('load("cord", "../lib/profile.php", '+cord+')',16000);
			}
			*/
			//alert(document.getElementById("cord").value);

		}, function() {
			handleLocationError(true, map.getCenter());
		});
	} else {
		// Browser doesn't support Geolocation
		handleLocationError(false, map.getCenter());
	}
	geocoder = new google.maps.Geocoder();
}

function handleLocationError(browserHasGeolocation, pos) {
	alert(browserHasGeolocation ? "Error: The Geolocation service failed." : "Error: Your browser doesn't support geolocation.");
}
