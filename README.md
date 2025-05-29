"# space_shack" 

Bugs so far

Only on preview site, not live currently

Logging out produces a 500 server error, and logging back in does not take me to reviews like I want 
- Adding redirect urls to settings.py, fixing line in space shack urls.py, 

Adding a blog post took to anotjher 500 server error
- Adding ReviewForm to views.py fixed this as error showed is as undefined - long day of coding - forgot to put it in!

Adding a blog post then did not post it to the reviews page
- I was looping over 'posts' not 'reviews' so was in limbo