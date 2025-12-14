
document.addEventListener('DOMContentLoaded', () => {
    // BCI Disclaimer Logic
    const disclaimerBtn = document.getElementById('agree-btn');
    if (disclaimerBtn) {
        disclaimerBtn.addEventListener('click', () => {
            localStorage.setItem('bci_consent', 'true');
            window.location.href = 'home.html';
        });
    }

    // Redirect if consent valid (Optional: enables direct access if allowed)
    // if (window.location.pathname.includes('index.html') && localStorage.getItem('bci_consent')) {
    //    window.location.href = 'home.html';
    // }

    // Disagree Logic
    const disagreeBtn = document.getElementById('disagree-btn');
    if (disagreeBtn) {
        disagreeBtn.addEventListener('click', () => {
            window.close(); // Only works if script opened it
            document.body.innerHTML = '<div style="display:flex;justify-content:center;align-items:center;height:100vh;background:#faf9f6;color:#1a2332;font-family:sans-serif;"><h1>Access Denied. You must accept the disclaimer to proceed.</h1></div>';
        });
    }
    // Mobile Hamburger Menu
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');
    const dropdown = document.querySelector('.dropdown');

    if (hamburger) {
        hamburger.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            // Toggle Icon
            const icon = hamburger.querySelector('i');
            if (navLinks.classList.contains('active')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-times');
            } else {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });
    }

    // Mobile Dropdown Toggle
    if (dropdown && window.innerWidth <= 768) {
        const dropLink = dropdown.querySelector('a'); // The main 'Services' link
        dropLink.addEventListener('click', (e) => {
            e.preventDefault(); // Prevent navigating to services.html on first click
            dropdown.classList.toggle('active');
        });
    }

    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
        if (!hamburger.contains(e.target) && !navLinks.contains(e.target) && navLinks.classList.contains('active')) {
            navLinks.classList.remove('active');
            hamburger.querySelector('i').classList.remove('fa-times');
            hamburger.querySelector('i').classList.add('fa-bars');
        }
    });
});
