# **Testing**

## **Table of content**

* [Testing User Stories](#testing-user-stories)
* [Code Validation](#code-validation)
    * [JSX](#jsx)
    * [CSS](#css)
    * [Lighthouse](#lighthouse)

## **Testing User Stories**

<hr>

## **Site Navigation** [#1](https://github.com/users/AVTpepper/projects/5/views/2?pane=issue&itemId=25686907)

### Issue 1: Homepage Design & Layout [#12](https://github.com/AVTpepper/onestop-artist-shop/issues/12)

As a **visitor**, I can **see a visually appealing and easy-to-navigate homepage** so that I can **explore the artist's work and website sections with ease**.

| **Test** | Issue | Result |
| --- | --- | --- |
| 1 | Homepage should have a clean and visually appealing design that represents the artist's brand identity | PASS |
| 2 | Homepage should display a hero image or slider showcasing the artist's work | PASS |
| 3 | Homepage should include clear call-to-action (CTA) buttons that direct users to the most important sections | PASS |
| 4 | Homepage should be responsive and work well on various screen sizes and devices | PASS |

### Issue 2: Shop Product Listing Page [#13](https://github.com/AVTpepper/onestop-artist-shop/issues/13)

As a **visitor**, I can **browse through the available artworks and products** so that I can **find and select items to purchase**.

| **Test** | Issue | Result |
| --- | --- | --- |
| 1 | Product listing page should display a grid or list of products with images, titles, and prices | PASS |
| 2 | Products should be organized by categories or types | PASS |
| 3 | Product listing page should be responsive and work well on various screen sizes and devices | PASS |

### Issue 3: Basic Product Detail Page [#14](https://github.com/AVTpepper/onestop-artist-shop/issues/14)

As a **visitor**, I can **view the details of a specific artwork or product** so that I can **make an informed decision before purchasing**.

| **Test** | Issue | Result |
| --- | --- | --- |
| 1 | Product detail page should display a large image, title, description, price, and an "Add to Cart" button | PASS |
| 2 | Page should be responsive and work well on various screen sizes and devices | PASS |

### Issue 4: Shopping Cart Functionality [#15](https://github.com/AVTpepper/onestop-artist-shop/issues/15)

As a **registered user**, I can **add products to my shopping cart** so that I can **review and purchase them later**.

| **Test** | Issue | Result |
| --- | --- | --- |
| 1 | Users should be able to add products to the shopping cart from the product detail page | PASS |
| 2 | Users should be able to view their shopping cart with a list of added products, including images, titles, prices, and quantities | PASS |
| 3 | The shopping cart should be accessible from any page on the website | PASS |

### Issue 5: Basic Newsletter Signup [#16](https://github.com/AVTpepper/onestop-artist-shop/issues/16)

As a **visitor**, I can **sign up for the artist's newsletter** so that I can **receive updates on new artworks, events, and promotions**.

| **Test** | Issue | Result |
| --- | --- | --- |
| 1 | The newsletter signup form should be accessible from the homepage or a dedicated newsletter page | PASS |
| 2 | Users should be able to submit their email address through the form | PASS |
| 3 | The form should include GDPR compliance elements, such as a consent checkbox and a link to the privacy policy | NOT IMPLEMENTED |

### Issue 16: Events/Exhibitions Page [#27](https://github.com/AVTpepper/onestop-artist-shop/issues/27) (not yet implemented)

As a **visitor**, I can **view a list of the artist's upcoming and past events or exhibitions** so that I can **attend or learn about their work in a broader context**.

| **Test** | Issue | Result |
| --- | --- | --- |
| 1 | The Events/Exhibitions page should display a list of events, including titles, dates, locations, and descriptions | NOT IMPLEMENTED |
| 2 | The events should be organized by date, with upcoming events listed first | NOT IMPLEMENTED |
| 3 | The page should be responsive and work well on various screen sizes and devices | NOT IMPLEMENTED |

### Issue 6: About Page Content [#17](https://github.com/AVTpepper/onestop-artist-shop/issues/17)

As a **visitor**, I can **learn more about the artist's background and artistic vision** so that I can **connect with their work on a deeper level**.

| **Test** | Issue | Result |
| --- | --- | --- |
| 1 | The About page should include the artist's bio, artist statement, resume/CV, and press mentions | NOT IMPLEMENTED |
| 2 | A professional photo or video of the artist should be displayed on the About page | PASS |
| 3 | The page should be responsive and work well on various screen sizes and devices | PASS |

### Issue 10: Backend Support for Newsletter Signup [#21](https://github.com/AVTpepper/onestop-artist-shop/issues/21) (not fully implemented)

As an **administrator**, I can **manage newsletter subscriptions** so that I can **send updates and promotional content to subscribers**.

| **Test** | Issue | Result |
| --- | --- | --- |
| 1 | The backend should store and manage newsletter subscriber data | PASS |
| 2 | The backend should integrate with an email marketing platform (e.g., Mailchimp, SendGrid) for sending newsletters | PASS |
| 3 | Test the newsletter subscription functionality and integration | PASS |

### Issue: Docstrings for functions and classes [#29](https://github.com/AVTpepper/onestop-artist-shop/issues/29)

As a **developer**, I can **understand the purpose of functions and classes in the codebase**, so that I can **easily maintain and update the project**.

| **Test** | Issue | Result |
| --- | --- | --- |
| 1 | All functions and classes in the codebase should have clear and concise docstrings | PASS |
| 2 | The docstrings should follow a consistent format | PASS |
| 3 | The docstrings should provide necessary information about the purpose, arguments, and return values of the functions and classes | PASS |

### Issue 13: Basic Contact Form [#24](https://github.com/AVTpepper/onestop-artist-shop/issues/24) (not implemented yet)

As a **visitor**, I can **submit a message to the artist using a contact form**, so that I can **ask questions or provide feedback**.

| **Test** | Issue | Result |
| --- | --- | --- |
| 1 | The contact form should include fields for the user's name, email address, subject, and message | NOT YET TESTED |
| 2 | The form should validate user input and provide feedback on successful submission or errors | NOT YET TESTED |
| 3 | The form should send the submitted message to the artist's email address | NOT YET TESTED |

### Issue 12: Basic Search Functionality [#23](https://github.com/AVTpepper/onestop-artist-shop/issues/23) (not yet implemented)

As a **visitor**, I can **search for specific artworks and products using keywords**, so that I can **easily find the items I'm interested in**.

| **Test** | Issue | Result |
| --- | --- | --- |
| 1 | Users should be able to enter keywords into a search bar and receive relevant search results | NOT YET TESTED |
| 2 | Search results should display in a list or grid format, similar to the product listing page | NOT YET TESTED |
| 3 | The search functionality should be accessible from any page on the website | NOT YET TESTED |

### Issue 9: Order Processing and Management [#20](https://github.com/AVTpepper/onestop-artist-shop/issues/20)

As an **administrator**, I can **manage orders placed by customers**, so that I can **fulfill and track them efficiently**.

| **Test** | Issue | Result |
| --- | --- | --- |
| 1 | The backend should handle order processing, including creating, updating, and deleting orders | PASS |
| 2 | The backend should support order status updates (e.g., pending, processing, shipped, completed) | NOT IMPLEMENTED |
| 3 | The backend should provide an interface for the administrator to manage and track orders | PASS |

### Issue 11: Basic User Registration and Login [#22](https://github.com/AVTpepper/onestop-artist-shop/issues/22)

As a **visitor**, I can **create an account and log in**, so that I can **access exclusive features, such as saving my shopping cart and viewing my order history**.

| **Test** | Issue | Result |
| --- | --- | --- |
| 1 | Users should be able to register with their email address, a username, a password, and other necessary details | PASS |
| 2 | Users should be able to log in with their email address / username, and password | PASS |
| 3 | The login and registration process should be secure and include validation checks | PASS |

### Issue 14: Order History for Registered Users [#25](https://github.com/AVTpepper/onestop-artist-shop/issues/25)

As a **registered user**, I can **view my order history**, so that I can **keep track of my purchases and their status**.

| **Test** | Issue | Result |
| --- | --- | --- |
| 1 | Users should be able to access a page listing their previous orders | PASS |
| 2 | The order history page should display order details, such as order number, date, items, and status | PASS |
| 3 | The page should be responsive and work well on various screen sizes and devices | PASS |

### Issue 15: Blog Page Design and Setup [#26](https://github.com/AVTpepper/onestop-artist-shop/issues/26)

As a **visitor**, I can **read the artist's blog posts**, so that I can **learn more about their creative process, inspirations, and news**.

| **Test** | Issue | Result |
| --- | --- | --- |
| 1 | The blog page should display a list of blog posts, including titles, images, and post excerpts | PASS |
| 2 | Users should be able to click on a post to read the full content on a separate page | PASS |
| 3 | The blog should include pagination or infinite scrolling for easy navigation | PASS |

### Issue: Implement Editing and Deleting Posts for Staff Members [#28](https://github.com/AVTpepper/onestop-artist-shop/issues/28)

As a **staff member**, I can **edit and delete blog posts**, so that I can **manage the content on the website efficiently**.

| **Test** | Issue | Result |
| --- | --- | --- |
| 1 | The backend should handle post management, including editing and deleting blog posts | PASS |
| 2 | The backend should ensure proper permissions, allowing only staff members to access editing and deleting functionalities | PASS |
| 3 | The backend should provide an interface for staff members to manage blog posts | PASS |

### Issue 7: Basic Portfolio/Gallery Page [#18](https://github.com/AVTpepper/onestop-artist-shop/issues/18)

As a **visitor**, I can **browse a curated selection of the artist's work**, so that I can **appreciate their creative style and range**.

| **Test** | Issue | Result |
| --- | --- | --- |
| 1 | The Portfolio/Gallery page should display a grid or list of artworks, organized by series or themes | PASS |
| 2 | High-quality images should be used, with titles, dimensions, materials, and availability for each piece | PASS |
| 3 | The page should be responsive and work well on various screen sizes and devices | PASS |

### Issue 8: Backend Setup and Configuration [#19](https://github.com/AVTpepper/onestop-artist-shop/issues/19)

As an **administrator**, I can **have a reliable backend infrastructure**, so that **the e-commerce site functions properly and manages data efficiently**.

| **Test** | Issue | Result |
| --- | --- | --- |
| 1 | The backend should be set up using Django | PASS |
| 2 | The backend should connect to a database for storing product and user data | PASS |
| 3 | The backend should support essential e-commerce functionality, such as user authentication and product management | PASS |


## **Code Validation**

### **CSS**

The [W3C CSS Validator Service](https://jigsaw.w3.org/css-validator/) returned ________.

### **Lighthouse**



* **Desktop**:

![desktop-lighthouse]()

* **Mobile**:



* Developers Results:

![mobile-lighthouse]()

