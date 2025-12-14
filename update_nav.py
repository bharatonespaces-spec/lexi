import os

# Define the old navigation block to replace
old_nav = """                <div class="nav-links">
                    <a href="../home.html">Home</a>
                    <a href="../home.html#about">About</a>
                    <a href="../home.html#services" class="active">Services</a>
                    <a href="../home.html#contact">Contact</a>
                </div>"""

# Define the new navigation block
new_nav = """                <div class="nav-links">
                    <a href="../home.html">Home</a>
                    <a href="../home.html#about">About</a>
                    <div class="dropdown">
                        <a href="services.html" class="active">Services <i class="fas fa-caret-down"></i></a>
                        <div class="dropdown-content">
                            <a href="mutual-consent-divorce.html">Mutual Consent Divorce</a>
                            <a href="contested-divorce.html">Contested Divorce</a>
                            <a href="marriage-registration.html">Marriage Registration</a>
                            <a href="child-custody.html">Child Custody</a>
                             <a href="domestic-violence.html">Domestic Violence</a>
                            <a href="498a-cases.html">498A Cases</a>
                            <a href="dispute-resolution.html">Dispute Resolution</a>
                            <a href="property-documentation.html">Property Documentation</a>
                            <a href="wills-registration.html">Wills & Probate</a>
                            <a href="succession-certificate.html">Succession Certificate</a>
                             <a href="consumer-court.html">Consumer Court</a>
                            <a href="housing-society.html">Housing Society Matters</a>
                        </div>
                    </div>
                    <a href="../home.html#contact">Contact</a>
                </div>"""

# Directory containing the pages
pages_dir = r"c:/Users/Aakanksha/.gemini/antigravity/scratch/lexi_services_website/pages"

# List all HTML files in the directory
for filename in os.listdir(pages_dir):
    if filename.endswith(".html") and filename != "services.html":
        filepath = os.path.join(pages_dir, filename)
        
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Check if the file contains the old nav
            if old_nav in content:
                # Replace content
                new_content = content.replace(old_nav, new_nav)
                
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                print(f"Updated: {filename}")
            else:
                # Try a looser match if exact match fails (e.g. whitespace)
                # This simple script assumes exact match, but let's see if it works first.
                print(f"Skipped (Pattern not found): {filename}")

        except Exception as e:
            print(f"Error processing {filename}: {e}")
