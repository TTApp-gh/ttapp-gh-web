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
// Function to initialize the map
function initializeMap() {
	// Create the map
	const map = L.map('map').setView([0, 0], 13); // Default view

	// Add OpenStreetMap tiles
	L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
		maxZoom: 19,
		attribution: '© OpenStreetMap contributors'
	}).addTo(map);

	// Geolocation to get the user's current position
	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(
			(position) => {
				const { latitude, longitude } = position.coords;
				// Set the map view to user's location
				map.setView([latitude, longitude], 13);

				// Add a marker for the user's location
				L.marker([latitude, longitude])
					.addTo(map)
					.bindPopup('You are here!')
					.openPopup();
			},
			(error) => {
				console.error("Geolocation error:", error.message);
				alert("Unable to retrieve your location. Please check your settings.");
			}
		);
	} else {
		alert("Geolocation is not supported by your browser.");
	}
}

// Initialize the map when the page loads
window.onload = initializeMap;


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

			map = new google.maps.Map(document.getElementById('maps'), {
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

// This code here refreshes the page on click of a backward or forward button
window.addEventListener('popstate', (event) => {
    console.log('Back or forward button clicked!');
    console.log('Refreshing the page...');
    location.reload(); // Reload the page
});