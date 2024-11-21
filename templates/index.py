<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
	<link rel="icon" href="{{ url_for('static', filename='images/logo.jpeg') }}">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/css/bootstrap.min.css">
	<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet" />
	<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>

<!-- Navbar -->
<nav class="navbar navbar-expand-lg navbar-dark bg-black fixed-top">
    <div class="container">
        <a id="home" class="navbar-brand navigate" href="/"><img src="{{ url_for('static', filename='images/logo.jpeg') }}" class="img_logo" /> {{ app_name }}</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto">
				<li id="home" class="nav-item navigate">
                    <a class="nav-link" href="#index">Home</a>
                </li>
				<li id="drive" class="nav-item navigate">
                    <a class="nav-link" href="#driver">Drive & Deliver</a>
                </li>
                <li id="ride" class="nav-item navigate">
                    <a class="nav-link" href="#ride">Ride</a>
                </li>
				<li id="eat" class="nav-item navigate">
                    <a class="nav-link" href="#eat">{{ app_name }} Eats</a>
                </li>
				<li id="business" class="nav-item navigate">
                    <a class="nav-link" href="#bussiness">{{ app_name }} for Business</a>
                </li>
				<li id="account" class="nav-item navigate">
                    <a class="nav-link" href="#account">Manage Account</a>
                </li>
                <li id="help" class="nav-item navigate">
                    <a class="nav-link" href="#help">Help</a>
                </li>
                <li id="login" class="nav-item navigate">
                    <a class="nav-link" href="#login">Log in</a>
                </li>
                <li id="signup" class="nav-item navigate">
                    <a class="nav-link btn btn-dark text-light" href="#signup">Sign up</a>
                </li>
            </ul>
        </div>
    </div>
</nav>
<br />
<br />

<!--------- The Index / Home Page is Identified and starts here id=drive -------------->
<!--------- The Index / Home Page is Identified and starts here id=drive -------------->

<!-- Hero Section -->
<section id="index" class="section home hero-section" title="home">
    <div class="container">
        <h1>Your ride, on demand</h1>
        <p>Get a reliable ride in minutes with the {{ app_name }}.</p>
        <a href="#" class="btn btn-light">Get Started</a>
    </div>
</section>

<!-- Ride/Package Section -->
<section class="section home ride-package-section">
    <div class="container">
        <div class="row align-items-center">
            <!-- Left Side: Form -->
            <div class="col-md-6">
                <h2>Go anywhere with {{ app_name }}</h2>
                <!-- Tabs for Ride and Package -->
                <ul class="nav nav-tabs mt-4" id="ridePackageTab" role="tablist">
                    <li class="nav-item" role="presentation">
                        <button class="nav-link active" id="ride-tab" data-bs-toggle="tab" data-bs-target="#ride" type="button" role="tab" aria-controls="ride" aria-selected="true">
                            <span class="me-2">&#128663;</span> Ride
                        </button>
                    </li>
                    <li class="nav-item" role="presentation">
                        <button class="nav-link" id="package-tab" data-bs-toggle="tab" data-bs-target="#package" type="button" role="tab" aria-controls="package" aria-selected="false">
                            <span class="me-2">&#128230;</span> Package
                        </button>
                    </li>
                </ul>

                <!-- Tab Content -->
                <div class="tab-content mt-3" id="ridePackageTabContent">
                    <!-- Ride Tab Content -->
                    <div class="tab-pane fade show active" id="ride" role="tabpanel" aria-labelledby="ride-tab">
                        <form class="mt-3">
                            <div class="mb-3">
                                <input type="text" class="form-control" placeholder="Pickup location">
                            </div>
                            <div class="mb-3">
                                <input type="text" class="form-control" placeholder="Dropoff location">
                            </div>
                            <div class="d-flex gap-2 mb-3">
                                <button type="button" class="btn btn-light border w-50">Today</button>
                                <button type="button" class="btn btn-light border w-50">Now</button>
                            </div>
                            <button type="submit" class="btn btn-dark w-100">See prices</button>
                        </form>
                    </div>

                    <!-- Package Tab Content -->
                    <div class="tab-pane fade" id="package" role="tabpanel" aria-labelledby="package-tab">
                        <form class="mt-3">
                            <div class="mb-3">
                                <input type="text" class="form-control" placeholder="Pickup location">
                            </div>
                            <div class="mb-3">
                                <input type="text" class="form-control" placeholder="Dropoff location">
                            </div>
                            <div class="d-flex gap-2 mb-3">
                                <button type="button" class="btn btn-light border w-50">Today</button>
                                <button type="button" class="btn btn-light border w-50">Now</button>
                            </div>
                            <button type="submit" class="btn btn-dark w-100">See prices</button>
                        </form>
                    </div>
                </div>
            </div>

            <!-- Right Side: Map -->
            <div class="col-md-6">
                <div class="map-placeholder" style="ckground-color: #e0e0e0; width: 100%; height: 400px; border-radius: 8px; display: flex; align-items: center; justify-content: center;">
                    <p>Map Placeholder</p>
					<section id="map"></section>
                </div>
            </div>
        </div>
    </div>
</section>
<section id="map"></section>

<!-- Suggestions Section -->
<section class="section home suggestions-section py-5">
    <div class="container">
        <h2 class="mb-4">Suggestions</h2>
        <div class="row">
            <!-- Suggestion Card 1 -->
            <div class="col-md-4">
                <div class="card shadow-sm p-4">
                    <h4 class="card-title">Ride</h4>
                    <p class="card-text">Go anywhere with Uber. Request a ride, hop in, and go.</p>
                    <img src="{{ url_for('static', filename='images/car.PNG') }}" alt="Ride" class="img-fluid mb-3">
                    <a href="#" class="btn btn-light border">Details</a>
                </div>
            </div>
            <!-- Suggestion Card 2 -->
            <div class="col-md-4">
                <div class="card shadow-sm p-4">
                    <h4 class="card-title">Package</h4>
                    <p class="card-text">{{ app_name }} Connect makes same-day delivery easier than ever.</p>
                    <img src="{{ url_for('static', filename='images/package.PNG') }}" alt="Package" class="img-fluid mb-3">
                    <a href="#" class="btn btn-light border">Details</a>
                </div>
            </div>
            <!-- Suggestion Card 3 -->
            <div class="col-md-4">
                <div class="card shadow-sm p-4">
                    <h4 class="card-title">Reserve</h4>
                    <p class="card-text">Reserve your ride in advance so you can relax on the day of your trip.</p>
                    <img src="{{ url_for('static', filename='images/reserve.PNG') }}" alt="Reserve" class="img-fluid mb-3">
                    <a href="#" class="btn btn-light border">Details</a>
                </div>
            </div>
        </div>
    </div>
</section>


<!-- Get Started Section -->
<section class="section home get-started-section py-5">
    <div class="container">
        <div class="row align-items-center">
            <!-- Image Column -->
            <div class="col-md-6">
                <img src="{{ url_for('static', filename='images/drive.PNG') }}" alt="Driver" class="img-fluid rounded">
            </div>
            <!-- Text Column -->
            <div class="col-md-6">
                <h2>Drive when you want, make what you need</h2>
                <p>Make money on your schedule with deliveries or rides—or both. You can use your own car or choose a rental through {{ app_name }}.</p>
                <a href="#" class="btn btn-dark mb-3">Get started</a>
                <p>Already have an account? <a href="#">Sign in</a></p>
            </div>
        </div>
    </div>
</section>


<!-- Uber for Business Section -->
<section class="section home uber-business-section py-5">
    <div class="container">
        <div class="row align-items-center">
            <!-- Text Column -->
            <div class="col-md-6">
                <h2>The {{ app_name }} you know, reimagined for business</h2>
                <p>Uber for Business is a platform for managing global rides and meals, and local deliveries, for companies of any size.</p>
                <a href="#" class="btn btn-dark mb-3">Get started</a>
                <a href="#" class="ml-3">Check out our solutions</a>
            </div>
            <!-- Image Column -->
            <div class="col-md-6">
                <img src="{{ url_for('static', filename='images/business2.PNG') }}" alt="Business Scene" class="img-fluid rounded">
            </div>
        </div>
    </div>
</section>



<!-- Services Section -->
<section class="section home service-section">
    <div class="container">
        <h2>Our Services</h2>
        <p>Choose from a range of services to suit your needs.</p>
        <div class="row mt-4">
            <div class="col-md-4">
                <div class="service-icon mb-3">&#128663;</div>
                <h5>Ride</h5>
                <p>Get from point A to B with ease using our reliable ride service.</p>
            </div>
            <div class="col-md-4">
                <div class="service-icon mb-3">&#127758;</div>
                <h5>Uber Eats</h5>
                <p>Order food from your favorite restaurants, delivered straight to your door.</p>
            </div>
            <div class="col-md-4">
                <div class="service-icon mb-3">&#128679;</div>
                <h5>Freight</h5>
                <p>Efficient freight shipping solutions for businesses of all sizes.</p>
            </div>
        </div>
    </div>
</section>

<!-- Testimonials Section -->
<section class="section home testimonial-section bg-light">
    <div class="container">
        <h2>What Our Customers Say</h2>
        <p>See why people love using {{ app_name }}.</p>
        <div class="row mt-4">
            <div class="col-md-4">
                <div class="card">
                    <div class="card-body">
                        <p>"Uber has made my life so much easier. I can get a ride anytime, anywhere!"</p>
                        <h6>- John Doe</h6>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card">
                    <div class="card-body">
                        <p>"Quick, easy, and reliable! Uber Eats is my go-to for food delivery."</p>
                        <h6>- Sarah Lee</h6>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card">
                    <div class="card-body">
                        <p>"The best option for safe and affordable transportation."</p>
                        <h6>- Mike Johnson</h6>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Pricing Table Section -->
<section class="section home pricing-section">
    <div class="container">
        <h2>Pricing Plans</h2>
        <p>Choose a plan that fits your budget.</p>
        <div class="row mt-4">
            <div class="col-md-4">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">Basic</h5>
                        <h6>$10 / ride</h6>
                        <p>Standard service, available for all users.</p>
                        <ul>
                            <li>Access to basic rides</li>
                            <li>Standard vehicles</li>
                            <li>Free cancellations</li>
                        </ul>
                        <a href="#" class="btn btn-dark">Select Plan</a>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">Premium</h5>
                        <h6>$20 / ride</h6>
                        <p>Enjoy premium features with every ride.</p>
                        <ul>
                            <li>Luxury vehicles</li>
                            <li>Priority pickups</li>
                            <li>Free cancellations</li>
                        </ul>
                        <a href="#" class="btn btn-dark">Select Plan</a>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">Business</h5>
                        <h6>Custom pricing</h6>
                        <p>Flexible options for corporate customers.</p>
                        <ul>
                            <li>Flexible routes</li>
                            <li>Monthly billing</li>
                            <li>24/7 support</li>
                        </ul>
                        <a href="#" class="btn btn-dark">Contact Us</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>


<!-- Download the App Section -->
<section class="section home download-app-section py-5" style="background-color: #f8f9fa;">
    <div class="container text-center">
        <h2 class="mb-4">It's easier in the apps</h2>
        <div class="row justify-content-center">
            <!-- Uber App Card -->
            <div class="col-md-4">
                <div class="card p-3 mb-4 shadow-sm">
                    <div class="card-body text-center">
                        <img src="{{ url_for('static', filename='images/qr_code.jpeg') }}" alt="Uber App QR Code" class="img-fluid mb-3">
                        <h5 class="card-title">Download the {{ app_name }}</h5>
                        <p class="card-text text-muted">Scan to download</p>
                    </div>
                </div>
            </div>
            <!-- Driver App Card -->
            <div class="col-md-4">
                <div class="card p-3 mb-4 shadow-sm">
                    <div class="card-body text-center">
                        <img src="{{ url_for('static', filename='images/qr_code.jpeg') }}" alt="Driver App QR Code" class="img-fluid mb-3">
                        <h5 class="card-title">Download the Driver app</h5>
                        <p class="card-text text-muted">Scan to download</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
<!--------------------------- The Index / Home Page Ends Here ------------------------>
<!--------------------------- The Index / Home Page Ends Here ------------------------>













<!--------- The Drive Page is Identified and starts here id=drive -------------->
<!--------- The Drive Page is Identified and starts here id=drive -------------->
<section id="driver" class="section drive drive-section" title="drive">
  <div class="drive-container">
    <div class="drive-text">
      <h1>Opportunity is everywhere</h1>
      <p>
        Make the most of your time on the road on the platform with the largest network of active riders.
      </p>
      <div class="drive-buttons">
        <a href="#" class="btn-primary">Sign up to drive</a>
        <a href="#" class="btn-secondary">Already have an account? Sign in</a>
      </div>
    </div>
    <div class="drive-image">
      <img src="{{ url_for('static', filename='images/drive1_img.PNG') }}" alt="Driver Illustration">
    </div>
  </div>
</section>

<section class="section drive earn-section">
  <div class="earn-container">
    <div class="earn-header">
      <h2>Make money when you want</h2>
    </div>
    <div class="earn-image">
      <img src="{{ url_for('static', filename='images/driver-passenger.PNG') }}" alt="Driver and Passenger Illustration">
    </div>
    <div class="earn-features">
      <div class="feature-item">
        <span class="feature-icon">📅</span>
        <h3>Set your own schedule</h3>
        <p>
          You’re the boss. You can drive with the Uber app day or night. Fit driving around your life, not the other way around.
        </p>
      </div>
      <div class="feature-item">
        <span class="feature-icon">💰</span>
        <h3>Make money on your own terms</h3>
        <p>
          The more you drive, the more money you can make. When demand is higher than normal, you can make even more.
        </p>
      </div>
      <div class="feature-item">
        <span class="feature-icon">📍</span>
        <h3>Let the app lead the way</h3>
        <p>
          Just tap and go. You get turn-by-turn directions, suggestions to help you make more money, and 24/7 support.
        </p>
      </div>
    </div>
  </div>
</section>

<section class="section drive get-started">
  <div class="get-started-container">
    <h2>Get started</h2>
    <p class="subheading">Hit the road</p>
    <div class="steps">
      <div class="step">
        <span class="step-icon">⭐</span>
        <h3>Sign up online</h3>
        <p>
          You’ll need a valid email address and cell phone number to sign up. Requirements vary by region, so we’ll show you what’s needed for your city.
        </p>
        <a href="#">Sign up online</a>
      </div>
      <div class="step">
        <span class="step-icon">📋</span>
        <h3>Check driving requirements</h3>
        <p>
          Most people are eligible to drive with Uber. Here’s what you need to know if you’re driving in Lagos or Abuja.
        </p>
        <a href="#">Requirements</a>
      </div>
      <div class="step">
        <span class="step-icon">✔️</span>
        <h3>Get a vehicle</h3>
        <p>
          You can sign up even if you don’t have a car that meets the vehicle requirements in Nigeria right now.
        </p>
        <a href="#">Vehicle requirements</a>
      </div>
    </div>
  </div>
</section>

<section class="section drive driver-extras">
  <div class="driver-extras-container">
    <h2>Driver extras</h2>
    <p class="subheading">What we do for you in Nigeria</p>
    <div class="extras">
      <div class="extra">
        <div class="icon-container">
          <img src="{{ url_for('static', filename='images/get_support.PNG') }}" alt="Get support icon" />
        </div>
        <h3>Get support</h3>
        <p>
          Let’s make every {{ app_name }} trip hassle-free. Our support pages can help you set up your account, get started with the app, adjust fares, and much more.
        </p>
        <a href="#">Get help</a>
      </div>
      <div class="extra">
        <div class="icon-container">
          <img src="{{ url_for('static', filename='images/contact_us.PNG') }}" alt="Contact us icon" />
        </div>
        <h3>Contact us</h3>
        <p>
          Got questions? Get answers. Enjoy personal support at an {{ app_name }} Greenlight Hub in Lagos or Abuja.
        </p>
        <a href="#">Contact us</a>
      </div>
      <div class="extra">
        <div class="icon-container">
          <img src="{{ url_for('static', filename='images/drive_safe.PNG') }}" alt="Drive safely icon" />
        </div>
        <h3>Drive safely</h3>
        <p>
          The {{ app_name }} is full of features that help you stay safe and confident before, during, and after every trip. And if you need help, {{ app_name }} gives you 24/7 support.
        </p>
        <a href="#">Read more about safety</a>
      </div>
    </div>
  </div>
</section>

<section class="section drive driver-app">
  <div class="driver-app-container">
    <div class="text-content">
      <h2>The Driver app</h2>
      <p>
        Easy to use and reliable, the app was built for drivers, with drivers.
      </p>
      <a href="#" class="learn-more">Learn more</a>
    </div>
    <div class="image-content">
      <img src="{{ url_for('static', filename='images/driver_app_image.PNG') }}" alt="Driver app interface on mobile" />
    </div>
  </div>
</section>

<section class="section drive faq-section">
  <div class="faq-container">
    <h2>Top questions from drivers</h2>
    <div class="faq">
      <div class="faq-item">
        <button class="faq-question">
          Can I drive with Uber in my city? <span class="arrow">▼</span>
        </button>
        <div class="faq-answer">
          <p>
            Yes, {{ app_name }} operates in most cities. Check our list of supported cities to confirm.
          </p>
        </div>
      </div>
      <div class="faq-item">
        <button class="faq-question">
          What are the requirements to drive with {{ app_name }}? <span class="arrow">▼</span>
        </button>
        <div class="faq-answer">
          <p>
            Requirements include a valid driver’s license, an eligible vehicle, and necessary documentation.
          </p>
        </div>
      </div>
      <div class="faq-item">
        <button class="faq-question">
          Is {{ app_name }} safe? <span class="arrow">▼</span>
        </button>
        <div class="faq-answer">
          <p>
            {{ app_name }} prioritizes safety with in-app features like GPS tracking and 24/7 support.
          </p>
        </div>
      </div>
      <div class="faq-item">
        <button class="faq-question">
          Do I need my own car? <span class="arrow">▼</span>
        </button>
        <div class="faq-answer">
          <p>
            Not necessarily. {{ app_name }} partners with rental and leasing companies if you don't own a car.
          </p>
        </div>
      </div>
      <div class="faq-item">
        <button class="faq-question">
          How much can drivers make with {{ app_name }}? <span class="arrow">▼</span>
        </button>
        <div class="faq-answer">
          <p>
            Earnings depend on location, demand, and driving hours. Check our earnings calculator.
          </p>
        </div>
      </div>
      <div class="faq-item">
        <button class="faq-question">
          How do I earn with surge? <span class="arrow">▼</span>
        </button>
        <div class="faq-answer">
          <p>
            During high-demand periods, surge pricing increases fares, boosting your earnings.
          </p>
        </div>
      </div>
      <div class="faq-item">
        <button class="faq-question">
          What is Partner Protection Insurance with AXA Mansard? <span class="arrow">▼</span>
        </button>
        <div class="faq-answer">
          <p>
            It provides insurance coverage for injuries, accidents, and other incidents while driving with {{ app_name }}.
          </p>
        </div>
      </div>
    </div>
  </div>
</section>
<!--------------------------- The Drive Page Ends Here ------------------------>
<!--------------------------- The Drive Page Ends Here ------------------------>






<!-- Footer -->
<footer class="footer">
  <div class="container">
    <div class="footer-top">
      <h3>{{ app_name }}</h3>
      <a href="#" class="help-link">Visit Help Center</a>
    </div>
    <div class="footer-columns">
      <div class="footer-column">
        <h4>Company</h4>
        <ul>
          <li><a href="#">About us</a></li>
          <li><a href="#">Our offerings</a></li>
          <li><a href="#">Newsroom</a></li>
          <li><a href="#">Investors</a></li>
          <li><a href="#">Blog</a></li>
          <li><a href="#">Careers</a></li>
        </ul>
      </div>
      <div class="footer-column">
        <h4>Products</h4>
        <ul>
          <li><a href="#">Ride</a></li>
          <li><a href="#">Drive</a></li>
          <li><a href="#">Deliver</a></li>
          <li><a href="#">TTApp Freight</a></li>
          <li><a href="#">Gift cards</a></li>
        </ul>
      </div>
      <div class="footer-column">
        <h4>Global Citizenship</h4>
        <ul>
          <li><a href="#">Safety</a></li>
          <li><a href="#">Diversity and Inclusion</a></li>
          <li><a href="#">Sustainability</a></li>
        </ul>
      </div>
      <div class="footer-column">
        <h4>Travel</h4>
        <ul>
          <li><a href="#">Reserve</a></li>
          <li><a href="#">Cities</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <div class="social-icons">
        <a href="#"><i class="fab fa-facebook"></i></a>
        <a href="#"><i class="fab fa-twitter"></i></a>
        <a href="#"><i class="fab fa-youtube"></i></a>
        <a href="#"><i class="fab fa-linkedin"></i></a>
        <a href="#"><i class="fab fa-instagram"></i></a>
      </div>
      <div class="app-store-links">
        <a href="#"><img src="{{ url_for('static', filename='images/playstore_1.png') }}" alt="Google Play"></a>
        <a href="#"><img src="{{ url_for('static', filename='images/apple1.png') }}" alt="App Store"></a>
      </div>
      <div class="location-settings">
        <span>🌍 English</span>
        <span>📍 Accra</span>
      </div>
    </div>
    <div class="footer-legal">
      <p>&copy; 2024 {{ app_name }} Technologies Inc.</p>
      <ul>
        <li><a href="#">Privacy</a></li>
        <li><a href="#">Accessibility</a></li>
        <li><a href="#">Terms</a></li>
      </ul>
    </div>
  </div>
</footer>


<script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/js/bootstrap.bundle.min.js"></script>
<script src="https://code.jquery.com/jquery-3.7.1.js" integrity="sha256-eKhayi8LEQwp4NKxN+CfCh+3qOVUtJn3QNZ0TciWLP4=" crossorigin="anonymous"></script>
<script async defer src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAcAKWEQPe2Bm_b0EU9kC2Cd7G776Se-dk&callback=initMap"></script>
<script src="{{ url_for('static', filename='js/script.js') }}"></script>
</body>
</html>