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

This section contains a range of issues that were solved, including simple ones at project inception to more nuanced/complex ones late in development. What you see here is in chronological order so it gives you an idea of which direction I had my development going in. If any bugs remain at the end of the project that haven't been rectified they will be in their appropriate section. 

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
