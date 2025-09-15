# Create additional pages to complete the website structure

# Products page
products_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Products | Makwell Electronics</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        .products-hero {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-align: center;
            padding: 150px 0 100px;
            margin-top: 80px;
        }
        
        .products-hero h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
        }
        
        .products-hero p {
            font-size: 1.25rem;
            opacity: 0.9;
        }
        
        .product-details {
            padding: 80px 0;
        }
        
        .product-category {
            margin-bottom: 60px;
        }
        
        .category-title {
            font-size: 2rem;
            margin-bottom: 30px;
            color: #333;
            border-bottom: 3px solid #007bff;
            display: inline-block;
            padding-bottom: 10px;
        }
        
        .product-specs {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
        }
        
        .spec-card {
            background: white;
            border: 1px solid #e5e5e5;
            border-radius: 8px;
            padding: 30px;
            text-align: center;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .spec-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
        }
        
        .spec-card h3 {
            font-size: 1.5rem;
            margin-bottom: 15px;
            color: #333;
        }
        
        .spec-list {
            list-style: none;
            margin-bottom: 20px;
        }
        
        .spec-list li {
            padding: 5px 0;
            color: #666;
        }
        
        .price-tag {
            font-size: 1.5rem;
            font-weight: 700;
            color: #007bff;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <!-- Header -->
    <header class="header">
        <nav class="navbar">
            <div class="nav-container">
                <div class="nav-brand">
                    <img src="assets/images/logo.jpg" alt="Makwell" class="logo">
                </div>
                <ul class="nav-menu">
                    <li><a href="index.html">Home</a></li>
                    <li><a href="products.html">Products</a></li>
                    <li><a href="about.html">About</a></li>
                    <li><a href="support.html">Support</a></li>
                    <li><a href="blogs.html">Blogs</a></li>
                </ul>
                <div class="nav-toggle">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            </div>
        </nav>
    </header>

    <main>
        <!-- Products Hero -->
        <section class="products-hero">
            <div class="container">
                <h1>Our Products</h1>
                <p>Discover our complete range of premium electronics</p>
            </div>
        </section>

        <!-- Product Details -->
        <section class="product-details">
            <div class="container">
                <!-- Smart TVs -->
                <div class="product-category">
                    <h2 class="category-title">Smart TVs & LED TVs</h2>
                    <div class="product-specs">
                        <div class="spec-card">
                            <h3>24" HD Smart TV</h3>
                            <ul class="spec-list">
                                <li>HD Ready 1366×768</li>
                                <li>Android 11</li>
                                <li>24W HiFi Speakers</li>
                                <li>Chromecast Built-in</li>
                                <li>Voice Control</li>
                            </ul>
                            <div class="price-tag">₹ 11,999</div>
                            <button class="product-btn">Know more</button>
                        </div>
                        
                        <div class="spec-card">
                            <h3>32" HD Smart TV</h3>
                            <ul class="spec-list">
                                <li>HD Ready 1366×768</li>
                                <li>Android 11</li>
                                <li>30W HiFi Speakers</li>
                                <li>Chromecast Built-in</li>
                                <li>Voice Control</li>
                            </ul>
                            <div class="price-tag">₹ 13,999</div>
                            <button class="product-btn">Know more</button>
                        </div>
                        
                        <div class="spec-card">
                            <h3>43" UHD 4K Smart TV</h3>
                            <ul class="spec-list">
                                <li>4K Ultra HD 3840×2160</li>
                                <li>Android 11</li>
                                <li>30W HiFi Speakers</li>
                                <li>HDR10+ Support</li>
                                <li>Voice Control</li>
                            </ul>
                            <div class="price-tag">₹ 24,999</div>
                            <button class="product-btn">Know more</button>
                        </div>
                        
                        <div class="spec-card">
                            <h3>55" UHD 4K Smart TV</h3>
                            <ul class="spec-list">
                                <li>4K Ultra HD 3840×2160</li>
                                <li>Android 11</li>
                                <li>40W HiFi Speakers</li>
                                <li>HDR10+ with Dolby Vision</li>
                                <li>Voice Control</li>
                            </ul>
                            <div class="price-tag">₹ 34,999</div>
                            <button class="product-btn">Know more</button>
                        </div>
                        
                        <div class="spec-card">
                            <h3>65" UHD 4K Smart TV</h3>
                            <ul class="spec-list">
                                <li>4K Ultra HD 3840×2160</li>
                                <li>Android 11</li>
                                <li>50W HiFi Speakers</li>
                                <li>HDR10+ with Dolby Vision</li>
                                <li>Voice Control</li>
                            </ul>
                            <div class="price-tag">₹ 44,999</div>
                            <button class="product-btn">Know more</button>
                        </div>
                    </div>
                </div>

                <!-- Washing Machines -->
                <div class="product-category">
                    <h2 class="category-title">Washing Machines</h2>
                    <div class="product-specs">
                        <div class="spec-card">
                            <h3>7.0 KG Semi-Automatic</h3>
                            <ul class="spec-list">
                                <li>7.0 KG Capacity</li>
                                <li>Toughened Glass Top</li>
                                <li>Diamond Steel Drum</li>
                                <li>Wind Jet Dry</li>
                                <li>3 Year Warranty</li>
                            </ul>
                            <div class="price-tag">₹ 12,999</div>
                            <button class="product-btn">Know more</button>
                        </div>
                        
                        <div class="spec-card">
                            <h3>9.0 KG Semi-Automatic</h3>
                            <ul class="spec-list">
                                <li>9.0 KG Capacity</li>
                                <li>Toughened Glass Top</li>
                                <li>Diamond Steel Drum</li>
                                <li>Wind Jet Dry</li>
                                <li>3 Year Warranty</li>
                            </ul>
                            <div class="price-tag">₹ 15,999</div>
                            <button class="product-btn">Know more</button>
                        </div>
                        
                        <div class="spec-card">
                            <h3>11.0 KG Semi-Automatic</h3>
                            <ul class="spec-list">
                                <li>11.0 KG Capacity</li>
                                <li>Toughened Glass Top</li>
                                <li>Diamond Steel Drum</li>
                                <li>Wind Jet Dry</li>
                                <li>3 Year Warranty</li>
                            </ul>
                            <div class="price-tag">₹ 18,999</div>
                            <button class="product-btn">Know more</button>
                        </div>
                    </div>
                </div>

                <!-- Electronics -->
                <div class="product-category">
                    <h2 class="category-title">Electronics & Appliances</h2>
                    <div class="product-specs">
                        <div class="spec-card">
                            <h3>Voltage Stabilizer 500VA</h3>
                            <ul class="spec-list">
                                <li>500VA Capacity</li>
                                <li>Digital Display</li>
                                <li>Overload Protection</li>
                                <li>Wide Input Range</li>
                                <li>2 Year Warranty</li>
                            </ul>
                            <div class="price-tag">₹ 2,999</div>
                            <button class="product-btn">Know more</button>
                        </div>
                        
                        <div class="spec-card">
                            <h3>Voltage Stabilizer 750W</h3>
                            <ul class="spec-list">
                                <li>750W Capacity</li>
                                <li>Digital Display</li>
                                <li>Overload Protection</li>
                                <li>Wide Input Range</li>
                                <li>2 Year Warranty</li>
                            </ul>
                            <div class="price-tag">₹ 3,999</div>
                            <button class="product-btn">Know more</button>
                        </div>
                        
                        <div class="spec-card">
                            <h3>Electric Iron 750W</h3>
                            <ul class="spec-list">
                                <li>750W Power</li>
                                <li>Non-stick Coating</li>
                                <li>Variable Temperature</li>
                                <li>Auto Shut-off</li>
                                <li>1 Year Warranty</li>
                            </ul>
                            <div class="price-tag">₹ 899</div>
                            <button class="product-btn">Know more</button>
                        </div>
                        
                        <div class="spec-card">
                            <h3>Electric Iron 1000W</h3>
                            <ul class="spec-list">
                                <li>1000W Power</li>
                                <li>Non-stick Coating</li>
                                <li>Variable Temperature</li>
                                <li>Auto Shut-off</li>
                                <li>1 Year Warranty</li>
                            </ul>
                            <div class="price-tag">₹ 1,199</div>
                            <button class="product-btn">Know more</button>
                        </div>
                    </div>
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

with open('products.html', 'w', encoding='utf-8') as f:
    f.write(products_html)

print("Products page created successfully!")