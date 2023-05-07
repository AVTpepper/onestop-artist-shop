# **Testing**

## **Table of content**

* [Testing User Stories](#testing-user-stories)
    * [Site Navigation](#site-navigation-1)
    * [User Authentication](#user-authentication-2)
    * [Property](#property-3)
    * [Profile Creation and Management](#profile-creation-and-management-4)
    * [Blog](#blog-88)
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
| 3 | The form should include GDPR compliance elements, such as a consent checkbox and a link to the privacy policy | FAIL |

### Issue 16: Events/Exhibitions Page [#27](https://github.com/AVTpepper/onestop-artist-shop/issues/27) (not yet implemented)

As a **visitor**, I can **view a list of the artist's upcoming and past events or exhibitions** so that I can **attend or learn about their work in a broader context**.

| **Test** | Issue | Result |
| --- | --- | --- |
| 1 | The Events/Exhibitions page should display a list of events, including titles, dates, locations, and descriptions | FAIL |
| 2 | The events should be organized by date, with upcoming events listed first | FAIL |
| 3 | The page should be responsive and work well on various screen sizes and devices | FAIL |

### Issue 6: About Page Content [#17](https://github.com/AVTpepper/onestop-artist-shop/issues/17)

As a **visitor**, I can **learn more about the artist's background and artistic vision** so that I can **connect with their work on a deeper level**.

| **Test** | Issue | Result |
| --- | --- | --- |
| 1 | The About page should include the artist's bio, artist statement, resume/CV, and press mentions | FAIL |
| 2 | A professional photo or video of the artist should be displayed on the About page | PASS |
| 3 | The page should be responsive and work well on various screen sizes and devices | PASS |

### Issue 10: Backend Support for Newsletter Signup [#21](https://github.com/AVTpepper/onestop-artist-shop/issues/21) (not fully implemented)

As an **administrator**, I can **manage newsletter subscriptions** so that I can **send updates and promotional content to subscribers**.

| **Test** | Issue | Result |
| --- | --- | --- |
| 1 | The backend should store and manage newsletter subscriber data | PASS |
| 2 | The backend should integrate with an email marketing platform (e.g., Mailchimp, SendGrid) for sending newsletters | PASS |
| 3 | Test the newsletter subscription functionality and integration | PASS |


## **Code Validation**

### **JSX**

All JSX code was validated and corrected throughout the development of the project.

### **CSS**

The [W3C CSS Validator Service](https://jigsaw.w3.org/css-validator/) returned no CSS errors.

### **Lighthouse**

Google Developers Tools Lighthouse was used to test the performance of the web application on both desktop and mobile.

* **Desktop**:

![desktop-lighthouse](/documentation/readme_images/lighthouse/lighthouse%20desktop%20main%20page.png)

* **Mobile**:

The Lighthouse performance for mobile on the developers internet speed ran a test which resulted in a performance of between 34-37.

However, when the same Lighthouse test for mobile was carried out on the developers mentors network speed and computer, the results were a more positive attribute of 70-80.

Both images are displayed for clarity and evidence.

* Developers Results:

![mobile-lighthouse](/documentation/readme_images/lighthouse/lighthouse%20mobile%20main%20page.png)

* Mentors Results: 

![mobile-lighthouse-mentor](/documentation/readme_images/lighthouse/mentor-lighthouse-mobile.png)