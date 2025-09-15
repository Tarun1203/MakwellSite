# Create Support page
support_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Support | Makwell Electronics</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        .support-hero {
            background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
            color: white;
            text-align: center;
            padding: 150px 0 100px;
            margin-top: 80px;
        }
        
        .support-hero h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
        }
        
        .support-hero p {
            font-size: 1.25rem;
            opacity: 0.9;
        }
        
        .support-content {
            padding: 80px 0;
        }
        
        .support-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            margin-bottom: 60px;
        }
        
        .support-card {
            background: white;
            padding: 40px 30px;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }
        
        .support-card:hover {
            transform: translateY(-5px);
        }
        
        .support-card h3 {
            font-size: 1.5rem;
            margin-bottom: 20px;
            color: #333;
        }
        
        .support-card p {
            color: #666;
            margin-bottom: 20px;
            line-height: 1.6;
        }
        
        .contact-form {
            background: #f8f9fa;
            padding: 60px 40px;
            border-radius: 12px;
            max-width: 800px;
            margin: 0 auto;
        }
        
        .form-group {
            margin-bottom: 25px;
        }
        
        .form-group label {
            display: block;
            margin-bottom: 8px;
            font-weight: 500;
            color: #333;
        }
        
        .form-group input,
        .form-group textarea,
        .form-group select {
            width: 100%;
            padding: 15px;
            border: 1px solid #ddd;
            border-radius: 6px;
            font-size: 1rem;
            transition: border-color 0.3s ease;
        }
        
        .form-group input:focus,
        .form-group textarea:focus,
        .form-group select:focus {
            outline: none;
            border-color: #007bff;
        }
        
        .form-group textarea {
            height: 120px;
            resize: vertical;
        }
        
        .submit-btn {
            background: #007bff;
            color: white;
            border: none;
            padding: 15px 40px;
            border-radius: 6px;
            font-size: 1rem;
            font-weight: 500;
            cursor: pointer;
            transition: background-color 0.3s ease;
            width: 100%;
        }
        
        .submit-btn:hover {
            background: #0056b3;
        }
        
        .contact-details {
            background: white;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            margin-bottom: 40px;
        }
        
        .contact-item {
            display: flex;
            align-items: center;
            margin-bottom: 20px;
            padding: 15px;
            background: #f8f9fa;
            border-radius: 8px;
        }
        
        .contact-item strong {
            min-width: 100px;
            color: #333;
        }
        
        .whatsapp-btn {
            background: #25d366;
            color: white;
            text-decoration: none;
            padding: 15px 30px;
            border-radius: 25px;
            display: inline-block;
            font-weight: 500;
            transition: background-color 0.3s ease;
            margin-top: 20px;
        }
        
        .whatsapp-btn:hover {
            background: #1da851;
            text-decoration: none;
            color: white;
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
        <!-- Support Hero -->
        <section class="support-hero">
            <div class="container">
                <h1>Customer Support</h1>
                <p>We're here to help you with all your queries</p>
            </div>
        </section>

        <!-- Support Content -->
        <section class="support-content">
            <div class="container">
                <!-- Contact Details -->
                <div class="contact-details">
                    <h2 style="text-align: center; margin-bottom: 40px; color: #333;">Get in Touch</h2>
                    
                    <div class="contact-item">
                        <strong>Email:</strong>
                        <span>makwellindia456@gmail.com</span>
                    </div>
                    
                    <div class="contact-item">
                        <strong>Phone:</strong>
                        <span>+91 99800 00515</span>
                    </div>
                    
                    <div class="contact-item">
                        <strong>Hours:</strong>
                        <span>Mon - Sun: 9:00 AM - 8:00 PM</span>
                    </div>
                    
                    <div style="text-align: center;">
                        <a href="https://wa.me/919980000515" class="whatsapp-btn" target="_blank">
                            📱 Chat on WhatsApp
                        </a>
                    </div>
                </div>

                <!-- Support Options -->
                <div class="support-grid">
                    <div class="support-card">
                        <h3>Installation Support</h3>
                        <p>Need help with product installation? Our expert technicians are ready to assist you with professional installation services.</p>
                        <button class="product-btn">Request Installation</button>
                    </div>
                    
                    <div class="support-card">
                        <h3>Warranty Claims</h3>
                        <p>Having issues with your MAK WELL product? File a warranty claim and get quick resolution from our service team.</p>
                        <button class="product-btn">File Warranty Claim</button>
                    </div>
                    
                    <div class="support-card">
                        <h3>Technical Support</h3>
                        <p>Get technical assistance for troubleshooting, setup guides, and product usage tips from our expert support team.</p>
                        <button class="product-btn">Get Technical Help</button>
                    </div>
                    
                    <div class="support-card">
                        <h3>Service Request</h3>
                        <p>Schedule a service appointment for maintenance, repairs, or general check-up of your MAK WELL products.</p>
                        <button class="product-btn">Schedule Service</button>
                    </div>
                </div>

                <!-- Contact Form -->
                <div class="contact-form">
                    <h2 style="text-align: center; margin-bottom: 30px; color: #333;">Send us a Message</h2>
                    <form id="supportForm">
                        <div class="form-group">
                            <label for="name">Full Name *</label>
                            <input type="text" id="name" name="name" required>
                        </div>
                        
                        <div class="form-group">
                            <label for="email">Email Address *</label>
                            <input type="email" id="email" name="email" required>
                        </div>
                        
                        <div class="form-group">
                            <label for="phone">Phone Number *</label>
                            <input type="tel" id="phone" name="phone" required>
                        </div>
                        
                        <div class="form-group">
                            <label for="product">Product Category</label>
                            <select id="product" name="product">
                                <option value="">Select Product Category</option>
                                <option value="smart-tv">Smart TV</option>
                                <option value="washing-machine">Washing Machine</option>
                                <option value="stabilizer">Voltage Stabilizer</option>
                                <option value="iron">Electric Iron</option>
                                <option value="other">Other Electronics</option>
                            </select>
                        </div>
                        
                        <div class="form-group">
                            <label for="model">Product Model (if applicable)</label>
                            <input type="text" id="model" name="model" placeholder="e.g., MW-43UHD-2024">
                        </div>
                        
                        <div class="form-group">
                            <label for="issue">Issue Type</label>
                            <select id="issue" name="issue">
                                <option value="">Select Issue Type</option>
                                <option value="installation">Installation Support</option>
                                <option value="warranty">Warranty Claim</option>
                                <option value="technical">Technical Issue</option>
                                <option value="service">Service Request</option>
                                <option value="complaint">Complaint</option>
                                <option value="feedback">Feedback</option>
                                <option value="other">Other</option>
                            </select>
                        </div>
                        
                        <div class="form-group">
                            <label for="message">Message *</label>
                            <textarea id="message" name="message" placeholder="Please describe your query or issue in detail..." required></textarea>
                        </div>
                        
                        <button type="submit" class="submit-btn">Send Message</button>
                    </form>
                </div>

                <!-- FAQ Section -->
                <div style="margin-top: 80px;">
                    <h2 style="text-align: center; margin-bottom: 40px; color: #333;">Frequently Asked Questions</h2>
                    
                    <div style="max-width: 800px; margin: 0 auto;">
                        <div style="margin-bottom: 30px; padding: 25px; background: white; border-radius: 8px; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);">
                            <h3 style="color: #333; margin-bottom: 15px;">What is the warranty period for MAK WELL products?</h3>
                            <p style="color: #666; line-height: 1.6; margin: 0;">TVs come with 2-3 years warranty, washing machines with 3 years warranty, and other electronics with 1-2 years warranty depending on the product.</p>
                        </div>
                        
                        <div style="margin-bottom: 30px; padding: 25px; background: white; border-radius: 8px; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);">
                            <h3 style="color: #333; margin-bottom: 15px;">How do I schedule an installation?</h3>
                            <p style="color: #666; line-height: 1.6; margin: 0;">You can schedule installation by calling our support number +91 99800 00515 or by filling out the contact form above with "Installation Support" selected.</p>
                        </div>
                        
                        <div style="margin-bottom: 30px; padding: 25px; background: white; border-radius: 8px; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);">
                            <h3 style="color: #333; margin-bottom: 15px;">Where can I find service centers?</h3>
                            <p style="color: #666; line-height: 1.6; margin: 0;">We have over 500 service centers across India. Contact us with your location and we'll provide details of the nearest service center.</p>
                        </div>
                        
                        <div style="margin-bottom: 30px; padding: 25px; background: white; border-radius: 8px; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);">
                            <h3 style="color: #333; margin-bottom: 15px;">How do I register my product?</h3>
                            <p style="color: #666; line-height: 1.6; margin: 0;">Product registration can be done by calling our customer care or by sending us your purchase details via email to makwellindia456@gmail.com.</p>
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
    <script>
        // Support form handling
        document.getElementById('supportForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Get form data
            const formData = new FormData(this);
            const data = Object.fromEntries(formData);
            
            // Basic validation
            if (!data.name || !data.email || !data.phone || !data.message) {
                alert('Please fill in all required fields.');
                return;
            }
            
            // Simulate form submission
            alert('Thank you for your message! We will get back to you within 24 hours.');
            this.reset();
        });
    </script>
</body>
</html>'''

with open('support.html', 'w', encoding='utf-8') as f:
    f.write(support_html)

print("Support page created successfully!")