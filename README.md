"# space_shack" 

Bugs so far

Only on preview site, not live currently

Logging out produces a 500 server error, and logging back in does not take me to reviews like I want 
- Adding redirect urls to settings.py, fixing line in space shack urls.py, 

Adding a blog post took to anotjher 500 server error
- Adding ReviewForm to views.py fixed this as error showed is as undefined - long day of coding - forgot to put it in!

Adding a blog post then did not post it to the reviews page
- I was looping over 'posts' not 'reviews' so was in limbo

Booking dates was failing on testing - message saying can't compate datetime.datetime to datetime.date
- Changed:
"if check_in < timezone.now().date():"
to
"if check_in and check_in.date() < timezone.now().date():
    self.add_error('check_in', 'Check-in cannot be in the past.')"
in bookings/forms
and adding 
"if self.check_in and self.check_in.date() < timezone.now().date():
    raise ValidationError("Check-in date cannot be in the past.")"
to models.py 
ensuring I was comparing date() to date()

Likes were not showing on reviews individually after design change, and getting poster comments under a button to say when you've liked a review:



Features that were not implement but could be in future:
User dashboard to see reviews