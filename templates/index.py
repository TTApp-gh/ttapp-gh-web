<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
	<link rel="icon" href="{{ url_for('static', filename='images/logo.jpeg') }}">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/css/bootstrap.min.css">
	<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet" />
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

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
                    <a class="nav-link" href="#riding">Ride</a>
                </li>
				<li id="eat" class="nav-item navigate">
                    <a class="nav-link" href="#eating">{{ app_name }} Eats</a>
                </li>
				<li id="biz" class="nav-item navigate">
                    <a class="nav-link" href="#business">{{ app_name }} for Business</a>
                </li>
				<li id="account" class="nav-item navigate">
                    <a class="nav-link" href="#account">Manage Account</a>
                </li>
                <li id="about" class="nav-item navigate">
                    <a class="nav-link" href="#about_us">About Us</a>
                </li>
                <li id="help0" class="nav-item navigate">
                    <a class="nav-link" href="#help">Help</a>
                </li>
                <li id="signin" class="nav-item navigate">
                    <a class="nav-link" href="#login">Log in</a>
                </li>
                <li id="signup" class="nav-item navigate">
                    <a class="nav-link btn btn-dark text-light" href="#signingup">Sign up</a>
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
<section id="riding" class="section home ride ride-package-section" title="ride">
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
                <div id="map" class="map-placeholder" style="ckground-color: #e0e0e0; width: 100%; height: 400px; border-radius: 8px; display: flex; align-items: center; justify-content: center;">
                    <p>Map Placeholder</p>
                </div>
            </div>
        </div>
    </div>
</section>


<!-- Suggestions Section -->
<section class="section home ride suggestions-section py-5">
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


<!-- TTApp for Business Section -->
<section class="section home uber-business-section py-5">
    <div class="container">
        <div class="row align-items-center">
            <!-- Text Column -->
            <div class="col-md-6">
                <h2>The {{ app_name }} you know, reimagined for business</h2>
                <p>{{ app_name }} for Business is a platform for managing global rides and meals, and local deliveries, for companies of any size.</p>
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
                <h5>{{ app_name }} Eats</h5>
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

<!-- Pricing Table Section -->
<section id="business" class="section home biz pricing-section" title="biz">
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

<!-- Testimonials Section -->
<section class="section home biz testimonial-section bg-light">
    <div class="container">
        <h2>What Our Customers Say</h2>
        <p>See why people love using {{ app_name }}.</p>
        <div class="row mt-4">
            <div class="col-md-4">
                <div class="card">
                    <div class="card-body">
                        <p>"{{ app_name }} has made my life so much easier. I can get a ride anytime, anywhere!"</p>
                        <h6>- John Doe</h6>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card">
                    <div class="card-body">
                        <p>"Quick, easy, and reliable! {{ app_name }} Eats is my go-to for food delivery."</p>
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


<!-- Download the App Section -->
<section class="section home biz download-app-section py-5" style="background-color: #f8f9fa;">
    <div class="container text-center">
        <h2 class="mb-4">It's easier in the apps</h2>
        <div class="row justify-content-center">
            <!-- TTApp App Card -->
            <div class="col-md-4">
                <div class="card p-3 mb-4 shadow-sm">
                    <div class="card-body text-center">
                        <img src="{{ url_for('static', filename='images/qr_code.jpeg') }}" alt="{{ app_name }} App QR Code" class="img-fluid mb-3">
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












<!--------- The signup Page is Identified and starts here id=drive -------------->
<!--------- The signup Page is Identified and starts here id=drive -------------->

<section id="signingup" class="section signup container my-5" title="signup">
  <div class="row g-4 text-center">
    <!-- Sign up to drive & deliver -->
    <div class="col-md-6">
      <div class="p-4 border-bottom">
        <h4 class="fw-bold"><a href="#signingup1" id="signup1" class="text-black fs-4 text-decoration-none navigate">Sign up to drive & deliver</a></h4>
        <a href="#signingup1" id="signup1" class="text-black fs-4 text-decoration-none navigate">→</a>
      </div>
    </div>
    <!-- Sign up to ride -->
    <div class="col-md-6">
      <div class="p-4 border-bottom">
        <h4 class="fw-bold"><a href="#signingup1" id="signup1" class="text-black fs-4 text-decoration-none navigate">Sign up to ride</a></h4>
        <a href="#signingup1" id="signup1" class="text-black fs-4 text-decoration-none navigate">→</a>
      </div>
    </div>
    <!-- Sign up to order delivery -->
    <div class="col-md-6">
      <div class="p-4 border-bottom">
        <h4 class="fw-bold"><a href="#signingup1" id="signup1" class="text-black fs-4 text-decoration-none navigate">Sign up to order delivery with TTApp</a></h4>
        <a href="#signingup1" id="signup1" class="text-black fs-4 text-decoration-none navigate">→</a>
      </div>
    </div>
    <!-- Sign up for business -->
    <div class="col-md-6">
      <div class="p-4 border-bottom">
        <h4 class="fw-bold"><a href="#signingup1" id="signup1" class="text-black fs-4 text-decoration-none navigate">Sign up to your TTApp Business account</a></h4>
        <a href="#signingup1" id="signup1" class="text-black fs-4 text-decoration-none navigate">→</a>
      </div>
    </div>
  </div>
</section>


<section id="signingup1" class="section signup1 container my-5" title="signup1">
  <div class="row justify-content-center">
    <div class="col-lg-6 col-md-8 col-sm-10">
      <!-- Form Title -->
      <h3 class="text-center mb-4">What's your phone number or email?</h3>
      
      <!-- Input Field -->
      <div class="mb-3">
        <input
          type="text"
          class="form-control form-control-lg"
          placeholder="Enter phone number or email"
        />
      </div>
      
      <!-- Continue Button -->
      <div class="d-grid mb-3">
        <button class="btn btn-dark btn-lg">Continue</button>
      </div>

      <!-- Divider -->
      <div class="d-flex align-items-center mb-3">
        <hr class="flex-grow-1" />
        <span class="mx-3 text-muted">or</span>
        <hr class="flex-grow-1" />
      </div>
      
      <!-- Alternative Login Options -->
      <div class="d-grid gap-3">
        <!-- Google Button -->
        <button class="btn btn-outline-secondary btn-lg d-flex align-items-center justify-content-center">
          <img
            src="{{ url_for('static', filename='images/google_logo.png') }}"
            alt="Google Logo"
            width="24"
            class="me-2"
          />
          Continue with Google
        </button>
        
        <!-- Apple Button -->
        <button class="btn btn-outline-secondary btn-lg d-flex align-items-center justify-content-center">
          <i class="bi bi-apple me-2 fs-4"></i>
          Continue with Apple
        </button>
        
        <!-- QR Code Button -->
        <button class="btn btn-outline-secondary btn-lg d-flex align-items-center justify-content-center">
          <i class="bi bi-qr-code-scan me-2 fs-4"></i>
          Log in with QR code
        </button>
      </div>

      <!-- Footer Note -->
      <p class="text-muted mt-4 text-center small">
        By proceeding, you consent to get calls, WhatsApp or SMS/RCS messages, 
        including by automated means, from {{ app_name }} and its affiliates to the number provided.
      </p>
    </div>
  </div>
</section>


<!--------------------------- The signup Page Ends Here ------------------------>
<!--------------------------- The signup Page Ends Here ------------------------>
















<!--------- The signin Page is Identified and starts here id=drive -------------->
<!--------- The signin Page is Identified and starts here id=drive -------------->

<section id="login" class="section signin container my-5" title="signin">
  <div class="row g-4 text-center">
    <!-- Sign in to drive & deliver -->
    <div class="col-md-6">
      <div class="p-4 border-bottom">
        <h4 class="fw-bold"><a href="#signingin1" id="signin1" class="text-black fs-4 text-decoration-none navigate"> Sign in to drive & deliver </a></h4>
        <a href="#signingin1" id="signin1" class="text-black fs-4 text-decoration-none navigate">→</a>
      </div>
    </div>
    <!-- Sign in to ride -->
    <div class="col-md-6">
      <div class="p-4 border-bottom">
        <h4 class="fw-bold"><a href="#signingin1" id="signin1" class="text-black fs-4 text-decoration-none navigate"> Sign in to ride </a></h4>
        <a href="#signingin1" id="signin1" class="text-black fs-4 text-decoration-none navigate">→</a>
      </div>
    </div>
    <!-- Sign in to order delivery -->
    <div class="col-md-6">
      <div class="p-4 border-bottom">
        <h4 class="fw-bold"><a href="#signingin1" id="signin1" class="text-black fs-4 text-decoration-none navigate">Sign in to order delivery with {{ app_name }} </a></h4>
        <a href="#signingin1" id="signin1" class="text-black fs-4 text-decoration-none navigate">→</a>
      </div>
    </div>
    <!-- Sign in for business -->
    <div class="col-md-6">
      <div class="p-4 border-bottom">
        <h4 class="fw-bold"><a href="#signingin1" id="signin1" class="text-black fs-4 text-decoration-none navigate"> Sign in to your {{ app_name }} Business account </a></h4>
        <a href="#signingin1" id="signin1" class="text-black fs-4 text-decoration-none navigate">→</a>
      </div>
    </div>
  </div>
</section>


<section id="signingin1" class="section signin1 container my-5" title="signin1">
  <div class="row justify-content-center">
    <div class="col-lg-6 col-md-8 col-sm-10">
      <!-- Form Title -->
      <h3 class="text-center mb-4">What's your phone number or email?</h3>
      
      <!-- Input Field -->
      <div class="mb-3">
        <input
          type="text"
          class="form-control form-control-lg"
          placeholder="Enter phone number or email"
        />
      </div>
      
      <!-- Continue Button -->
      <div class="d-grid mb-3">
        <button class="btn btn-dark btn-lg">Continue</button>
      </div>

      <!-- Divider -->
      <div class="d-flex align-items-center mb-3">
        <hr class="flex-grow-1" />
        <span class="mx-3 text-muted">or</span>
        <hr class="flex-grow-1" />
      </div>
      
      <!-- Alternative Login Options -->
      <div class="d-grid gap-3">
        <!-- Google Button -->
        <button class="btn btn-outline-secondary btn-lg d-flex align-items-center justify-content-center">
          <img
            src="{{ url_for('static', filename='images/google_logo.png') }}"
            alt="Google Logo"
            width="24"
            class="me-2"
          />
          Continue with Google
        </button>
        
        <!-- Apple Button -->
        <button class="btn btn-outline-secondary btn-lg d-flex align-items-center justify-content-center">
          <i class="bi bi-apple me-2 fs-4"></i>
          Continue with Apple
        </button>
        
        <!-- QR Code Button -->
        <button class="btn btn-outline-secondary btn-lg d-flex align-items-center justify-content-center">
          <i class="bi bi-qr-code-scan me-2 fs-4"></i>
          Log in with QR code
        </button>
      </div>

      <!-- Footer Note -->
      <p class="text-muted mt-4 text-center small">
        By proceeding, you consent to get calls, WhatsApp or SMS/RCS messages, 
        including by automated means, from {{ app_name }} and its affiliates to the number provided.
      </p>
    </div>
  </div>
</section>

<!--------------------------- The signin Page Ends Here ------------------------>
<!--------------------------- The signin Page Ends Here ------------------------>













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

<section class="section drive sign-up-section">
  <div class="sign-up-container">
    <div class="sign-up-header">
      <h2>Sign up to drive</h2>
      <a href="#" class="cta-arrow">
        <span>→</span>
      </a>
    </div>
    <hr />
    <div class="sign-up-content">
      <p>
        This is a promotional offer and is not a promise or guarantee of future earnings. This offer is available only to new drivers and delivery people on the {{ app_name }} who (i) have never previously signed up to drive or deliver with {{ app_name }}; (ii) receive this offer directly from Uber and see it in the guarantee tracker of the {{ app_name }} Driver app; (iii) are cleared to drive or deliver with {{ app_name }}; and (iv) complete the number of trips or deliveries displayed in the guarantee tracker in the city where they signed up to drive within the specified timeframe. Offer terms such as the number of trips or deliveries and reward amount may vary by location. The guarantee offer that you see in the app replaces any guarantee amounts {{ app_name }} previously offered you.
      </p>
      <p>
        Earnings from your trips (after service fees and certain charges are deducted, such as city or local government charges) are included toward your guaranteed amount; any tips and promotions you make are on top of that amount. Earnings from your deliveries (after service fees and certain charges are deducted, such as city or local government charges) and Eats Boost promotions are included toward your offer amount; any tips and additional promotions you make are on top of that amount.
      </p>
      <p>
        Any payment due will be automatically added to your account after you complete the required trips. Each completed trip or delivery counts as one trip or delivery toward your minimum requirement. Canceled trips or deliveries do not count. This offer is only valid for those who received it from {{ app_name }} (via an email, an ad, a web page, or a unique referral link) and meet the eligibility requirements. {{ app_name }} reserves the right to withhold or deduct payments that it determines or believes were fraudulent, illegal, in error, or in violation of the driver terms or these terms. Limited time only. Offer and terms are subject to change.
      </p>
    </div>
  </div>
</section>

<!--------------------------- The Drive Page Ends Here ------------------------>
<!--------------------------- The Drive Page Ends Here ------------------------>







<!--------- The TTApp Eat Page is Identified and starts here id=drive -------------->
<!--------- The TTApp Eat Page is Identified and starts here id=drive -------------->

<section id="eating" class="section eat delivery-section" title="eat">
  <div class="delivery-container">
    <header class="delivery-header">
      <h1>Order delivery near you</h1>
    </header>
    <form class="delivery-form">
      <div class="input-group">
        <input
          type="text"
          placeholder="Enter delivery address"
          class="delivery-input"
          aria-label="Enter delivery address"
        />
        <select class="delivery-time">
          <option value="now">Deliver now</option>
          <option value="later">Deliver later</option>
        </select>
        <button type="button" class="search-btn">Search here</button>
      </div>
      <p class="signin-link">
        Or <a href="#">Sign In</a>
      </p>
    </form>
    <div class="background-overlay"></div>
  </div>
</section>

<section class="section eat ttapp-services">
  <div class="services-container">
    <div class="service-card">
      <img src="{{ url_for('static', filename='images/eat_image1.PNG') }}" alt="Feed your employees" class="service-image" />
      <h2>Feed your employees</h2>
      <a href="#" class="service-link">Create a business account</a>
    </div>
    <div class="service-card">
      <img src="{{ url_for('static', filename='images/eat_image2.PNG') }}" alt="Your restaurant, delivered" class="service-image" />
      <h2>Your restaurant, delivered</h2>
      <a href="#" class="service-link">Add your restaurant</a>
    </div>
    <div class="service-card">
      <img src="{{ url_for('static', filename='images/eat_image3.PNG') }}" alt="Deliver with TTApp" class="service-image" />
      <h2>Deliver with TTApp</h2>
      <a href="#" class="service-link">Sign up to deliver</a>
    </div>
  </div>

  <div class="cities-near-me">
    <h2>Cities near me</h2>
    <a href="#" class="view-all-link">View all cities</a>
    <div id="maps" style="height: 500px; width: 100%;"></div>
  </div>
</section>


<section class="section eat ttapp-locations">
  <div class="cities-section">
    <h2>Cities with TTApp</h2>
    <div class="cities-list">
      <ul>
        <li>Akron</li>
        <li>Albuquerque</li>
        <li>Bridgeport</li>
        <li>Concord</li>
        <li>Dayton</li>
        <li>El Paso</li>
      </ul>
      <ul>
        <li>Hartford</li>
        <li>Houston</li>
        <li>Indianapolis</li>
        <li>McAllen</li>
        <li>Mesa</li>
        <li>Milwaukee</li>
      </ul>
      <ul>
        <li>Nashville</li>
        <li>New Orleans</li>
        <li>Oklahoma City</li>
        <li>Omaha</li>
        <li>Orlando</li>
        <li>Palm Bay</li>
      </ul>
      <ul>
        <li>Providence</li>
        <li>Queens</li>
        <li>San Antonio</li>
        <li>Stony Brook</li>
        <li>Tucson</li>
        <li>West Hollywood</li>
      </ul>
    </div>
    <a href="#" class="view-all-link">View all cities</a>
  </div>

  <div class="countries-section">
    <h2>Countries with TTApp</h2>
    <div class="countries-list">
      <ul>
        <li>Australia</li>
        <li>Belgium</li>
        <li>Canada</li>
        <li>Chile</li>
        <li>Costa Rica</li>
      </ul>
      <ul>
        <li>France</li>
        <li>Germany</li>
        <li>Guatemala</li>
        <li>Ireland</li>
        <li>Italy</li>
      </ul>
      <ul>
        <li>Mexico</li>
        <li>Netherlands</li>
        <li>New Zealand</li>
        <li>Panama</li>
        <li>Poland</li>
      </ul>
      <ul>
        <li>Sri Lanka</li>
        <li>Sweden</li>
        <li>Switzerland</li>
        <li>Taiwan (ROC)</li>
        <li>United Kingdom</li>
      </ul>
    </div>
    <a href="#" class="view-all-link">View all countries</a>
  </div>
</section>

<!--------------------------- The TTApp Eat Page Ends Here ------------------------>
<!--------------------------- The TTApp Eat Page Ends Here ------------------------>











<!--------- The About us Page is Identified and starts here id=about_us -------------->
<!--------- The About us Page is Identified and starts here id=about_us -------------->

<section id="about_us" class="section about about-us-section" title="about">
  <div class="container-fluid p-0">
    <!-- Hero Section with Image -->
    <div class="row g-0">
      <div class="col-12">
        <div class="about-hero" style="background-image: url('../static/images/about0.PNG'); background-size: cover; background-position: center; height: 400px;">
          <div class="d-flex align-items-center justify-content-center h-100">
            <h1 class="text-white display-4 fw-bold">About Us</h1>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Content Section -->
  <div class="container py-5">
    <h2 class="fw-bold mb-4">We reimagine the way the world moves for the better</h2>
    <p class="text-muted mb-4">
      Movement is what we power. It’s our lifeblood. It runs through our veins. It’s what gets us out of bed each morning. It pushes us to constantly reimagine how we can move better. For you. For all the places you want to go. For all the things you want to get. For all the ways you want to earn. Across the entire world. In real time. At the incredible speed of now.
    </p>
    <a href="#" class="text-decoration-underline text-dark fw-semibold">Read our full mission statement</a>
  </div>
</section>

<section class="section about ceo-sustainability-section">
  <div class="container-fluid">
    <!-- CEO Section -->
    <div class="row align-items-center mb-5">
      <div class="col-lg-6 p-0">
        <div class="ceo-image" style="background-image: url('../static/images/CEO.jpg'); background-size: cover; background-position: center; height: 300px;">
          <!-- Empty space for the CEO image -->
        </div>
      </div>
      <div class="col-lg-6 d-flex flex-column justify-content-center text-center text-lg-start py-4 px-3">
        <h2 class="fw-bold mb-3">CEO</h2>
        <p class="text-muted">
          Read about our team’s commitment to provide everyone on our global platform with the technology that can help them move ahead.
        </p>
        <a href="#" class="btn btn-dark fw-bold px-4 py-2">Read the CEO's letter</a>
      </div>
    </div>

    <!-- Sustainability Section -->
    <div class="row align-items-center">
      <div class="col-lg-6 order-lg-2 p-0">
        <img src="{{ url_for('static', filename='images/sustainability.PNG') }}" alt="Sustainability Image" class="img-fluid">
      </div>
      <div class="col-lg-6 order-lg-1 d-flex flex-column justify-content-center py-4 px-3">
        <h2 class="fw-bold mb-3">Sustainability</h2>
        <p class="text-muted">
          {{ app_name }} is committing to becoming a fully electric, zero-emission platform by 2040, with 100% of rides taking place in zero-emission vehicles, on public transit, or with micromobility.
        </p>
        <p class="text-muted">
          It is our responsibility to aggressively tackle the challenge of climate change. We aim to provide riders with greener options, help drivers go electric, and make transparency a priority.
        </p>
        <a href="#" class="text-decoration-underline text-dark fw-semibold">Learn more</a>
      </div>
    </div>
  </div>
</section>
<br />
<section class="section about ttapp-section">
  <div class="container">
    <!-- Rides and Beyond Section -->
    <div class="row align-items-center mb-5">
      <!-- Image Column -->
      <div class="col-lg-6">
        <img src="{{ url_for('static', filename='images/road.PNG') }}" alt="Highway" class="img-fluid rounded">
      </div>
      <!-- Content Column -->
      <div class="col-lg-6">
        <h2 class="fw-bold mb-3">Rides and beyond</h2>
        <p class="text-muted">
          In addition to helping riders find a way to go from point A to point B, {{ app_name }} helps people order food quickly and affordably, removes barriers to healthcare, creates new freight-booking solutions, and helps companies provide a seamless employee travel experience. We also ensure drivers and couriers earn fairly.
        </p>
        <div class="d-flex gap-3">
          <a href="#" class="text-decoration-underline text-dark fw-semibold">How to use {{ app_name }}</a>
          <a href="#" class="text-decoration-underline text-dark fw-semibold">Our offerings</a>
        </div>
      </div>
    </div>

    <!-- Your Safety Drives Us Section -->
    <div class="row align-items-center">
      <!-- Content Column -->
      <div class="col-lg-6">
        <h2 class="fw-bold mb-3">Your safety drives us</h2>
        <p class="text-muted">
          Whether you're in the back seat or behind the wheel, your safety is essential. At {{ app_name }}, we are committed to ensuring safety at every step. Technology is at the heart of our approach, partnering with safety advocates and developing new technologies to improve safety, making it easier for everyone to get around.
        </p>
        <a href="#" class="text-decoration-underline text-dark fw-semibold">Learn more</a>
      </div>
      <!-- Image/Icon Column -->
      <div class="col-lg-6 text-center">
        <img src="{{ url_for('static', filename='images/safety.PNG') }}" alt="Safety Shield Icon" class="img-fluid" style="max-height: 400px;">
      </div>
    </div>
  </div>
</section>

<section class="section about ttapp-company-info py-5">
  <div class="container">
    <h2 class="fw-bold mb-5 text-center">Company Info</h2>
    <div class="row">
      <!-- Card 1: Who's driving TTApp -->
      <div class="col-lg-4 col-md-6 mb-4">
        <div class="card border-0 shadow-sm h-100">
          <img src="{{ url_for('static', filename='images/info1.PNG') }}" class="card-img-top" alt="Leadership Presentation">
          <div class="card-body">
            <h5 class="card-title fw-bold">Who's driving {{ app_name }}</h5>
            <p class="card-text text-muted">
              We're building a culture within {{ app_name }} that emphasizes doing the right thing for riders, drivers, and employees. Find out more about the team that's leading the way.
            </p>
            <a href="#" class="text-decoration-underline text-dark fw-semibold">See our leadership</a>
          </div>
        </div>
      </div>

      <!-- Card 2: Getting diversity right -->
      <div class="col-lg-4 col-md-6 mb-4">
        <div class="card border-0 shadow-sm h-100">
          <img src="{{ url_for('static', filename='images/info2.PNG') }}" class="card-img-top" alt="Diversity Team">
          <div class="card-body">
            <h5 class="card-title fw-bold">Getting diversity right</h5>
            <p class="card-text text-muted">
              At {{ app_name }}, our goal is to create a workplace that is inclusive and reflects the diversity of the cities we serve, ensuring everyone can thrive.
            </p>
            <a href="#" class="text-decoration-underline text-dark fw-semibold">Read about diversity</a>
          </div>
        </div>
      </div>

      <!-- Card 3: Acting with integrity -->
      <div class="col-lg-4 col-md-6 mb-4">
        <div class="card border-0 shadow-sm h-100">
          <img src="{{ url_for('static', filename='images/info3.PNG') }}" class="card-img-top" alt="Integrity Discussion">
          <div class="card-body">
            <h5 class="card-title fw-bold">Acting with integrity</h5>
            <p class="card-text text-muted">
              {{ app_name }}'s Ethics & Compliance Program reflects our commitment to transparency and ethical standards across all aspects of our business.
            </p>
            <a href="#" class="text-decoration-underline text-dark fw-semibold">Learn more</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>



<!--------------------------- The About us Page Ends Here ------------------------>
<!--------------------------- The About us Page Ends Here ------------------------>











<!--------- The Help Page is Identified and starts here id=drive -------------->
<!--------- The Help Page is Identified and starts here id=drive -------------->

<section id="help" class="section help0 container-fluid bg-light text-center py-5 help_bg" title="help0">
  <div class="container">
    <!-- Header Section -->
    <h1 class="fw-bold mb-3">Welcome to {{ app_name }} Support</h1>
    <p class="text-black mb-5">
      We’re here to help. Looking for customer service contact information? Explore support 
      resources for the relevant products below to find the best way to reach out about your issue.
    </p>

    <!-- Support Categories -->
    <div class="row justify-content-center g-4">
      <!-- Riders -->
      <div class="col-lg-2 col-md-4 col-sm-6">
        <div class="card border-0 shadow-sm p-3">
          <i class="bi bi-car-front fs-1 mb-3"></i>
          <h5 class="card-title">Riders</h5>
        </div>
      </div>
      
      <!-- Driving & Delivering -->
      <div class="col-lg-2 col-md-4 col-sm-6">
        <div class="card border-0 shadow-sm p-3">
          <i class="bi bi-steering-wheel fs-1 mb-3"></i>
          <h5 class="card-title">Driving & Delivering</h5>
        </div>
      </div>
      
      <!-- TTApp Eats -->
      <div class="col-lg-2 col-md-4 col-sm-6">
        <div class="card border-0 shadow-sm p-3">
          <i class="bi bi-cup-straw fs-1 mb-3"></i>
          <h5 class="card-title">{{ app_name }} Eats</h5>
        </div>
      </div>
      
      <!-- Merchants & Restaurants -->
      <div class="col-lg-2 col-md-4 col-sm-6">
        <div class="card border-0 shadow-sm p-3">
          <i class="bi bi-shop-window fs-1 mb-3"></i>
          <h5 class="card-title">Merchants & Restaurants</h5>
        </div>
      </div>
      
      <!-- Bikes & Scooters -->
      <div class="col-lg-2 col-md-4 col-sm-6">
        <div class="card border-0 shadow-sm p-3">
          <i class="bi bi-bicycle fs-1 mb-3"></i>
          <h5 class="card-title">Bikes & Scooters</h5>
        </div>
      </div>
      
      <!-- TTApp for Business -->
      <div class="col-lg-2 col-md-4 col-sm-6">
        <div class="card border-0 shadow-sm p-3">
          <i class="bi bi-briefcase fs-1 mb-3"></i>
          <h5 class="card-title">{{ app_name }} for Business</h5>
        </div>
      </div>
      
      <!-- Freight -->
      <div class="col-lg-2 col-md-4 col-sm-6">
        <div class="card border-0 shadow-sm p-3">
          <i class="bi bi-truck fs-1 mb-3"></i>
          <h5 class="card-title">Freight</h5>
        </div>
      </div>
    </div>
  </div>
</section>

<!--------------------------- The Help Page Ends Here ------------------------>
<!--------------------------- The Help Page Ends Here ------------------------>










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
          <li><a href="#">{{ app_name }} Freight</a></li>
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
