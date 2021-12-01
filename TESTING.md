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
- [known bugs and yet to be fixed](#known-bugs-and-yet-to-be-fixed)

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

HTML was validated with [W3C Validator](https://validator.w3.org/) by URI. Results came out as follows.

![W3C Validator Results](https://github.com/gomathishankar28/ms4_bubbles/blob/main//readme_images/testing/htmlvalidator.jpg?raw=true)

### **Results from  W3C CSS**

CSS was validated with [W3C CSS](https://jigsaw.w3.org/css-validator/) by URI. Results came out as follows.

![W3c CSS Results](https://github.com/gomathishankar28/ms4_bubbles/blob/main//readme_images/testing/w3cresults.jpg?raw=true)

### **Results from Jshint**

Js files were validated with [Jshint](https://jshint.com/). No Errors found

   1. Warnings for variables with let or const declaration according to ECMAScript 6 features

              Fixed by adding /*jshint esversion: 6 */ at the top of every js file.

## User Stories Testing

*    As a prospective customer to the website, I want to easily navigate the site, so that I can easily find the products that  
 Bubbles offers.
         
         >  As the Website is launched, On the top-center is the Navigation bar with Products as the first link that displays what products,Bubbles offers.

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
        
         > This is acheived by providing an Edit profile form for all the registered users

*  As a Prospective customer tothe website , I would like to View my previous orders.

         > This is acheived by providing an view order history button on My profile page for all the registered users.

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

*   As a customer, I should be able to place orders even without signing into the site.
         > This is acheived by allowing the user to proceed with order without requesting them to login.

*   As a customer, I should be able to sign in, to access personalised information
         > This is acheived by clicking on "My profile" menu for any logged in user.


 ## Functional Testing

   Functional testing was done by testing induvidual features of the website to see if they meet their intended purpose.

   ## Home App

      1. Checked to see if Clicking on "Take a Look" button displays the Products Page - Tested PASS.

      2. Checked to see if searching for appropriate category of product on the search bar displays the corresponding productcategory page- Tested PASS 

      3. Checked to see Manage blog and Manage Products option under  USer Nav menu is displayed only for Admin user. - Tested PASS.

      4. Checked to see if  a Thankyou page is displayed when user sends a feedback using contact form.- Tested PASS.

   ## Profiles App

      1. Checked to see if My Profile option is displayed only for Loggedin user.- Tested PASS.

      2. Checked to see if the user details except the name are pre-filled on the checkout form,if the user has saved his profile already.- Tested PASS.

      3. Checked to see if Clicking on "My profile" displays the user Profile with personaland shipping details.- Tested PASS.

      4. Checked to see if clicking on "Edit Profile" on Profile page displays an Edit Form for the user to update his/her details.- Tested PASS.

      5. Checked to see if clicking on "update" on Edit Profile form  updates the users details.- Tested PASS.

      6. Checked to see if clicking on "View Order History" on profile page displays the order summary of allthe previous orders.- Tested PASS.

   ## Products App

      1. Checked to see if clicking on each product displays a Product detail page with description, average rating, directions for storage and shipping and return policy.- Tested PASS.

      2. Checked to see if "Manage Product" option is available only for admin user.- Tested PASS.

      3. Checked to see if admin user is able to add a new product via "Add Product Form".- Tested PASS.

      4. Checked to see if admin user is able to Edit an existing product via "Edit Product Form".- Tested PASS.

      5. Checked to see if admin user is able to delete an existing product".- Tested PASS.

      6. Checked to see if the incremenet and decrement quantity button works as appropriate.- Tested PASS.

      7. Checked to see if adding a product to the bag using "ADD to Cart" updates the bag count appropraitely.- Tested PASS.

   ## Reviews App

      1. Checked to see if clicking on "View Reviews" on product detail page displays the reviews for that particular product available.- Tested PASS.

      2. Checked to see if clicking on "View Reviews" on product detail page displays the message "No reviews available forthis product" if reviews for that particular product is NOT available.- Tested PASS.

      3.Checked to see if the Average Rating is calculated based on the rating of the user reviews.- Tested PASS.

      4. Checked to see if clicking on "Add Review" invokes a Login form if user is NOT logged in.- Tested PASS.

      5. Checked to see if clicking on "Add Review" invokes a Add Review form if user is logged in and if review is added to that product.- Tested PASS.

      6. Checked to see if clicking on Edit Review button displays an Edit Review form for the user who created that review and if review is updated appropriately.- Tested PASS.

      7. Checked to see if clicking on Delete Review button deletes that review created by the user.- Tested PASS.

   ## Bag App

      1. Checked to see if clicking on Empty bag displays an message saying the cart is empty.- Tested PASS.

      2. Checked to see if the bag is updated with the item, quantity and price whenever a new product is added.- Tested PASS.

      3. Checked to see if the bag is updated with the item, quantity and price whenever an existing product is updated.- Tested PASS.

      4. Checked to see if the bag is updated with the item, quantity and price whenever a  product is deleted from the bag.- Tested PASS.

   ## Checkout App

      1. Checked to see if clicking on checkout button displays the checkout form.- Tested PASS.

      2. Checked to see if there is an error when any required field is missed outtobe filled.- Tested PASS.

      3. Checked to see if the successful submission of the form displays a success message with order summary.- Tested PASS.


   ## Blog App

      1. Checked to see if total number of available posts is displayed correctly.- Tested PASS.

      2. Checked to see if Clicking on "Read More" button displays a detailed version of that post.- Tested PASS.

      3. Checked to see if a comment is added to a Post ,it is displayed under the appropriate post with name,date and time.- Tested PASS.

   ## Responsiveness Testing

**Devices Testing**

 Website was tested using Chrome Dev tools and Responsive Viewer in the following devices to check if the pages are rendered well.The results are satisfying<br>

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

![Performance Results](https://github.com/gomathishankar28/ms4_bubbles/blob/main//readme_images/testing//perfomance.jpg?raw=true)

## Accessibility Testing

The website's accessibility was also tested using Lighthouse. The result are shown below.

![Accessibility](https://github.com/gomathishankar28/ms4_bubbles/blob/main//readme_images/testing/accessibility.jpg?raw=true)



## Best Practices and SEO Results

![BestPractices](https://github.com/gomathishankar28/ms4_bubbles/blob/main/readme_images/testing/best_practices.jpg?raw=true)


![SEO](https://github.com/gomathishankar28/ms4_bubbles/blob/main/readme_images/testing/SEO.jpg?raw=true)


Spelling was checked thoroughly using [W3C Spell Checker](https://www.w3.org/2002/01/spellchecker). The results are satisfying.


## Issues found and fixed during Coding

1. I got a page not found error when i clicked on "My profile" for a new user who has just registered but not placed any order yet.
      This happened because the Profile page was designed to render the PERSONAL, SHIPPING and ORDER HISTORY details. And the shipping information was updated from the last order placed by the user which will obviously not be there for a new user who has not placed any order yet. Fixed by adding an if and else to test if the object exists and then rendering a different template.

            def profile(request):
         """ Display the user's profile. """
         profile = get_object_or_404(UserProfile, user=request.user)
         order = Order.objects.filter(user_profile=profile)
         if not(order):
            template = 'profiles/profile_new.html'
            return render(request, template)
         else:
            order = profile.orders.latest('order_number')
            template = 'profiles/profile.html'
            context = {
                  'profile': profile,
                  'on_profile_page': True,
                  'order': order,
            }
            return render(request, template, context)



2. Had issues calculating average rating for a product based on customer reviews. Later found a solution to calculate average rating on product_detail view as follows

         def product_detail(request, product_id):
      
         """ A view to show individual product details """
         product = get_object_or_404(Product, pk=product_id)
         reviews = Review.objects.filter(product=product)
         review_form = ReviewForm()
         avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']
         product.save()
         template = 'products/product_detail.html'
         context = {
            'product': product,
            'reviews': reviews,
            'review_form': review_form,
            'avg_rating': avg_rating
         }
         return render(request, template, context)


3. Wanted to restrict the edit and delete review action only to user's own reviews. This was done on the template by checking
{% if request.user == review.user %} before displaying edit , delete buttons to the user. This did not work.Later found that I should add a lower filter for string comparisons

        {% if request.user|lower == review.user|lower %}
         <span>
            <a href="{% url 'edit_review' review.id %}" data-toggle="tooltip" title="Edit Review" data-placement="top"     class="btn"><i class="far fa-edit"></i>
            </a>
         </span>
         <span>
            <a href="{% url 'delete_review' review.id %}" data-toggle="tooltip" title="Delete Review" data-placement="top" class="btn"><i class="far fa-trash-alt"></i>
            </a>
         </span>
         {% endif %}


## Known bugs and yet to be fixed

1. Form validation for checkout form and manage profile form is not in place. Need to fix it by altering the model by using  django-phonenumber field and write functions to raise validation errors for other form fields wherever required.


