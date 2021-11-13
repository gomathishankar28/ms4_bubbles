# **Testing**

## Table of Contents

- [Smoke Testing](#smoke-testing)
- [Code Testing](#code-testing)
- [User stories Testing](#user-stories-testing)
- [Functional Testing](#functional-testing)
- [Responsiveness Testing](#responsiveness-testing)
- [Performance Testing](#performance-testing)
- [Accessibility Testing](#accessibility-testing)
- [Best Practices and SEO Results](#best-practices-and-seo-results)
- [Issues found and fixed during Coding](#issues-found-and-fixed-during-coding)
- [Enhancements](#enhancements)

## Smoke Testing

Following testcases were tested as part of smoke testing.

> 1. To  Check if the Website launches with a Home page when given the URL of the site. - **Tested Pass**.
> 2. To Check for broken links for all the navigation menus. – **Tested Pass**.
> 3. To Check if “search” button on the landing page displays the desired results based on the search – **Tested Pass**
> 4. To check if clicking on each product in Products Page displays the  appropriate Product detail page- **Tested pass**.
> 5. To check if hitting on CTA button on the heroimage displays the Products Page – **Tested Pass**.
> 6. To check if the Increment and decrement functionof the Quantity button on the productdetail page  works – **Tested Pass**.
> 7. To check if clicking on Add to Cart button,addsthe corresponding item to the shopping bag.  – **Tested Pass**.
> 8. To check if clicking on Checkout button displays the checkout form - **Tested Pass**.
> 9. To check if clicking on Add_review button in product_detail page invokes the "Add review form" - **Tested pass**.
> 10. To check if the send button on the contact form renders a Thankyou Page – **Tested Pass**.
> 11. To check if the clicking on add comment on Blogpost page displays the added comment under the aprropriate post - **Tested Pass**.
> 12. To check if searching for inappropriate item results in "sorry results not found" page - **Tested Pass**.

## Code Testing

### **Results from HTML Validator**

HTML was validated with [W3C Validator](https://validator.w3.org/) by direct input. Results came out good except for few errors because of the use of  jinja templating which cannot be avoided.


### **Results from  W3C CSS**

CSS was validated with [W3C CSS](https://jigsaw.w3.org/css-validator/) by direct input.Results came out good


### **Results from Jshint**

Js files were validated with [Jshint](https://jshint.com/). No Errors found

   1. Warnings for variables with let or const declaration according to ECMAScript 6 features

              Fixed by adding /*jshint esversion: 6 */ at the top of every js file.

## User Stories Testing

*    As a prospective customer to the website, I want to easily navigate the site, so that I can easily find the products that   Bubbles offers.

*   As a prospective customer to the website, I want to precisely know the different varieties of bathing products they sell.

*   As a prospective customer to the website, I should be able to search based on keywords so that I can get the desired information quickly.

*   As a prospective customer, I would like to receive suggestions in the search field so that I can narrow down my search easily.

*   As a prospective customer, I should be able to access all the different bathing products from nav menu.

*   As a new customer to the website, I want to know if there are any new arrivals.

*   As a new customer, I want to know the description of each product

*   As a new customer to website, I want to know how many products are available under each category.

*   As a customer to the website, I want to know the price of the product.

*   As a customer, I would like to see any reviews available for the product.

*   As a customer, I would like to add my own review to the product.

*   As a customer, I would like to see an average rating for each product that would help me to choose a better product.

*   As a customer, I would like to knowthe shipping and Return Policy for the products.

*   As a prospective customer to the website, I want to edit my review for the product.

*   As a prospective customer to the website, I want to delete my review for the product.

*   As a prospective customer to the website, I want to contact Bubbles team incase of any issues.

*  As a prospective customer to the website, I would like to easily update my cart by increasing or decreasing the quantity of the product.

*  As a prospective customer to the website, I would like to have my delivery information prefilled so that i can complete my purchase quickly.

*   As an Administrator, I would like to restrict only the logged in users to add/edit/delete his/her ownreview so that unauthorized/ untraceable changes are prevented.

*   As an administrator, I would like to add a new product.

*   As an administrator, I would like to add a new BlogPost.

*   As an administrator, both unregistered and registered users should be able to view the product and the user reviews so that the display of information is not restricted for unregistered users.

*   As an administrator, I should allow registered users to log out so that unauthorized accesses are prevented.

*   As an administrator, I would like to have field level validations on the contact entry so that incorrect or incomplete information is avoided.