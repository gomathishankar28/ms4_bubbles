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

*    As a prospective customer to the website, I want to easily navigate the site, so that I can easily find the products that  
 Bubbles offers.
   > As the Website is launched, On the top-center is the Navigation bar with Products as the first link that displays what products,Bubbles offers.

*   As a prospective customer to the website, I want to precisely know the different varieties of bathing products they sell.

   > As the Website is launched, On the top-center is the Navigation bar with Products as the first link that displays what products,Bubbles offers.

*   As a prospective customer to the website, I should be able to search based on keywords so that I can get the desired information quickly.

   > As the Website is launched, On the top is the search bar that enables the user to look for products that they want.

*   As a prospective customer, I should be able to access all the different bathing products from nav menu.
   > This is acheived by having a Dropdown Nav menu Products under which all different bathing products are listed

*   As a new customer to the website, I want to know if there are any new arrivals.
   > This is acheived by having a Latest Arrivals section on the Home page.

*   As a new customer to the website, I want to know more about the Bubbles team.
   > This is acheived by having a About section on the Home page.

*   As a new customer to the website, I want to see some success stories from customers.
   > This is acheived by having a Testimonials of 5 different customers as a carousel on the Home page.

*   As a new customer, I want to know the description of each product
   > This is acheived by displaying a Prodcut_detail page when each product is clicked.

*   As a new customer to website, I want to know how many products are available under each category.
   > This is acheived by dispaying the breadcrumb on top-left of the products page which tells which category of  products, the user is currently in and number of products in each category

*   As a customer to the website, I want to know the price of the product.
   > This is acheived by displaying an image of the product in the products page along with the name, Pricead Rating for the product.

*   As a customer, I would like to see any reviews available for the product.
   > This is acheived by cicking on "View Reviews" button on the product_detail page.

*   As a customer, I would like to add my own review to the product.
   > This is acheived by clicking on "Add Review" button on the product_detail page.

*   As a customer, I would like to see an average rating for each product that would help me to choose a better product.
   > This is acheived by displaying an average rating of the product in the product_detail page which is calculated based on the user's review rating. 

*   As a customer, I would like to know the shipping and Return Policy for the products.
   > This is acheived by displaying this information on the product_detail page.

*   As a prospective customer to the website, I want to edit my review for the product.
   > This is acheived by having an Edit review button against each review.

*   As a prospective customer to the website, I want to delete my review for the product.
   > This is acheived by having a delete review button against each review.

*   As a prospective customer to the website, I want to contact Bubbles team incase of any issues.
   > This is acheived by having a contact form on the Home page.

*  As a prospective customer to the website, I would like to easily update my cart by increasing or decreasing the quantity of the product.
   > This is acheived by placing a increment decrement quantity Input box on the Product_detail page.

*  As a prospective customer to the website, I would like to have my delivery information prefilled so that i can complete my purchase quickly.
   > This is acheived by having a Checkbox to save the  user's  personal and shipping details while making their first purchase.

*  As a prospective customer to the website, I would like to Edit my personal and shipping details.

*  As a Prospective customer tothe website , I would like to View my previous orders.

*   As an Administrator, I would like to restrict only the logged in users to add/edit/delete his/her own review so that unauthorized/ untraceable changes are prevented.
   > This is acheieved by displaying edit, delete review buttons only for the reviews the logged in user has created. Also ,to add a review, user willbe asked to login before adding a review.

*   As an administrator, I would like to add a new product.
   > This is acheieved by dispalying a Add Product form by clicking on Manage Products option on the User Nav menu which will be visible only for admin user.

*   As an administrator, I would like to add a new Blog Post.
   > This is acheieved by dispalying a Add Post form by clicking on Manage Blog option on the User Nav menu which will be visible only for admin user..

*   As an administrator, both unregistered and registered users should be able to view the product and the user reviews so that the display of information is not restricted for unregistered users.
   > This is acheieved by clicking on "Take a Look" button on the hero image and also further clicking on each product,usercan see the reviews for the product.

*   As an administrator, I should allow registered users to log out so that unauthorized accesses are prevented.
   > This is acheieved by dispalying a Add Post form by clicking on Manage Blog option on the User Nav menu.

*   As an administrator, I would like to have field level validations on the contact entry so that incorrect or incomplete information is avoided.
   > This is acheieved by using django-phonenumber for Mobile number field on the checkout form.


 ## Functional Testing

   Functional testing was done by testing induvidual features of the website to see if they meet their intended purpose.

   ## Home App

   ## Profiles App

   ## Products App

   ## Reviews App

   ## Bag App

   ## Checkout App

   ## Blog App

   ## Responsiveness Testing

**Devices Testing**

 Website was tested using Chrome Dev tools in the following devices to check if the pages are rendered well.The results are satisfying<br>

   1. Galaxy Fold.<br>
   2. Moto G4<br>
   3. Pixel 2<br>
   4. Pixel 2xl<br>
   5. iphone5<br>
   6. iphone 6/7/8<br>
   7. iphone 6/7/8 plus<br>
   8. iphone x<br>
   9. surface Duo<br>
   10. ipad<br>
   11. ipad pro.<br>

***BrowserTesting***

Website was tested in browsers listed below and results were satisfying.

1. Chrome<br>
2. Edge.<br>
3. Opera<br>
4. Safari<br>
5. Firefox<br>

***Operating System Testing***

Website was tested in different OS listed below and results were satisfying.

1. Windows 10<br>
2. Mac OS.<br>
3. iOS.<br>
4. Android<br>

## Performance Testing

Performance has been tested using the Lighthouse tool of Google Chrome. The results are shown below.

> ![Perfomance Results](https://github.com/gomathishankar28/ms4_bubbles/blob/master/readme_images/testing//performance.jpg?raw=true)

## Accessibility Testing

The website's accessibility was also tested using Lighthouse. The result are shown below.

> ![Accessibility](https://github.com/gomathishankar28/ms4_bubbles/blob/master/readme_images/testing/accessibility.jpg?raw=true)


## Best Practices and SEO Results

> ![BestPractices](https://github.com/gomathishankar28/ms4_bubbles/blob/master/readme_images/testing/best_practices.jpg?raw=true)


> ![SEO](https://github.com/gomathishankar28/ms4_bubbles/blob/master/readme_images/testing/SEO.jpg?raw=true)


Spelling was checked thoroughly using [W3C Spell Checker](https://www.w3.org/2002/01/spellchecker). The results are satisfying.


## Issues found and fixed during Coding

