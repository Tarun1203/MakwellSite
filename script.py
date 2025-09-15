# Create the main HTML structure for Makwell website based on Acer TV design
html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Makwell Electronics | Premium TVs, Washing Machines & Electronics</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <!-- Skip Navigation -->
    <a href="#main-content" class="skip-nav">Skip to content</a>
    
    <!-- Header -->
    <header class="header">
        <nav class="navbar">
            <div class="nav-container">
                <div class="nav-brand">
                    <img src="assets/images/logo.jpg" alt="Makwell" class="logo">
                </div>
                <ul class="nav-menu">
                    <li><a href="#home">Home</a></li>
                    <li><a href="#products">Products</a></li>
                    <li><a href="#about">About</a></li>
                    <li><a href="#support">Support</a></li>
                    <li><a href="#blogs">Blogs</a></li>
                </ul>
                <div class="nav-toggle">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            </div>
        </nav>
    </header>

    <!-- Main Content -->
    <main id="main-content">
        <!-- Hero Slider Section -->
        <section class="hero-slider">
            <div class="slider-container">
                <!-- Slide 1 -->
                <div class="slide active">
                    <div class="slide-content">
                        <h1 class="slide-title">
                            <span class="title-line">True-to-life</span>
                            <span class="title-line">cinematic visuals</span>
                        </h1>
                        <p class="slide-description">
                            Experience true-to-life visuals captivating you and take you deeper into everything you watch. 
                            The Quad core processor uses multiple algorithms to improve picture quality in real-time across 
                            five dimensions - Clarity, Contrast, Colour, Motion and Sharpness.
                        </p>
                    </div>
                </div>

                <!-- Slide 2 -->
                <div class="slide">
                    <div class="slide-content">
                        <h1 class="slide-title">
                            <span class="title-line">Spectacular</span>
                            <span class="title-line">audio experience</span>
                        </h1>
                        <p class="slide-description">
                            Immerse yourself in powerful, crystal-clear sound with our advanced audio technology. 
                            Experience every detail with precision-engineered speakers and Dolby Atmos support.
                        </p>
                    </div>
                </div>

                <!-- Slide 3 -->
                <div class="slide">
                    <div class="slide-content">
                        <h1 class="slide-title">
                            <span class="title-line">Your space</span>
                            <span class="title-line">Your choice</span>
                            <span class="title-line">Your theater</span>
                        </h1>
                        <p class="slide-description">
                            Transform any room into your personal cinema with our range of premium televisions 
                            designed to fit perfectly in your space.
                        </p>
                    </div>
                </div>

                <!-- Slide 4 -->
                <div class="slide">
                    <div class="slide-content">
                        <h1 class="slide-title">
                            <span class="title-line">Fast and efficient</span>
                            <span class="title-line">connectivity</span>
                        </h1>
                        <p class="slide-description">
                            Stay connected with advanced WiFi, Bluetooth, and multiple HDMI ports. 
                            Stream, cast, and connect all your devices seamlessly.
                        </p>
                    </div>
                </div>

                <!-- Slide 5 -->
                <div class="slide">
                    <div class="slide-content">
                        <h1 class="slide-title">
                            <span class="title-line">Next gen</span>
                            <span class="title-line">Configuration</span>
                        </h1>
                        <p class="slide-description">
                            Powered by the latest technology with advanced processors, AI-enhanced features, 
                            and smart connectivity for the ultimate viewing experience.
                        </p>
                    </div>
                </div>
            </div>

            <!-- Slider Navigation -->
            <div class="slider-nav">
                <button class="nav-dot active" data-slide="0"></button>
                <button class="nav-dot" data-slide="1"></button>
                <button class="nav-dot" data-slide="2"></button>
                <button class="nav-dot" data-slide="3"></button>
                <button class="nav-dot" data-slide="4"></button>
            </div>

            <!-- Slider Controls -->
            <button class="slider-btn prev" id="prevBtn">Previous</button>
            <button class="slider-btn next" id="nextBtn">Next</button>
        </section>

        <!-- Products Section -->
        <section class="products-section" id="products">
            <div class="container">
                <div class="products-grid">
                    <!-- Smart TV Series -->
                    <div class="product-card">
                        <div class="product-info">
                            <h3 class="product-title">Smart TV Series</h3>
                            <p class="product-sizes">24″HD | 32″HD | 43″UHD | 55″UHD | 65″UHD</p>
                            <p class="product-price">From ₹ 11,999/-</p>
                            <button class="product-btn">Know more</button>
                        </div>
                    </div>

                    <!-- Premium XL Series -->
                    <div class="product-card">
                        <div class="product-info">
                            <h3 class="product-title">Premium XL Series</h3>
                            <p class="product-sizes">70″UHD</p>
                            <p class="product-price">At ₹ 69,999/-</p>
                            <button class="product-btn">Know more</button>
                        </div>
                    </div>

                    <!-- QLED Series -->
                    <div class="product-card">
                        <div class="product-info">
                            <h3 class="product-title">QLED Series</h3>
                            <p class="product-sizes">32″HD | 43″UHD | 50″UHD | 55″UHD</p>
                            <p class="product-price">From ₹ 15,999/-</p>
                            <button class="product-btn">Know more</button>
                        </div>
                    </div>

                    <!-- Pro Series -->
                    <div class="product-card">
                        <div class="product-info">
                            <h3 class="product-title">Pro Series</h3>
                            <p class="product-sizes">43″UHD | 50″UHD | 55″UHD</p>
                            <p class="product-price">From ₹ 27,999/-</p>
                            <button class="product-btn">Know more</button>
                        </div>
                    </div>

                    <!-- Washing Machines -->
                    <div class="product-card">
                        <div class="product-info">
                            <h3 class="product-title">Washing Machines</h3>
                            <p class="product-sizes">7.0 KG | 9.0 KG | 11.0 KG</p>
                            <p class="product-price">From ₹ 12,999/-</p>
                            <button class="product-btn">Know more</button>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Blog Section -->
        <section class="blog-section" id="blogs">
            <div class="container">
                <div class="blog-header">
                    <h4 class="blog-category">BLOGS</h4>
                    <h2 class="blog-title">An in-depth exploration of our products</h2>
                    <button class="view-all-btn">View all</button>
                </div>
            </div>
        </section>
    </main>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>CONTACT US</h3>
                    <p>Get in touch with us for any product-related queries.</p>
                    <div class="contact-info">
                        <p>Email: makwellindia456@gmail.com</p>
                        <p>Phone: +91 99800 00515</p>
                        <p>Mon - Sun: 9:00 AM - 8:00 PM</p>
                    </div>
                </div>
                <div class="footer-section">
                    <h3>Follow us on</h3>
                    <div class="social-links">
                        <a href="#" class="social-link">Facebook</a>
                        <a href="#" class="social-link">Instagram</a>
                        <a href="#" class="social-link">YouTube</a>
                    </div>
                </div>
            </div>
        </div>
    </footer>

    <script src="script.js"></script>
</body>
</html>'''

# Save the HTML file
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Main HTML file created successfully!")