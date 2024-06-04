## Flask Application Design
**Problem:** Build a website that teaches e-commerce basics.

### HTML Files
- **home.html:** Main landing page that welcomes users and provides links to different sections of the website.
- **basics.html:** Contains the content on e-commerce basics, including topics like types of e-commerce businesses, building an e-commerce website, marketing strategies, and payment gateways.
- **success_stories.html:** Shares success stories of e-commerce businesses to provide inspiration and demonstrate the potential of e-commerce.
- **contact.html:** Provides contact information and a form for visitors to reach out with questions or inquiries.

### Routes
- **@app.route('/'):** Home page route that displays the content from **home.html**.
- **@app.route('/basics')**: Route for the e-commerce basics section, displaying content from **basics.html**.
- **@app.route('/success-stories')**: Route for the success stories section, displaying content from **success_stories.html**.
- **@app.route('/contact')**: Route that displays the contact page from **contact.html**.