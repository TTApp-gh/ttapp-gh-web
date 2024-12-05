<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
	<link rel="icon" href="{{ url_for('static', filename='images/logo.jpeg') }}">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/css/bootstrap.min.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons/font/bootstrap-icons.css" rel="stylesheet" />
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
				<li id="accounts" class="nav-item navigate">
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
        <a href="#riding" id="ride" class="btn btn-light navigate">Get Started</a>
    </div>
</section>

<!-- Ride/Package Section -->
<section id="riding" class="section home ride ride-package-section" title="ride">
<br />
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
                    <div class="tab-pane show active" id="ride" role="tabpanel" aria-labelledby="ride-tab">
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
                    <a href="#riding" id="ride" class=" navigate btn btn-light border">Details</a>
                </div>
            </div>
            <!-- Suggestion Card 2 -->
            <div class="col-md-4">
                <div class="card shadow-sm p-4">
                    <h4 class="card-title">Package</h4>
                    <p class="card-text">{{ app_name }} Connect makes same-day delivery easier than ever.</p>
                    <img src="{{ url_for('static', filename='images/package.PNG') }}" alt="Package" class="img-fluid mb-3">
                    <a href="#packaging" id="package1" class="navigate btn btn-light border">Details</a>
                </div>
            </div>
            <!-- Suggestion Card 3 -->
            <div class="col-md-4">
                <div class="card shadow-sm p-4">
                    <h4 class="card-title">Reserve</h4>
                    <p class="card-text">Reserve your ride in advance so you can relax on the day of your trip.</p>
                    <img src="{{ url_for('static', filename='images/reserve.PNG') }}" alt="Reserve" class="img-fluid mb-3">
                    <a href="#riding" id="ride" class=" navigate btn btn-light border">Details</a>
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
                <a href="#login" id="signin" class="btn btn-dark mb-3 navigate">Get started</a>
                <p>Already have an account? <a href="#login" id="signin" class="text-black navigate">Sign in</a></p>
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
                <a href="#business" id="biz" class="btn btn-dark mb-3 navigate">Get started</a>
                <a href="#business" id="biz" class="ml-3 text-black navigate">Check out our solutions</a>
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














<!--------------------------- The Manage Account Page starts Here ------------------------>
<!--------------------------- The Manage Account Page starts Here ------------------------>

<section id="account" class="section account1 ttapp-account-info" title="account1">
  <div class="container-fluid p-0">
    <!-- Sidebar and Main Content Wrapper -->
    <div class="row">
      <!-- Sidebar -->
      <aside class="col-md-3 bg-dark text-white py-4">
        <h5 class="text-uppercase fw-bold px-4">TTApp Account</h5>
        <nav class="nav flex-column px-4 mt-4">
          <a href="#account" id="account1" class="navigate nav-link text-white active">Account Info</a>
          <a href="#security" id="security1" class="navigate nav-link text-white">Security</a>
          <a href="#privacy" id="privacy1" class="navigate nav-link text-white">Privacy & Data</a>
        </nav>
      </aside>

      <!-- Main Content -->
      <div class="col-md-9 bg-light py-5">
        <div class="container">
          <!-- Section Header -->
          <h2 class="fw-bold mb-4">Account Info</h2>

          <!-- Profile Info -->
          <div class="d-flex align-items-center mb-5">
            <div class="profile-image position-relative me-3">
              <img
                src="{{ url_for('static', filename='images/CEO.jpg') }}"
                alt="Profile Image"
                class="rounded-circle border"
              />
              <button
                class="btn btn-sm btn-light border rounded-circle position-absolute"
                style="bottom: 0; right: 0;"
              >
                <i class="bi bi-pencil"></i>
              </button>
            </div>
            <div>
              <h4 class="fw-semibold mb-0">Basic Info</h4>
            </div>
          </div>

          <!-- Info Cards -->
          <ul class="list-group list-group-flush">
            <li class="list-group-item d-flex justify-content-between align-items-center">
              <div>
                <h6 class="mb-1">Name</h6>
                <p class="mb-0">Abraham Livinus</p>
              </div>
              <a href="#" class="text-decoration-none">
                <i class="bi bi-chevron-right"></i>
              </a>
            </li>
            <li class="list-group-item d-flex justify-content-between align-items-center">
              <div>
                <h6 class="mb-1">Phone number</h6>
                <p class="mb-0">+2348109214791 <i class="bi bi-check-circle text-success"></i></p>
              </div>
              <a href="#" class="text-decoration-none">
                <i class="bi bi-chevron-right"></i>
              </a>
            </li>
            <li class="list-group-item d-flex justify-content-between align-items-center">
              <div>
                <h6 class="mb-1">Email</h6>
                <p class="mb-0">abrahamlivinus@gmail.com <i class="bi bi-check-circle text-success"></i></p>
              </div>
              <a href="#" class="text-decoration-none">
                <i class="bi bi-chevron-right"></i>
              </a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>


<section id="security" class="section security1 ttapp-security" title="security1">
  <div class="container-fluid p-0">
    <!-- Sidebar and Main Content Wrapper -->
    <div class="row">
      <!-- Sidebar -->
      <aside class="col-md-3 bg-dark text-white py-4">
        <h5 class="text-uppercase fw-bold px-4">TTApp Account</h5>
        <nav class="nav flex-column px-4 mt-4">
          <a href="#account" id="account1" class="navigate nav-link text-white">Account Info</a>
          <a href="#security" id="security1" class="navigate nav-link text-white active">Security</a>
          <a href="#privacy" id="privacy1" class="navigate nav-link text-white">Privacy & Data</a>
        </nav>
      </aside>

      <!-- Main Content -->
      <div class="col-md-9 bg-light py-5">
        <div class="container">
          <!-- Section Header -->
          <h2 class="fw-bold mb-4">Security</h2>

          <!-- Logging In Section -->
          <div class="mb-5">
            <h4 class="fw-semibold mb-3">Logging in to TTApp</h4>
            <ul class="list-group list-group-flush">
              <li class="list-group-item d-flex justify-content-between align-items-center">
                <div>
                  <h6 class="mb-1">Password</h6>
                </div>
                <a href="#" class="text-decoration-none">
                  <i class="bi bi-chevron-right"></i>
                </a>
              </li>
              <li class="list-group-item d-flex justify-content-between align-items-center">
                <div>
                  <h6 class="mb-1">Passkeys</h6>
                  <p class="mb-0 text-muted">
                    Passkeys are easier and more secure than passwords.
                  </p>
                </div>
                <a href="#" class="text-decoration-none">
                  <i class="bi bi-chevron-right"></i>
                </a>
              </li>
              <li class="list-group-item d-flex justify-content-between align-items-center">
                <div>
                  <h6 class="mb-1">Authenticator app</h6>
                  <p class="mb-0 text-muted">
                    Set up your authenticator app to add an extra layer of security.
                  </p>
                </div>
                <a href="#" class="text-decoration-none">
                  <i class="bi bi-chevron-right"></i>
                </a>
              </li>
              <li class="list-group-item d-flex justify-content-between align-items-center">
                <div>
                  <h6 class="mb-1">2-step verification</h6>
                  <p class="mb-0 text-muted">
                    Add additional security to your account with 2-step verification.
                  </p>
                </div>
                <a href="#" class="text-decoration-none">
                  <i class="bi bi-chevron-right"></i>
                </a>
              </li>
            </ul>
          </div>

          <!-- Connected Social Apps Section -->
          <div class="mb-5">
            <h4 class="fw-semibold mb-3">Connected social apps</h4>
            <p class="text-muted">
              You've allowed these social apps to sign in to your TTApp account.
            </p>
            <div class="d-flex justify-content-between align-items-center bg-white p-3 border rounded">
              <div class="d-flex align-items-center">
                <i class="bi bi-google fs-4 text-muted me-3"></i>
                <span>Google</span>
              </div>
              <button class="btn btn-outline-danger btn-sm">Disconnect</button>
            </div>
          </div>

          <!-- Login Activity Section -->
          <div>
            <h4 class="fw-semibold mb-3">Login activity</h4>
            <p class="text-muted">
              You're logged in or have been logged in on these devices within the last 30 days. Multiple logins from the same device may appear.
            </p>
            <div class="bg-white p-3 border rounded d-flex align-items-start">
              <i class="bi bi-laptop fs-3 text-muted me-3"></i>
              <div>
                <h6 class="mb-1">Chrome on Windows</h6>
                <p class="mb-0 text-primary">Your current login</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section id="privacy" class="section privacy1 container-fluid bg-dark text-light" title="privacy1">
  <div class="row">
    <div class="col-md-3">
      <nav class="nav flex-column px-4 mt-4">
          <a href="#account" id="account1" class="navigate nav-link text-white">Account Info</a>
          <a href="#security" id="security1" class="navigate nav-link text-white">Security</a>
          <a href="#privacy" id="privacy1" class="navigate nav-link text-white active">Privacy & Data</a>
        </nav>
    </div>

    <div class="col-md-9">
      <h2 class="mt-3">Privacy & Data</h2>
      <a href="#privacy0" id="privacy2" class="navigate text-white">
        <h4 class="mt-4">Privacy Center</h4>
        <p>Take control of your privacy and learn how we protect it.</p>
      </a>

      <h4 class="mt-4">Third-party apps with account access</h4>
      <p>Once you allow access to third-party apps, you'll see them here. <a href="#third_party" id="third_party1" class="navigate text-white">Learn more</a></p>
    </div>
  </div>
</section>

<!--------------------------- The Manage Account Page Ends Here ------------------------>
<!--------------------------- The Manage Account Page Ends Here ------------------------>












<!--------------------------- The Privacy Page Starts Here ------------------------>
<!--------------------------- The Privacy Page Starts Here ------------------------>

<section id="privacy0" class="section privacy2 ttapp-privacy py-5" title="privacy2">
  <div class="container">
    <!-- Privacy Center Heading -->
    <div class="text-center mb-5">
      <h2 class="fw-bold">Privacy Center</h2>
      <p class="text-muted">Take control of your privacy and learn how we protect it.</p>
    </div>

    <!-- Section 1: Your Data and Privacy -->
    <div class="mb-5">
      <h4 class="fw-bold mb-4">Your data and privacy at {{ app_name }}</h4>
      <div class="row g-4">
        <div class="col-md-4">
          <div class="card h-100 text-center p-3">
            <img src="{{ url_for('static', filename='images/summary.PNG') }}" alt="Data Summary" class="card-img-top mb-3" style="height: 100px; object-fit: contain;">
            <div class="card-body">
              <p class="card-text">Would you like to see a summary of how you use {{ app_name }}?</p>
              <a href="#" class="btn btn-outline-primary text-white bg-dark">See summary</a>
            </div>
          </div>
        </div>
        <div class="col-md-4">
          <div class="card h-100 text-center p-3">
            <img src="{{ url_for('static', filename='images/view.PNG') }}" alt="Data Shape" class="card-img-top mb-3" style="height: 100px; object-fit: contain;">
            <div class="card-body">
              <p class="card-text">How does your data shape your trip experience?</p>
              <a href="#" class="btn btn-outline-primary text-white bg-dark">View</a>
            </div>
          </div>
        </div>
        <div class="col-md-4">
          <div class="card h-100 text-center p-3">
            <img src="{{ url_for('static', filename='images/request.PNG') }}" alt="Personal Data" class="card-img-top mb-3" style="height: 100px; object-fit: contain;">
            <div class="card-body">
              <p class="card-text">Would you like a copy of your personal data?</p>
              <a href="#" class="btn btn-outline-primary text-white bg-dark">Request</a>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Section 2: Ads and Data -->
    <div class="mb-5">
      <h4 class="fw-bold mb-4">Ads and Data</h4>
      <ul class="list-group">
        <li class="list-group-item d-flex justify-content-between align-items-center">
          Offers and Promos from {{ app_name }}
          <span class="text-muted">Control personalized offers and promos</span>
          <a href="#" class="text-primary">></a>
        </li>
        <li class="list-group-item d-flex justify-content-between align-items-center">
          Data Tracking
          <span class="text-muted">Control Data Tracking for Personalized Ads</span>
          <a href="#" class="text-primary">></a>
        </li>
        <li class="list-group-item d-flex justify-content-between align-items-center">
          Ads on {{ app_name }} Eats
          <span class="text-muted">Control personalized ads you see in Eats</span>
          <a href="#" class="text-primary">></a>
        </li>
        <li class="list-group-item d-flex justify-content-between align-items-center">
          Ads on Rides
          <span class="text-muted">Control personalized ads you see on Rides</span>
          <a href="#" class="text-primary">></a>
        </li>
      </ul>
    </div>

    <!-- Section 3: Account Security and Privacy Approach -->
    <div class="mb-5">
      <h4 class="fw-bold mb-4">Account Security</h4>
      <div class="d-flex justify-content-between align-items-center">
        <span>Account Deletion</span>
        <a href="#" class="text-primary">></a>
      </div>
    </div>

    <div class="text-center">
      <h4 class="fw-bold">How do we approach privacy at {{ app_name }}?</h4>
      <div class="mt-4">
        <a href="#" class="btn btn-outline-primary me-3 text-white bg-dark">Check out Privacy Overview Page</a>
        <a href="#" class="btn btn-outline-primary text-white bg-dark">Submit a privacy inquiry</a>
      </div>
    </div>
  </div>
</section>

<!--------------------------- The Privacy Page Ends Here ------------------------>
<!--------------------------- The Privacy Page Ends Here ------------------------>











<!--------------------------- The Third Party Page Starts Here ------------------------>
<!--------------------------- The Third Party Page Starts Here ------------------------>

<section id="third_party" class="section third_party1 ttapp-third-party py-5" title="third_party1">
  <div class="container">
    <nav class="breadcrumb mb-4">
      <a href="#" class="breadcrumb-item">Home</a>
      <span class="breadcrumb-item active">Third Party Applications</span>
    </nav>

    <h1 class="fw-bold mb-4">Third Party Applications</h1>
    <p>
      You can connect third-party applications to your TTApp account to enable additional features. 
      This most commonly happens when you:
    </p>
    <ul>
      <li>Explore benefits and discounts provided by third parties</li>
      <li>Sign in to other apps with your TTApp account</li>
    </ul>

    <p>
      Third-party applications will request permission to access your TTApp account and data before enabling these features. 
      Such applications do <strong>NOT</strong> include:
    </p>
    <ul>
      <li>Social accounts used to sign in to TTApp (like Google or Facebook)</li>
      <li>Government or regulatory entities</li>
      <li>Advertisers</li>
    </ul>

    <h2 class="fw-bold mt-4">Removing Access</h2>
    <p>
      You can view and manage which third-party applications can access your data under 
      <a href="#account" id="accounts" class="navigate text-black text-decoration-none">account management</a>.
    </p>
    <p>
      If you remove access for a third-party application, they won’t be able to access your data, and you won’t have access to their services. However, they may still have data they previously accessed.
    </p>
    <p>
      Please refer to the third party’s privacy notice for information regarding how and why they collect and use your information, and contact the third party if you have any questions. Each third party’s privacy notice can be found under 
      <a href="#account" id="accounts" class=" navigate text-black text-decoration-none">account management</a>.
    </p>
    <p>
      If you would like to use a third-party application whose access you removed in the future, you will be asked to provide access before using the app.
    </p>

    <div class="row mt-5">
      <div class="col-md-6 text-center">
        <p class="fw-bold">Can we help with this section?</p>
        <button class="btn btn-outline-primary">Yes</button>
        <button class="btn btn-outline-secondary">No</button>
      </div>
    </div>
  </div>
</section>

<!--------------------------- The Third Party Page Ends Here ------------------------>
<!--------------------------- The Third Party Page Ends Here ------------------------>













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
        <a href="#signingup" id="signup" class="btn-primary navigate">Sign up to drive</a>
        <a href="#login" id="signin" class="btn-secondary navigate">Already have an account? Sign in</a>
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
        <a href="#signingup" id="signup" class="navigate text-dark">Sign up online</a>
      </div>
      <div class="step">
        <span class="step-icon">📋</span>
        <h3>Check driving requirements</h3>
        <p>
          Most people are eligible to drive with Uber. Here’s what you need to know if you’re driving in Lagos or Abuja.
        </p>
        <a href="#" class="navigate text-dark">Requirements</a>
      </div>
      <div class="step">
        <span class="step-icon">✔️</span>
        <h3>Get a vehicle</h3>
        <p>
          You can sign up even if you don’t have a car that meets the vehicle requirements in Nigeria right now.
        </p>
        <a href="#" class="navigate text-dark">Vehicle requirements</a>
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
        <a href="#help" id="help0" class="navigate text-dark">Get help</a>
      </div>
      <div class="extra">
        <div class="icon-container">
          <img src="{{ url_for('static', filename='images/contact_us.PNG') }}" alt="Contact us icon" />
        </div>
        <h3>Contact us</h3>
        <p>
          Got questions? Get answers. Enjoy personal support at an {{ app_name }} Greenlight Hub in Lagos or Abuja.
        </p>
        <a href="#contact" id="contact1" class="navigate text-dark">Contact us</a>
      </div>
      <div class="extra">
        <div class="icon-container">
          <img src="{{ url_for('static', filename='images/drive_safe.PNG') }}" alt="Drive safely icon" />
        </div>
        <h3>Drive safely</h3>
        <p>
          The {{ app_name }} is full of features that help you stay safe and confident before, during, and after every trip. And if you need help, {{ app_name }} gives you 24/7 support.
        </p>
        <a href="#" class="navigate text-dark">Read more about safety</a>
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
      <a href="#" class="learn-more text-dark navigate">Learn more</a>
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
      <a href="#signingup" id="signup" class="cta-arrow navigate">
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












<!--------------------------- The Package Page Starts Here ------------------------>
<!--------------------------- The Package Page Starts Here ------------------------>

<section id="packaging" class="section package1 ttapp-package py-5" title="package1">
  <div class="container-fluid">
    <div class="row">
      <!-- Left Section: Details -->
      <div class="col-md-4">
        <div class="card h-100 shadow border-0">
          <img src="{{ url_for('static', filename='images/package0.PNG') }}" alt="Package Delivery" class="card-img-top" style="height: 200px; object-fit: cover;">
          <div class="card-body">
            <h4 class="fw-bold">TTApp Package</h4>
            <p class="text-muted">Have a courier deliver something for you. Get packages delivered in the time it takes to drive there.</p>
            <div class="btn-group mb-3" role="group">
              <button type="button" class="btn btn-outline-primary bg-dark text-white active">Send</button>
              <button type="button" class="btn btn-outline-primary text-black">Receive</button>
            </div>
            <div class="mb-3">
              <label for="pickup-location" class="form-label">Pickup location</label>
              <select id="pickup-location" class="form-select">
                <option selected>Select location</option>
                <option value="1">Location 1</option>
                <option value="2">Location 2</option>
                <option value="3">Location 3</option>
              </select>
            </div>
            <button type="button" class="btn btn-primary bg-dark text-white w-100" disabled>Search</button>
          </div>
        </div>
      </div>

      <!-- Right Section: Map -->
      <div class="col-md-8">
        <div class="map-container h-100">
          <iframe
            src="https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d14604.759530823495!2d3.4037482!3d6.4495088!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sen!2sng!4v1634144538164!5m2!1sen!2sng"
            width="100%"
            height="100%"
            style="border:0;"
            allowfullscreen=""
            loading="lazy"></iframe>
        </div>
      </div>
    </div>
  </div>
</section>

<!--------------------------- The Package Page Ends Here ------------------------>
<!--------------------------- The Package Page Ends Here ------------------------>







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

<hr class="section eat cities1" />
<h2 class="section cities1">Cities</h2>
<hr class="section eat cities1" />
<div id="cities" class="section eat cities1 map-container h-600" title="cities1">
  <iframe
    src="https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d14604.759530823495!2d3.4037482!3d6.4495088!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sen!2sng!4v1634144538164!5m2!1sen!2sng"
    width="100%"
    height="600px"
    style="border:0;"
    allowfullscreen=""
    loading="lazy"></iframe>
</div>


<section class="section eat cities1 ttapp-locations">
  <div class="cities-section">
    <h2>Cities with {{ app_name }}</h2>
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

<section class="section about ttapp-latest py-5">
  <div class="container">
    <!-- Section Header -->
    <h2 class="fw-bold text-center mb-5">Keep up with the latest</h2>
    <div class="row text-center">
      <!-- Newsroom -->
      <div class="col-lg-4 col-md-6 mb-4">
        <div class="icon mb-3">
          <i class="bi bi-megaphone" style="font-size: 2rem; color: #333;"></i>
        </div>
        <h5 class="fw-bold">Newsroom</h5>
        <p class="text-muted">
          Get announcements about partnerships, app updates, initiatives, and more near you and around the world.
        </p>
        <a href="#" class="text-decoration-underline text-dark fw-semibold">Go to Newsroom</a>
      </div>
      <!-- Blog -->
      <div class="col-lg-4 col-md-6 mb-4">
        <div class="icon mb-3">
          <i class="bi bi-journal-text" style="font-size: 2rem; color: #333;"></i>
        </div>
        <h5 class="fw-bold">Blog</h5>
        <p class="text-muted">
          Find new places to explore and learn about TTApp products, partnerships, and more.
        </p>
        <a href="#" class="text-decoration-underline text-dark fw-semibold">Read our posts</a>
      </div>
      <!-- Investor Relations -->
      <div class="col-lg-4 col-md-6 mb-4">
        <div class="icon mb-3">
          <i class="bi bi-graph-up" style="font-size: 2rem; color: #333;"></i>
        </div>
        <h5 class="fw-bold">Investor relations</h5>
        <p class="text-muted">
          Download financial reports, see next-quarter plans, and read about our corporate responsibility initiatives.
        </p>
        <a href="#" class="text-decoration-underline text-dark fw-semibold">Learn more</a>
      </div>
    </div>
  </div>
  <div class="container mt-5">
    <!-- Call to Action -->
    <div class="row align-items-center">
      <div class="col-lg-6 mb-4 mb-lg-0">
        <h3 class="fw-bold">Come reimagine with us</h3>
        <p class="text-muted">Join our team to build innovative solutions that redefine the way people connect and explore.</p>
        <a href="#" class="btn btn-dark px-4 py-2">Search open roles</a>
      </div>
      <div class="col-lg-6 text-center">
        <img src="{{ url_for('static', filename='images/globe.PNG') }}" alt="Globe illustration" class="img-fluid" style="max-height: 400px;">
      </div>
    </div>
  </div>
</section>

<!--------------------------- The About us Page Ends Here ------------------------>
<!--------------------------- The About us Page Ends Here ------------------------>













<!--------------------------- The Contact us Page starts Here ------------------------>
<!--------------------------- The Contact us Page starts Here ------------------------>

<section id="contact" class="section contact1 ttapp-contact" title="contact1">
  <div class="container-fluid py-5">
    <div class="row align-items-center">
      <!-- Left Text Section -->
      <div class="col-md-6 px-5">
        <h1 class="fw-bold mb-3">Contact {{ app_name }} in Ghana</h1>
        <p class="text-muted">
          Have questions about driving with {{ app_name }}? We're here for whatever you need.
        </p>
      </div>

      <!-- Right Image Section -->
      <div class="col-md-6">
        <img src="{{ url_for('static', filename='images/contact.PNG') }}" alt="Contact TTApp in Nigeria" class="img-fluid rounded">
      </div>
    </div>
  </div>
</section>

<section class="section contact1 ttapp-support py-5">
  <div class="container">
    <!-- Get More Information Section -->
    <div class="row mb-5">
      <div class="col-12 mb-4">
        <h3 class="fw-bold">Get more information</h3>
      </div>
      <div class="col-md-6 d-flex align-items-start">
        <img src="{{ url_for('static', filename='images/driver_app.PNG') }}" alt="Driver App Basics" class="me-3" style="width: 50px; height: 50px;">
        <div>
          <h5>Driver App Basics</h5>
          <p class="text-muted">Find information about how to take trips with the {{ app_name }}, where to see your earnings, and more.</p>
          <a href="#driver" id="drive" class="navigate text-primary text-dark">Learn more</a>
        </div>
      </div>
      <div class="col-md-6 d-flex align-items-start">
        <img src="{{ url_for('static', filename='images/help_img.PNG') }}" alt="Help Center" class="me-3" style="width: 50px; height: 50px;">
        <div>
          <h5>Help Center</h5>
          <p class="text-muted">Browse frequently asked questions from drivers.</p>
          <a href="#help" id="help1" class="navigate text-primary text-dark">Get help</a>
        </div>
      </div>
    </div>
    <br />
    <!-- In-Person Support Section -->
    <div class="row">
      <div class="col-md-6">
        <h3 class="fw-bold">In-person support</h3>
        <p class="text-muted">
          In some cities, you might be able to get support in person at a {{ app_name }} location.
        </p>
        <p class="text-muted">
          To check availability, go to <strong>Help</strong> in your Driver app, then <strong>Book an in-person appointment</strong>, choose the issue you need help with, and tap <strong>Schedule an appointment</strong> if you want more help. Or you can visit our website.
        </p>
        <h5>Business hours</h5>
        <ul class="list-unstyled text-muted">
          <li>Monday & Tuesday: 9am - 5pm</li>
          <li>Wednesday: 9am - 4:30pm</li>
          <li>Thursday & Friday: 9am - 5pm</li>
        </ul>
        <a href="#" class="text-primary text-dark">Book an appointment</a>
      </div>
      <div class="col-md-6 text-center">
        <img src="{{ url_for('static', filename='images/support.PNG') }}" alt="In-person Support" class="img-fluid">
      </div>
    </div>
  </div>
</section>

<!--------------------------- The Contact us Page Ends Here ------------------------>
<!--------------------------- The Contact us Page Ends Here ------------------------>











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











<!------------------- The Terms And Conditions Page starts Here ---------------------->
<!------------------- The Terms And Conditions Page starts Here ---------------------->

<section id="terms" class="section terms1 ttapp-terms py-5" title="terms1">
  <div class="container">
    <h1 class="text-center fw-bold mb-4">Terms and Conditions</h1>
    <p class="text-center text-muted mb-5">
      Please read these Terms and Conditions ("Terms", "Terms and Conditions") carefully before using the {{ app_name }} platform.
    </p>

    <div class="accordion" id="termsAccordion">
      <!-- Section 1 -->
      <div class="accordion-item">
        <h2 class="accordion-header" id="headingOne">
          <button
            class="accordion-button"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#collapseOne"
            aria-expanded="true"
            aria-controls="collapseOne">
            1. Introduction
          </button>
        </h2>
        <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#termsAccordion">
          <div class="accordion-body">
            Welcome to {{ app_name }}! By accessing or using our app, you agree to comply with and be bound by these terms. If you do not agree with any part of these terms, please do not use {{ app_name }}.
          </div>
        </div>
      </div>

      <!-- Section 2 -->
      <div class="accordion-item">
        <h2 class="accordion-header" id="headingTwo">
          <button
            class="accordion-button collapsed"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#collapseTwo"
            aria-expanded="false"
            aria-controls="collapseTwo">
            2. Eligibility
          </button>
        </h2>
        <div id="collapseTwo" class="accordion-collapse collapse" aria-labelledby="headingTwo" data-bs-parent="#termsAccordion">
          <div class="accordion-body">
            To use {{ app_name }}, you must be at least 18 years old and legally capable of entering into binding agreements. By registering, you confirm that you meet these eligibility requirements.
          </div>
        </div>
      </div>

      <!-- Section 3 -->
      <div class="accordion-item">
        <h2 class="accordion-header" id="headingThree">
          <button
            class="accordion-button collapsed"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#collapseThree"
            aria-expanded="false"
            aria-controls="collapseThree">
            3. User Responsibilities
          </button>
        </h2>
        <div id="collapseThree" class="accordion-collapse collapse" aria-labelledby="headingThree" data-bs-parent="#termsAccordion">
          <div class="accordion-body">
            Users are responsible for maintaining the confidentiality of their account information and ensuring all details provided are accurate. Any misuse of the {{ app_name }} platform may result in account suspension.
          </div>
        </div>
      </div>

      <!-- Section 4 -->
      <div class="accordion-item">
        <h2 class="accordion-header" id="headingFour">
          <button
            class="accordion-button collapsed"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#collapseFour"
            aria-expanded="false"
            aria-controls="collapseFour">
            4. Payments and Refunds
          </button>
        </h2>
        <div id="collapseFour" class="accordion-collapse collapse" aria-labelledby="headingFour" data-bs-parent="#termsAccordion">
          <div class="accordion-body">
            Payments made through {{ app_name }} are non-refundable unless explicitly stated otherwise. By using the platform, you agree to the payment terms outlined during your transaction.
          </div>
        </div>
      </div>

      <!-- Section 5 -->
      <div class="accordion-item">
        <h2 class="accordion-header" id="headingFive">
          <button
            class="accordion-button collapsed"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#collapseFive"
            aria-expanded="false"
            aria-controls="collapseFive">
            5. Limitation of Liability
          </button>
        </h2>
        <div id="collapseFive" class="accordion-collapse collapse" aria-labelledby="headingFive" data-bs-parent="#termsAccordion">
          <div class="accordion-body">
            {{ app_name }} is not liable for any direct, indirect, incidental, or consequential damages arising from the use or inability to use the platform. Users are encouraged to report any issues via the {{ app_name }} Help Center.
          </div>
        </div>
      </div>
    </div>

    <div class="text-center mt-4">
      <p class="text-muted">For further information, please contact <a href="mailto:support@ttapp.com" class="text-decoration-none">support@ttapp.com</a>.</p>
    </div>
  </div>
</section>

<!------------------- The Terms And Conditions Page Ends Here ---------------------->
<!------------------- The Terms And Conditions Page Ends Here ---------------------->













<!------------------- The Offering Page Starts Here ---------------------->
<!------------------- The Offering Page Starts Here ---------------------->

<section id="offering"  class="section offering1 ttapp-technology py-5" title="offering1">
  <div class="container text-center">
    <!-- Heading Section -->
    <h1 class="fw-bold">{{ app_name }}'s Technology Offerings</h1>
    <p class="mt-3">Changing how people can connect and move packages from point A to point B is just the beginning.</p>
    <button class="btn btn-dark mt-3">Explore the App</button>
  </div>

  <!-- Description Section -->
  <div class="container mt-5">
    <h2 class="fw-bold text-center mb-4">{{ app_name }} Apps, Products, and Other Offerings</h2>
    <div class="row">
      <div class="col-md-6">
        <p>
          {{ app_name }} is a technology company whose mission is to reimagine the way the world moves for the better.
          Our technology helps us develop and maintain multilateral platforms that match consumers looking for
          reliable delivery services. These platforms integrate a variety of transportation methods, such as
          couriers and personal drivers.
        </p>
      </div>
      <div class="col-md-6">
        <p>
          We also connect consumers and businesses, allowing them to send and receive packages conveniently.
          {{ app_name }}'s platform ensures seamless logistics between independent providers and recipients. With our
          global reach, {{ app_name }} supports movement in multiple cities and countries worldwide.
        </p>
      </div>
    </div>
  </div>

  <!-- Ride Options Section -->
  <div class="container mt-5 text-center">
    <h2 class="fw-bold">{{ app_name }}'s Most Popular Delivery Options</h2>
    <p class="mt-3">Send or receive packages quickly and reliably.</p>
    <div class="d-flex justify-content-center gap-4 mt-3">
      <a href="#" class="btn btn-outline-black">Download the App</a>
      <a href="#" class="btn btn-outline-secondary">See More Delivery Options</a>
    </div>
  </div>
</section>

<section class="section offering1 ttapp-services py-5">
  <div class="container">
    <!-- Delivery Options Section -->
    <div class="row text-center mb-5">
      <div class="col-md-4">
        <img src="{{ url_for('static', filename='images/offer1.PNG') }}" alt="TTApp Regular Delivery" class="img-fluid mb-3">
        <h4 class="fw-bold">{{ app_name }} Regular</h4>
        <p>Affordable deliveries for your everyday needs.</p>
        <a href="#" class="text-black">Learn more</a>
      </div>
      <div class="col-md-4">
        <img src="{{ url_for('static', filename='images/offer2.PNG') }}" alt="TTApp Shared Delivery" class="img-fluid mb-3">
        <h4 class="fw-bold">{{ app_name }} Shared</h4>
        <p>Share delivery costs with nearby senders.</p>
        <a href="#" class="text-black">Learn more</a>
      </div>
      <div class="col-md-4">
        <img src="{{ url_for('static', filename='images/offer3.PNG') }}" alt="TTApp Premium Delivery" class="img-fluid mb-3">
        <h4 class="fw-bold">{{ app_name }} Premium</h4>
        <p>Exclusive deliveries with extra care and speed.</p>
        <a href="#" class="text-black">Learn more</a>
      </div>
    </div>

    <!-- Additional Features Section -->
    <div class="row text-center">
      <div class="col-md-4">
        <div class="d-flex align-items-center justify-content-center mb-2">
          <i class="bi bi-shield-check fs-1 text-black"></i>
        </div>
        <h5 class="fw-bold">Safety</h5>
        <p>Experience peace of mind with every delivery.</p>
        <a href="#safety" id="safety1" class="navigate text-black">Learn more about safety</a>
      </div>
      <div class="col-md-4">
        <div class="d-flex align-items-center justify-content-center mb-2">
          <i class="bi bi-geo-alt fs-1 text-black"></i>
        </div>
        <h5 class="fw-bold">Coverage</h5>
        <p>Available in 10,000+ locations worldwide.</p>
        <a href="#" class="text-black">Find a location</a>
      </div>
      <div class="col-md-4">
        <div class="d-flex align-items-center justify-content-center mb-2">
          <i class="bi bi-airplane fs-1 text-black"></i>
        </div>
        <h5 class="fw-bold">Airports</h5>
        <p>Quick package transfers to and from 600+ airports.</p>
        <a href="#" class="text-black">See all airports</a>
      </div>
    </div>
  </div>
</section>

<section class="section offering1 ttapp-offers py-5">
  <div class="container">
    <!-- Food Delivery Section -->
    <div class="row mb-5">
      <div class="col-12">
        <h2 class="fw-bold mb-4">Food Delivery on Demand</h2>
      </div>
      <div class="col-md-6 mb-4">
        <img src="{{ url_for('static', filename='images/offer4.PNG') }}" class="img-fluid rounded" alt="TTApp Food Delivery">
        <h5 class="mt-3 fw-bold">{{ app_name }} Eats</h5>
        <p>Order from your favorite restaurants, online or via the {{ app_name }}. Restaurants will prepare your order, and a nearby delivery person will bring it to your door.</p>
        <a href="#eating" id="eat" class="navigate text-black">Visit {{ app_name }} Eats</a>
      </div>
      <div class="col-md-6 mb-4">
        <img src="{{ url_for('static', filename='images/offer5.PNG') }}" class="img-fluid rounded" alt="Partner with TTApp">
        <h5 class="mt-3 fw-bold">Restaurants</h5>
        <p>Expand your restaurant business by featuring your menu on {{ app_name }} Eats. Delight customers and grow your reach with fast and reliable food delivery.</p>
        <a href="#eating" id="eat" class="navigate text-black">Partner with {{ app_name }} Eats</a>
      </div>
    </div>

    <!-- Earning Opportunities Section -->
    <div class="row">
      <div class="col-12">
        <h2 class="fw-bold mb-4">Earn Money with {{ app_name }}</h2>
      </div>
      <div class="col-md-6 mb-4">
        <img src="{{ url_for('static', filename='images/offer6.PNG') }}" class="img-fluid rounded" alt="Drive with TTApp">
        <h5 class="mt-3 fw-bold">Drive with {{ app_name }}</h5>
        <p>Make the most of your time on the road by driving with {{ app_name }}. Join our network of active drivers and earn while exploring your city.</p>
        <a href="#signingup" id="signup" class="navigate text-black">Sign up to drive</a>
      </div>
      <div class="col-md-6 mb-4">
        <img src="{{ url_for('static', filename='images/offer7.PNG') }}" class="img-fluid rounded" alt="Deliver with TTApp">
        <h5 class="mt-3 fw-bold">Deliver with {{ app_name }}</h5>
        <p>Earn money delivering food orders, packages, and more with {{ app_name }}. Enjoy flexible hours and the freedom to choose your schedule.</p>
        <a href="#signingup" id="signup" class="navigate text-black">Sign up to deliver</a>
      </div>
    </div>
  </div>
</section>

<section class="section offering1 ttapp-initiatives py-5">
  <div class="container">
    <!-- Moving Cities Forward Section -->
    <div class="row mb-5">
      <div class="col-12">
        <h2 class="fw-bold mb-4">Moving Cities Forward, Together</h2>
      </div>
      <div class="col-md-6 mb-4">
        <img src="{{ url_for('static', filename='images/offer8.PNG') }}" class="img-fluid rounded" alt="Public Transportation">
        <h5 class="mt-3 fw-bold">Helping to improve public transportation for all</h5>
        <p>{{ app_name }} is committed to helping cities around the world make public transportation more accessible, equitable, and efficient.</p>
        <a href="#" class="text-black">Learn more about {{ app_name }} Transit</a>
      </div>
      <div class="col-md-6 mb-4">
        <img src="{{ url_for('static', filename='images/offer9.PNG') }}" class="img-fluid rounded" alt="Healthcare Access">
        <h5 class="mt-3 fw-bold">Providing access to care for those in need</h5>
        <p>We partner with healthcare organizations to provide their members and patients access to care by offering flexible ride-scheduling options.</p>
        <a href="#" class="text-black">Visit {{ app_name }} Health</a>
      </div>
    </div>

    <!-- Helping Businesses Move Ahead Section -->
    <div class="row">
      <div class="col-12">
        <h2 class="fw-bold mb-4">Helping Businesses Move Ahead</h2>
      </div>
      <div class="col-md-6 mb-4">
        <img src="{{ url_for('static', filename='images/offer10.PNG') }}" class="img-fluid rounded" alt="TTApp Freight">
        <h5 class="mt-3 fw-bold">{{ app_name }} Freight</h5>
        <p>{{ app_name }} Freight is a platform that matches carriers with shippers. Instantly book loads, with upfront pricing ensuring carriers always know how much they’ll earn.</p>
        <a href="#" class="text-black">Learn more about {{ app_name }} Freight</a>
      </div>
      <div class="col-md-6 mb-4">
        <img src="{{ url_for('static', filename='images/offer11.PNG') }}" class="img-fluid rounded" alt="TTApp for Business">
        <h5 class="mt-3 fw-bold">{{ app_name }} for Business</h5>
        <p>Whether it's employee travel or customer rides, {{ app_name }} for Business offers easy solutions for managing ground transportation with automated billing and reporting.</p>
        <a href="#business" id="biz" class="navigate text-black">Learn more about {{ app_name }} for Business</a>
      </div>
    </div>
  </div>
</section>


<!------------------- The Offering Page Ends Here ---------------------->
<!------------------- The Offering Page Ends Here ---------------------->












<!------------------- The safety Page Starts Here ---------------------->
<!------------------- The safety Page Starts Here ---------------------->

<section id="safety" class="section safety1 ttapp-safety py-5" title="safety1">
  <div class="container">
    <!-- Commitment to Safety -->
    <div class="row align-items-center mb-5">
      <div class="col-md-6">
        <h2 class="fw-bold">Our Commitment to Safety</h2>
        <p>
          We want you to move freely, make the most of your time, and stay connected to the people and places that matter most to you. 
          That's why we are committed to safety—from the creation of new standards to the development of technology with the aim of reducing incidents.
        </p>
      </div>
      <div class="col-md-6 text-center">
        <img src="{{ url_for('static', filename='images/safe1.PNG') }}" class="img-fluid rounded" alt="Commitment to Safety">
      </div>
    </div>

    <!-- Safety Features -->
    <div class="row text-center">
      <div class="col-12">
        <h2 class="fw-bold mb-4">How Safety is Built into Your Experience</h2>
      </div>
      <div class="col-md-4 mb-4">
        <h5 class="fw-bold">Safety Features in the App</h5>
        <p>
          Share your trip details with loved ones. Track your trip during your ride. Our technology helps put peace of mind at your fingertips.
        </p>
      </div>
      <div class="col-md-4 mb-4">
        <h5 class="fw-bold">An Inclusive Community</h5>
        <p>
          Millions of riders and drivers share a set of Community Guidelines, holding each other accountable to do the right thing.
        </p>
      </div>
      <div class="col-md-4 mb-4">
        <h5 class="fw-bold">Support at Every Turn</h5>
        <p>
          A specially trained team is available 24/7. Reach them in the app, day or night, with any questions or safety concerns.
        </p>
      </div>
    </div>
  </div>
</section>

<section class="section safety1 ttapp-safety-journeys py-5">
  <div class="container">
    <!-- Title -->
    <div class="row text-center mb-5">
      <div class="col-12">
        <h2 class="fw-bold">Building Safer Journeys for Everyone</h2>
      </div>
    </div>

    <!-- Driver and Rider Safety -->
    <div class="row">
      <!-- Driver Safety -->
      <div class="col-md-6 mb-4">
        <div class="card h-100 border-0 shadow-sm">
          <img src="{{ url_for('static', filename='images/safe2.PNG') }}" class="card-img-top rounded" alt="Driver Safety">
          <div class="card-body">
            <h5 class="card-title fw-bold">Driver Safety</h5>
            <p class="card-text">
              Count on 24/7 support to help with any questions or safety concerns. Share your trip with loved ones. Our focus is on your safety, so you can go where the opportunity is.
            </p>
            <a href="#" class="btn btn-link text-black">Learn more</a>
          </div>
        </div>
      </div>

      <!-- Rider Safety -->
      <div class="col-md-6 mb-4">
        <div class="card h-100 border-0 shadow-sm">
          <img src="{{ url_for('static', filename='images/safe3.PNG') }}" class="card-img-top rounded" alt="Rider Safety">
          <div class="card-body">
            <h5 class="card-title fw-bold">Rider Safety</h5>
            <p class="card-text">
              Millions of rides are requested every day. Every rider has access to safety features built into the app. And every ride has a support team if you need them.
            </p>
            <a href="#" class="btn btn-link text-black">Learn more</a>
          </div>
        </div>
      </div>
    </div>

    <!-- Quote Section -->
    <div class="row mt-5">
      <div class="col-12">
        <div class="bg-primary text-white p-4 rounded text-center">
          <blockquote class="blockquote">
            <p class="mb-0">
              “Every day, our technology puts millions of people together in cars in cities around the world. Helping keep people safe is a huge responsibility and one we do not take lightly.”
            </p>
            <br />
            <div class="blockquote-footer text-white">
              Mike Opare, {{ app_name }} CEO
            </div>
          </blockquote>
        </div>
      </div>
    </div>
  </div>
</section>

<!------------------- The safety Page Ends Here ---------------------->
<!------------------- The safety Page Ends Here ---------------------->










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
          <li><a href="#about_us" id="about" class="navigate">About us</a></li>
          <li><a href="#offering" id="offering1" class="navigate">Our offerings</a></li>
          <li><a href="#">Newsroom</a></li>
          <li><a href="#">Investors</a></li>
          <li><a href="#">Blog</a></li>
          <li><a href="#contact" id="contact1" class="navigate">Contact Us</a></li>
        </ul>
      </div>
      <div class="footer-column">
        <h4>Products</h4>
        <ul>
          <li><a href="#riding" id="ride" class="navigate">Ride</a></li>
          <li><a href="#driver" id="drive" class="navigate">Drive</a></li>
          <li><a href="#packaging" id="package1" class="navigate">Deliver</a></li>
          <li><a href="#">{{ app_name }} Freight</a></li>
          <li><a href="#">Gift cards</a></li>
        </ul>
      </div>
      <div class="footer-column">
        <h4>Global Citizenship</h4>
        <ul>
          <li><a href="#safety" id="safety1" class="navigate">Safety</a></li>
          <li><a href="#">Diversity and Inclusion</a></li>
          <li><a href="#">Sustainability</a></li>
        </ul>
      </div>
      <div class="footer-column">
        <h4>Travel</h4>
        <ul>
          <li><a href="#riding" id="ride" class="navigate">Reserve</a></li>
          <li><a href="#cities" id="cities1" class="navigate">Cities</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <div class="social-icons">
        <a href="https://www.facebook.com/profile.php?id=61566501765378&mibextid=ZbWKwL"><i class="fab fa-facebook"></i></a>
        <a href="https://x.com/thetrotroapp"><i class="fab fa-twitter"></i></a>
        <a href="http://www.youtube.com/@TheTrotroApp"><i class="fab fa-youtube"></i></a>
        <a href="https://www.linkedin.com/company/ttapp/"><i class="fab fa-linkedin"></i></a>
        <a href="https://www.instagram.com/thetrotroapp/"><i class="fab fa-instagram"></i></a>
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
        <li><a href="#privacy" id="privacy1" class="navigate">Privacy</a></li>
        <li><a href="#">Accessibility</a></li>
        <li><a href="#terms" id="terms1" class="navigate">Terms</a></li>
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
