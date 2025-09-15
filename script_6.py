# Create Blogs page
blogs_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blogs | Makwell Electronics</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        .blogs-hero {
            background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
            color: white;
            text-align: center;
            padding: 150px 0 100px;
            margin-top: 80px;
        }
        
        .blogs-hero h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
        }
        
        .blogs-hero p {
            font-size: 1.25rem;
            opacity: 0.9;
        }
        
        .blogs-content {
            padding: 80px 0;
        }
        
        .blog-tabs {
            display: flex;
            justify-content: center;
            margin-bottom: 50px;
            border-bottom: 1px solid #e5e5e5;
        }
        
        .blog-tab {
            padding: 15px 30px;
            background: none;
            border: none;
            font-size: 1.1rem;
            font-weight: 500;
            color: #666;
            cursor: pointer;
            border-bottom: 3px solid transparent;
            transition: all 0.3s ease;
        }
        
        .blog-tab.active {
            color: #007bff;
            border-bottom-color: #007bff;
        }
        
        .blog-tab:hover {
            color: #007bff;
        }
        
        .blog-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 30px;
        }
        
        .blog-card {
            background: white;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .blog-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.15);
        }
        
        .blog-image {
            height: 200px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 3rem;
        }
        
        .blog-content {
            padding: 30px;
        }
        
        .blog-date {
            color: #666;
            font-size: 0.9rem;
            margin-bottom: 10px;
        }
        
        .blog-title {
            font-size: 1.5rem;
            font-weight: 600;
            color: #333;
            margin-bottom: 15px;
            line-height: 1.3;
        }
        
        .blog-excerpt {
            color: #666;
            line-height: 1.6;
            margin-bottom: 20px;
        }
        
        .read-more-btn {
            background: #007bff;
            color: white;
            text-decoration: none;
            padding: 10px 20px;
            border-radius: 6px;
            font-weight: 500;
            display: inline-block;
            transition: background-color 0.3s ease;
        }
        
        .read-more-btn:hover {
            background: #0056b3;
            text-decoration: none;
            color: white;
        }
        
        .tab-content {
            display: none;
        }
        
        .tab-content.active {
            display: block;
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
        <!-- Blogs Hero -->
        <section class="blogs-hero">
            <div class="container">
                <h1>BLOGS</h1>
                <p>An in-depth exploration of our products and technology</p>
            </div>
        </section>

        <!-- Blogs Content -->
        <section class="blogs-content">
            <div class="container">
                <!-- Blog Tabs -->
                <div class="blog-tabs">
                    <button class="blog-tab active" data-tab="blogs">Blogs</button>
                    <button class="blog-tab" data-tab="press">Press Release</button>
                </div>

                <!-- Blogs Tab Content -->
                <div class="tab-content active" id="blogs">
                    <div class="blog-grid">
                        <article class="blog-card">
                            <div class="blog-image">📺</div>
                            <div class="blog-content">
                                <div class="blog-date">September 10, 2024</div>
                                <h3 class="blog-title">The Evolution of Smart TV Technology: What Makes MAK WELL TVs Special</h3>
                                <p class="blog-excerpt">
                                    Discover how smart TV technology has evolved and what makes MAK WELL televisions 
                                    stand out in today's competitive market with cutting-edge features and affordable pricing.
                                </p>
                                <a href="#" class="read-more-btn">Know more</a>
                            </div>
                        </article>

                        <article class="blog-card">
                            <div class="blog-image">🔊</div>
                            <div class="blog-content">
                                <div class="blog-date">September 5, 2024</div>
                                <h3 class="blog-title">Immerse Yourself in Sound: Exploring the Magic of Dolby Atmos in MAK WELL TVs</h3>
                                <p class="blog-excerpt">
                                    Experience cinema-quality audio at home with Dolby Atmos technology. Learn how 
                                    MAK WELL TVs deliver immersive sound that brings your favorite content to life.
                                </p>
                                <a href="#" class="read-more-btn">Know more</a>
                            </div>
                        </article>

                        <article class="blog-card">
                            <div class="blog-image">🖥️</div>
                            <div class="blog-content">
                                <div class="blog-date">August 28, 2024</div>
                                <h3 class="blog-title">4K vs Full HD: Choosing the Right Resolution for Your Home</h3>
                                <p class="blog-excerpt">
                                    Understanding the differences between 4K Ultra HD and Full HD displays. 
                                    Get expert advice on selecting the perfect TV resolution for your viewing needs.
                                </p>
                                <a href="#" class="read-more-btn">Know more</a>
                            </div>
                        </article>

                        <article class="blog-card">
                            <div class="blog-image">🏠</div>
                            <div class="blog-content">
                                <div class="blog-date">August 20, 2024</div>
                                <h3 class="blog-title">Smart Home Integration: Connecting Your MAK WELL TV to Your Digital Ecosystem</h3>
                                <p class="blog-excerpt">
                                    Learn how to integrate your MAK WELL smart TV with other smart home devices 
                                    for a seamless connected living experience.
                                </p>
                                <a href="#" class="read-more-btn">Know more</a>
                            </div>
                        </article>

                        <article class="blog-card">
                            <div class="blog-image">👪</div>
                            <div class="blog-content">
                                <div class="blog-date">August 15, 2024</div>
                                <h3 class="blog-title">Creating the Perfect Family Entertainment Center with MAK WELL Products</h3>
                                <p class="blog-excerpt">
                                    Design the ultimate family entertainment space with MAK WELL TVs and accessories. 
                                    Tips for optimizing your living room for maximum enjoyment.
                                </p>
                                <a href="#" class="read-more-btn">Know more</a>
                            </div>
                        </article>

                        <article class="blog-card">
                            <div class="blog-image">⚡</div>
                            <div class="blog-content">
                                <div class="blog-date">August 10, 2024</div>
                                <h3 class="blog-title">Energy Efficiency in Modern Electronics: How MAK WELL Saves You Money</h3>
                                <p class="blog-excerpt">
                                    Explore the energy-saving features in MAK WELL products and learn how 
                                    modern electronics can reduce your electricity bills while being eco-friendly.
                                </p>
                                <a href="#" class="read-more-btn">Know more</a>
                            </div>
                        </article>
                    </div>
                </div>

                <!-- Press Release Tab Content -->
                <div class="tab-content" id="press">
                    <div class="blog-grid">
                        <article class="blog-card">
                            <div class="blog-image">📢</div>
                            <div class="blog-content">
                                <div class="blog-date">September 12, 2024</div>
                                <h3 class="blog-title">MAK WELL Launches New 70" Premium XL Series TV</h3>
                                <p class="blog-excerpt">
                                    MAK WELL announces the launch of its largest TV yet - the 70" Premium XL Series 
                                    with advanced 4K technology and immersive audio experience at an competitive price.
                                </p>
                                <a href="#" class="read-more-btn">Know more</a>
                            </div>
                        </article>

                        <article class="blog-card">
                            <div class="blog-image">🏆</div>
                            <div class="blog-content">
                                <div class="blog-date">August 25, 2024</div>
                                <h3 class="blog-title">MAK WELL Wins "Best Value Electronics Brand" Award</h3>
                                <p class="blog-excerpt">
                                    MAK WELL Electronics has been recognized as the "Best Value Electronics Brand" 
                                    by the Consumer Electronics Association of India for the second consecutive year.
                                </p>
                                <a href="#" class="read-more-btn">Know more</a>
                            </div>
                        </article>

                        <article class="blog-card">
                            <div class="blog-image">🌱</div>
                            <div class="blog-content">
                                <div class="blog-date">August 18, 2024</div>
                                <h3 class="blog-title">MAK WELL Commits to Carbon Neutral Manufacturing by 2025</h3>
                                <p class="blog-excerpt">
                                    As part of its sustainability initiative, MAK WELL announces ambitious plans 
                                    to achieve carbon neutral manufacturing operations across all facilities by 2025.
                                </p>
                                <a href="#" class="read-more-btn">Know more</a>
                            </div>
                        </article>

                        <article class="blog-card">
                            <div class="blog-image">📈</div>
                            <div class="blog-content">
                                <div class="blog-date">July 30, 2024</div>
                                <h3 class="blog-title">MAK WELL Reports 40% Growth in Q2 2024</h3>
                                <p class="blog-excerpt">
                                    MAK WELL Electronics reports strong quarterly performance with 40% year-over-year 
                                    growth driven by increased demand for smart TVs and home appliances.
                                </p>
                                <a href="#" class="read-more-btn">Know more</a>
                            </div>
                        </article>
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
    <script>
        // Blog tabs functionality
        document.addEventListener('DOMContentLoaded', function() {
            const blogTabs = document.querySelectorAll('.blog-tab');
            const tabContents = document.querySelectorAll('.tab-content');

            blogTabs.forEach(tab => {
                tab.addEventListener('click', function() {
                    const targetTab = this.getAttribute('data-tab');

                    // Remove active class from all tabs and contents
                    blogTabs.forEach(t => t.classList.remove('active'));
                    tabContents.forEach(content => content.classList.remove('active'));

                    // Add active class to clicked tab and corresponding content
                    this.classList.add('active');
                    document.getElementById(targetTab).classList.add('active');
                });
            });

            // Handle read more buttons
            const readMoreBtns = document.querySelectorAll('.read-more-btn');
            readMoreBtns.forEach(btn => {
                btn.addEventListener('click', function(e) {
                    e.preventDefault();
                    const blogTitle = this.closest('.blog-content').querySelector('.blog-title').textContent;
                    alert(`Opening: ${blogTitle}`);
                });
            });
        });
    </script>
</body>
</html>'''

with open('blogs.html', 'w', encoding='utf-8') as f:
    f.write(blogs_html)

print("Blogs page created successfully!")