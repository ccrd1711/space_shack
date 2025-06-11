# Space Shack on planet Phaedrus-1711 website Testing.md

![The Space Shack Website amiresponsive image](/docs/images/amiresponsive-shack.png)

# Testing Contents Menu 

* [Automated Testing](#automated-testing)
    * [Validators](#validators)
    * [Lighthouse](#lighthouse)

* [Manual Testing](#manual-testing)
    * [User Stories](#user-stories)
    * [New Visitors](#new-visitors-to-the-site)
    * [Returning Visitors](#returning-visitors)
    * [New Visitor Testing](#new-visitor-testing)
    * [Return Visitor Testing](#returning-visitor-testing)

* [Bugs/Issues/Fixes](#bugsissuesfixes)

* [Responsive Tests](#responsive-tests)

# Automated Testing

## Validators 

### HTML 

HTML validation was completed using [W3C Validator](https://validator.w3.org). In past projects I have copied and pasted my HTML directly from the files in VS Code in to the validator to test. This time, due to having base.html and most html pages in my project extending from base.html, I went to every single page on the website and viewed the source code. I copied and pasted this html in to the validator. Every single page  passed with no errors.

### CSS 

CSS validation was completed using [the W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/validator), no errors were found. This one was completed as normal, by copying my CSS file input into the direct input box. 

### Javascript 

Javascript validation was completed using [JSHint](https://jshint.com/) and both files came back with no errors found.

### Python

Python PEP8 compliance testing and validation was completed using [the CI Python Linter](https://pep8ci.herokuapp.com). Every single py file was input on 9/6 after reaching a point in development where likely no more changes were to be made apart from comments. All files were amended and are now compliant with no errors. 

## Lighthouse 

Here are the reports I got from running Lighthouse reports on desktop and mobile 

### Desktop

![A screenshot of the results of lighthouse testing on desktop](/docs/images/lighthouse/desktop%20index%20lighthouse.png)

### Mobile 

![A screenshot of the results of Lighthouse testing on mobile devices](/docs/images/lighthouse/mobile-lighthouse-report.png)

# Manual Testing 

## User Stories 

### New visitors to the site 

| Goal | How is it achieved? | Pass or Fail | 
| --- | :---: | ---: |
|As a new visitor I want to gain an understanding of what Phaedrus-1711 and the Space Shack experience offers, through an immersive landing page and rich descriptions. | The user is welcomed by a vibrant and cosy-feeling landing page and the About page provides more immersive information on their potential stay at the Shack.| Pass 
|As a new visitor I want to successfully navigate the site to explore reviews and comments from previous “guests.” | All users are able to *view* the reviews, and can see who it was written by, the content and star rating.| Pass 
|As a new visitor I want to register for an account to become part of the interplanetary travel community.| Continuing on from the previous story, users can go one further and register which allows them full interactivity and can leave comments and like reviews.| Pass
|As a new visitor I want to make a (rather expensive) booking securely and then be able to leave my own reviews.| You are not able to leave a review or book the Shack on the site without being logged in. The form is fully interactive so that it will snuff out typo errors on email fields, and avoids double bookings.| Pass
|As a new visitor I want to make sure I can follow this accommodation in other ways so that I can get updates from elsewhere.| There are social media icons along the bottom of every page to take the user to relevant social channels for updates.| Pass 

### Returning visitors to the site 

| Goal | How is it achieved? | Pass or Fail | 
| --- | :---: | ---: |
|As a returning user I want to log in and out of their account securely.| Users have a login button brightly signposted in the nav bar, and a log out option in the dropdown under their username.| Pass 
|As a returning user I want to submit, view, edit, or delete their own reviews and comments.| As mentioned above, this is a continuation. All submissions, views, edits and deletes have their own dedicated screens.| Pass 
|As a returning user I want to enjoy a consistent and responsive user interface across devices, reinforcing a seamless and immersive space tourism experience.| The site is fully functional and responsive on all screen sizes and is designed for ease of navigation| Pass 
|As a returning user I want to enjoy navigating through the site on mobile as well as desktop.| There is an accessible and well highlighted dropdown to take you to all elements of the site plus an icon in the top left to take you to the index page quicker.| Pass
|As a returning user I want to view and manage my upcoming bookings, so I can keep track of my interplanetary travel plans with ease.| In the dropdown under the user name is a section for My Bookings where any booked trips can be removed or amended as necessary| Pass 


# Bugs/Issues/Fixes

This section contains a range of issues that were solved, including simple ones at project inception to more nuanced/complex ones late in development. What you see here is in chronological order so it gives you an idea of which direction I had my development going in. If any bugs remain at the end of the project that haven't been rectified they will be in their appropriate section. There were likely others through development that haven't been recorded fully due to being so focused on fixing them and forgetting to note them down at the time. 

 Fixed bugs | What happened? | Solution 
-- | -- | -- |
No. 1 | When submitting a review form error message showed: NameError: name 'ReviewForm' is not defined | 'from .forms import ReviewForm' input at top of views.py
No. 2 | When clicking sign up, the site broke with message: NoReverseMatch: Reverse for 'signup' not found | Again this was a template created before the view and url and tested in error. View added and path created in urls.py 
No. 3 | Submitting a comment showed no visible errors, but nothing appeared in the interace. The comment was being saved but Django didn't know which review the comment belonged. | Ensured that in the review_detail view the comment was tied to the correct review. comment.post=review solved this along with {% for comment in comments %}
No. 4 | Creating a review post still manually required a slug, and leaving it blank caused errors | Used Django's slugify to autofill within the save method in ReviewPost of reviews/models.py 
No. 5 | The booking form failed with this error: "can't compare datetime.datetime to datetime.date". This happened because check_in and check_out are stored as DateTimeField but the code was comparing them to timezone.now().date() and Python rejects this. | Converted check_in to just a date: 'if self.check_in.date() < timezone.now().date():' so the comparisons were valid. 
No. 6 | Users could book the Shack even if overlapping dates had already been booked by someone else. The system did not check for existing bookings. | In the Booking model's clean method, I added a query to find overlapping bookings. 'overlapping_bookings' on line 29 in models.py. The model also blocks the current booking booking from the check during edits, and shows a validation error for when the overlap is triggered. 
No. 7 | Multiple TemplateDoesNotExist errors especially for login.html (in registration folder) and base.html | Added "'DIRS': [BASE_DIR / 'templates']," to settings.py after confirming file structure.
No. 8 | Login was required to view reviews, which was only meant to be for creating comments or writing reviews | Easy fix of removing the @login_required decorator from the reviews_list view in views.py. Anyone can view reviews, but only logged-in users can post, comment or like. 
No. 9 | When the reviews were changing between one and the other, the whole review container would flash and/or jump down the page. | Set .review-list to position: relative with a fixed height, and .review-item to position: absolute so the items stack in place. The carousel smoothly fades between items now in one stable position. 
No. 10 | Login was set to send the user to the reviews page straight away upon logging in. This must have been an error created when setting the parameters so much that you had to be logged in to leave a review. The same was happening with logging out. | Fixed both routing issues in settings.py, with logging in routing users to the homepage and logging out landing on a confirmation with a CTA to log back in. 
No. 11 | Star ratings on the reviews page carousel were continuously showing 5 stars, but the correct individual score given was on each written detail page. Eg. A user gives 3 stars, this would show in that page where you can comment. But on the review_list page carousel it would show as 5 still. | After confirming the ratings were saved properly in the model, I updated the star display look to check the post.rating. Ensured this was the same for both review_detail and review_list. 
No. 12 | Users could not 'unlike' a review after liking, no feedback or reversal. | Updated review_detail in views.py. Originally the view only created a like if the user had not already liked the post, so added logic to delete the like if it was actioned again with liked.delete(). 
No. 13 | When users went to leave a comment on a review, the form included a label that said "Body:" beside a large white input box. It looked clunky and out of place. | In forms.py CommentForm was customised to include a placeholder instead of using the default label. Starting at line 24 in forms.py 
No. 14 | Review detail layout looked messy and not up to modern standards | After using other websites for inspiration (like Booking.com and Amazon.co.uk), the template was reimagined by wrapping sections in divs with semantic classes like .review-header, .comment-section etc. CSS was then added to these to improve the order, layout, spacing and typography. The page now looks well structured and separated. 
No. 15 | Booking cancellations happened instantly without confirmation message, so when you cancelled you were immediately taking to My Bookings with the text "You have no bookings". | The button was replaced with a link directing to a separate confirmation page that was created very early on in development but almost forgotten about due to the depth of the project. The cancel_booking view then handled requests by directing to confirm_cancel.html and only deleted the booking on a POST. Now they're taken to a 'make-sure' cancel page avoiding any accidental cancellations. 
No. 16 | Multiple pages that were very late to development in terms of styling all had their content pushed too close to the top of the browser window, creating a cramped appearance. | Each page had its content wrapped in a div with class .spacing-top and a shared rule was created to bring them all down 80px.