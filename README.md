# Space Shack on planet Phaedrus-1711 website README.md

![The Space Shack Website amiresponsive image](/docs/images/amiresponsive-shack.png)

The live Space Shack site can be viewed [here](https://space-shack-a7e1db1b7daa.herokuapp.com/)

# Contents 

* [Introduction](#introduction)
* [Site objectives](#site-objectives)
* [User Experience](#user-experience)
    * [Target Audience](#target-audience)
    * [User Stories](#user-stories)
* [Design Development](#design-development)
    * [Typography](#typography)
    * [Colour Scheme](#colour-scheme)
    * [Wireframes](#wireframes)
    * [Images](#images)
    * [Database Tables](#database-tables)
    * [Flow Diagrams](#flow-diagrams)
* [Features](#features)
* [Ideas going forward](#ideas-going-forward)
* [Technologies Used](#technologies-used)
    * [Languages Used](#languages-used)
    * [External programs and libraries](#external-programs-or-libraries-used)
* [Testing File](#testing-file)
* [Deployment](#deployment-and-accessing-code-workspace)
* [Credits](#credits)
    * [Content](#content)
    * [Media](#media) 
* [Acknowledgements](#acknowledgements)

# Introduction 

## A Brief Summary 

Welcome to the Space Shack website - a simple booking and review portal for a fictional accommodation based on planet Phaedrus-1711. My daughter, 4, loves space and recently has been going through a phase of want to learn everything about all the planets right after story time at night. One night at bed time she asked if we could "Go up there one day". So although the idea for project 3 went through many different phases, I think it began that night. 

# Site objectives

## Deliver a clean, immersive user experience

The aim is to create a website that is not only visually engaging with a 'spacey' theme, but also accessible and intuitive to navigate. With a strong focus on usability, the front-end design combimnes custom HTML and CSS with Django template logic to ensure consistency and clarity across the whole site. Responsive layouts and semantic structure will ensure accessibility across screen sizes and user needs. 

## Enable dynamic user interaction through full-stack functionality

Using Django's back-end capabilities, authenticated users can interact fully with the platform. This includes posting, editing, and deleting reviews of the Space Shack, as well as commenting on others' experiences. Users can also submit booking requests for a fictional stay on the luxury space shack located on Phaedrus-1711. All user interactions are backed by a relational database and protected by authentication. 

## Use a cloud-hosted relational database

This project makes use of Neon.tech, a cloud-hosted PostgreSQL database, to store and manage all persistent data - including user reviews, comments and booking enquiries. This setup allows scalable, secure access to data from the deployed Heroku app while following best practices for environment separation and security. 

# User Experience

## Target Audience 

The target audience for the Space Shack Booking and Review Site includes sci-fi enthusiasts, space tourists, and interplanetary travellers seeking luxury accommodation beyond Earth. This fictional audience is composed of adventurous individuals who value comfort, exclusivity, and unique travel experiences — even if those experiences are imagined.

The site is also designed for users who enjoy sharing and reading space-themed reviews, engaging with others' stories, and contributing to a growing community of galactic travellers. By allowing visitors to leave comments and explore others’ stays, the platform fosters interaction in a way that mimics real-world review ecosystems.

Ultimately, the site provides a playful but fully functional simulation of a futuristic tourism experience, aimed at those who enjoy immersive fiction, user-generated content, and clean, easy-to-navigate design — while demonstrating practical full-stack development skills.

## User Stories 

The manual testing for these can be found in the [Testing document](/TESTING.md)

### New Visitor Goals 

- As a new visitor I want to gain an understanding of what Phaedrus-1711 and the Space Shack experience offers, through an immersive landing page and rich descriptions.

- As a new visitor I want to successfully navigate the site to explore reviews and comments from previous “guests.”

- As a new visitor I want to register for an account to become part of the interplanetary travel community.

- As a new visitor I want to make a (rather expensive) booking securely and then be able to leave my own reviews.

- As a new visitor I want to make sure I can follow this accommodation in other ways so that I can get updates from elsewhere. 

### Existing Visitor Goals 

- As a returning user I want to log in and out of their account securely.

- As a returning user I want to submit, view, edit, or delete their own reviews and comments.

- As a returning user I want to enjoy a consistent and responsive user interface across devices, reinforcing a seamless and immersive space tourism experience.

- As a returning user I want to enjoy navigating through the site on mobile as well as desktop.

- As a returning user I want to view and manage my upcoming bookings, so I can keep track of my interplanetary travel plans with ease.

# Design Development

Overall I wanted this website to have a fairly 'dark' look, to help reflect the darkness and 'abyss-ness' of space. I have styled the backgrounds with ChatGPT in this manner on purpose. It helped to create a cosy image of the fictional shack to 'entice' people to make 'bookings'. 

Before all this, I actually had a completely different idea but I felt like the scope was too large. It was to have a site where users could create, edit and delete their own fictional planets. It would include planet designs, colours, features, distance from the sun etc however I think it would have been a mission to get images generated of every new one created - a feature I think a site that does that would need. It wouldn't be enough to create the planets with no visual pleasure after. 

## Typography 

The site uses the Orbitron font throughout to maintain a futuristic, space-themed aesthetic. While I initially considered using a classic sci-fi green (often seen in retro space films) for the accent color, I felt it would be too harsh on the eyes. Instead, I opted for a bold yellow accent that complements the theme while keeping the overall look visually accessible and modern.

## Colour Scheme

This site incorporates the use of imagery into every page barring a few (Each individual review page, and both of the edit and delete buttons on that page and their redirects, will lead to a smartly coloured page with no imagery.) Despite this, the contrast is excellent throughout as shown in the screenshots below. Where there is a shift in the colour of the background for *imageColourPicker*, the lighter of the colours was chosen with the pen to try and accurately show the contrast levels to the text above it. 

![A screenshot showing contrasting color levels](/docs/images/features/contrast-check-1.jpg)
![A screenshot showing contrasting color levels](/docs/images/features/contrast-check-2.jpg)
![A screenshot showing contrasting color levels](/docs/images/features/contrast-check-3.jpg)
![A screenshot showing contrasting color levels](/docs/images/features/contrast-check-4.jpg)
![A screenshot showing contrasting color levels](/docs/images/features/contrast-check-5.jpg)
![A screenshot showing contrasting color levels](/docs/images/features/contrast-check-6.jpg)

## Wireframes 

Here are the wireframes I created at project inception for desktop.

Landing/Home page

![A wireframe for the homepage when displayed on desktop](/docs/images/landing-wireframe-pc.png)

About page 

![A wireframe for the about page when displayed on desktop](/docs/images/about-wireframe-pc.png)

Reviews page 

![A wireframe for the reviews page when displayed on desktop](/docs/images/reviews-wireframe-pc.png)

Booking page 

![A wireframe for the booking page when displayed on desktop](/docs/images/booking-wireframe-pc.png)

Edit, delete, sign in/out/up, confirmation pages

![A wireframe for the various administrative pages when displayed on desktop](/docs/images/admin-wireframe-pc.png)

Here is a wireframe for the 'About' page on smaller screens (tablet and below) as it's the only page that should really change much. The rest of the pages should generally stay the same, just shortened down in the responsiveness and focus, with a burger icon on all those relevant for navigation. 

![A wireframe of the about page when viewed on mobile or tablet](/docs/images/about-wireframe-mobile.png)

## Images 
All the images in this project were made using my own prompts given to ChatGPT. I generally believe we all need to harness the abilities of AI, but this project simply wouldn't have been possible in a creative way for obvious reasons without it. I had a very clear image of my landing page from day 1 (See Design) and the rest followed from there. The only tricky part of the prompts was trying to keep the "layout" of the planet uniformed through different prompts that created different angles, but I think I've succeeded in the most part. 

## Database Tables 

This project uses four main database tables: Booking, ReviewPost, Comment and Like - all of which connect to Django's built-in User model through foreign keys

### Booking Table 

Booking stores booking enquiries with guest information, check-in/check-out dates, and links each booking to a user.

| key | name             | type              |
|-----|------------------|-------------------|
| PK  | id               | integer           |
|     | name             | string            |
|     | email            | string            |
|     | number_of_guests | integer           |
|     | check_in         | datetime          |
|     | check_out        | datetime          |
|     | total_cost       | decimal           |
|     | created_on       | datetime          |
| FK  | user             | foreignkey(user)  |

### ReviewPost table  

Holds user-submitted reviews with titles, content, ratings and an author (user).

| key | name        | type                  |
|-----|-------------|-----------------------|
| PK  | id          | integer               |
|     | title       | string                |
|     | slug        | string                |
| FK  | author      | foreignkey(user)      |
|     | created_on  | datetime              |
|     | content     | text                  |
|     | excerpt     | text                  |
|     | rating      | integer               |
|     | approved    | boolean               |

### Comment Table 

Contains comments made by users on review posts, linking each to both a review and a user. 

| key | name       | type                     |
|-----|------------|--------------------------|
| PK  | id         | integer                  |
| FK  | post       | foreignkey(reviewpost)   |
| FK  | author     | foreignkey(user)         |
|     | body       | text                     |
|     | created_on | datetime                 |

### Like Table 

Tracks which users liked which review posts, ensuring each user can only like a post once. 

| key | name   | type                     |
|-----|--------|--------------------------|
| PK  | id     | integer                  |
| FK  | post   | foreignkey(reviewpost)   |
| FK  | user   | foreignkey(user)         |

## Flow Diagrams 

Here is a Flow Diagram for the User of the site

![User Flow Diagram](/docs/images/website-flow-user.drawio.png)

Here is a Flow Diagram for the Admin/Superuser(s) of the site

![User Flow Diagram](/docs/images/website-flow-admin.drawio.png)

# Features 

Here are some screenshots from the live site to show what users can look forward to 'on arrival'. 

This screenshot below is of the landing page. There are quite a few features to see here. There is the icon in the top left that will take you 'Home' instead of having to use the nav menu (this is a mobile shot). You can, however, still see the dropdown in action of a 'Signed-in' user. The arrow beside your name allows you to see bookings and logout. You can also see the social media links at the bottom in the footer. 

![Home page screenshot](/docs/images/features/nav-expanded-mobile.jpg)

This screenshot is of the 'About' page. I really wanted to allow myself a bit more creativity with this project and so although this page was not part of any requirements, I decided to put it in. It allowed me to have some fun with the planet names and just overall general content. This is of a PC view, showing the nav bar in it's full flow rather than condensed. 

![About page screenshot](/docs/images/features/nav-expanded-pc.jpg)

This screenshot shows the confirmation screen after a user makes a booking on the Space Shack. It has a welcome message, the price, and as you can see full functionality in taking you to your bookings screen should you want to amend or delete the booking. I did not want users to have to navigate more than needs be, but also wanted to keep the edit/delete buttons for another area outside of confirmation 

![Confirmation page screenshot](/docs/images/features/booking-confirmation.png)

And here is confirmation of the screen you would have when you get to My Bookings. Edit and delete both come with their own dedicated html pages allowing for full control, and the same rules that apply when making the initial booking.

![My bookings page screenshot](/docs/images/features/bookings-made.png)

Here is a screenshot of the booking screen, as well. Full functionality testing can be found for this and other aspects of user input on the site in the [Testing document](/TESTING.md)

![Booking page screenshot](/docs/images/features/form-shot.jpg)

Here is a screenshot of the welcoming reviews page. I do not like the idea of grid displays so the review is a carousel that changes every 5 seconds. Users can still click in to reviews if they feel they want to re-read, or if some reviews are too long and they've not had enough time to read it 

![Reviews screenshot](/docs/images/features/reviews-shot.jpg)

This is a screenshot of the page of each individual review, as mentioned above too. It shows a bit more detail and the bakcground changes colour for a bit of variety. This is where users can 'Like' the review and leave a comment, and as you can see they are able to edit or delete comments too which, like bookings, have their own tidy dedicated pages for the action.

![Review-detail page screenshot](/docs/images/features/single-review-shot.jpg)

Lastly here is a screenshot of the screen you're welcomed with when you want to post your own review. As stated elsewhere in the project, I took out the ability of uploading photos on this one. However if this were based on a real place I would have kept the functionality in there. 

![Add review page screenshot](/docs/images/features/posting-review.jpg)

# Ideas going forward 

While the current version of the site meets the core requirements, there is definite scope for growth. Given the scale of the project and the time available, I haven't implemented a full user profile section. At present, users have access to a booking portal, which successfully demonstrates CRUD functionality. However, introducing user profiles in future would open up additional opportunities — such as enabling direct communication with site administrators or tracking personal activity more comprehensively.

On the administrative side, there is potential to implement a comment and post moderation system. This would allow administrators to approve or reject submissions before they are published, streamlining content management. For now, I'm satisfied that the site effectively demonstrates the intended CRUD operations, but these enhancements would add further depth and professionalism to the platform.

Further, there is the chance to only allow users to leave a review once they have had a stay at the shack. This would have been a cool feature to implement despite it being fictional. This could be validated by checking if the user has an instance of booking, and if it's in the past then that would grant them functionality to post. Due to the scope and time constraints I haven't implemented it so far. 

# Technologies Used 

## Languages Used 
- HTML5
- CSS3
- JavaScript
- Python 
- Django
- SQL

## External Programs or Libraries used 
- VSCode for local development
- PostgreSQL
- [GoogleFonts](https://fonts.google.com/)
- [GitPod](https://www.gitpod.io/)
- [GitHub](https://github.com/)
- [Heroku](https://heroku.com)
- [NeonTech](https://neon.com/)
- [PEP8 Validator](https://pep8ci.herokuapp.com/)
- [Draw.io](https://app.diagrams.net/)
- [ChatGPT](https://chatgpt.com)
- [Imageresizer.com](https://imageresizer.com/)
- [Imagecolorpicker.com](https://imagecolorpicker.com/)

# Testing File
The testing.md file for this website can be viewed [here](/TESTING.md) 

# Deployment and accessing code workspace

## GitHub Deployment
This project used GitHub for version control and code storage throughout development.

After each addition, change, or removal of code, I committed updates using the following commands in the terminal (VS Code with Git Bash was used for this project):

git add .
git commit -m "Meaningful and descriptive commit message"
git push

This ensured the latest version of the codebase was stored and backed up in my [GitHub repository](https://github.com/ccrd1711/space_shack)

## Forking or Cloning the Repository

To make your own copy of this repository:

Fork:
Click the Fork button in the top-right corner of the GitHub page to add it to your own account.

Clone:
Click the green Code button.

Copy the repository URL using the clipboard icon.

Open your terminal (Git Bash recommended) and run:
git clone https://github.com/your-username/space_shack.git

Change into the project directory:
cd space_shack

You now have a local copy ready to work on.

## Heroku Deployment 

The live version of this site is hosted on Heroku, using a PostgreSQL database hosted by Neon.tech. The site is fully integrated with Django and configured for deployment using standard production settings.

Create a New App
Log in to your Heroku dashboard.

Click New → Create new app.

Name your app (e.g. space-shack-live) and choose your region.

Click Create app.

et Config Vars
In the Settings tab, click Reveal Config Vars, and add the following environment variables:

Key	Value
DATABASE_URL	From Neon.tech
SECRET_KEY	Your Django secret key
ALLOWED_HOSTS	Your Heroku app domain
PORT	(Optional, usually not needed)

These variables are used by your Django settings to keep sensitive information out of version control.

## Deploying from GitHub

Go to the Deploy tab.

Choose GitHub as the deployment method.

Connect your GitHub account if you haven’t already.

Search for your repository name (space_shack) and click Connect.

Under Manual deploy, choose the branch (e.g. main) and click Deploy Branch.

Once the build process finishes, click Open App to launch the live site.

You can also enable Automatic Deploys so that every push to GitHub triggers a redeployment.

# Credits 

## Content 
This website is an orginal creation and all the content is based off my own ideas and imagination. The name of the planet Phaedrus-1711, is based off a character in one of my favourite books of all time *Zen and the Art of Motorcycle Maintenance*. Phaedrus' contextual existence in the novel amongst readers is somewhat contested, but Phaedrus could be summarised simply as the alter ego of the narrator. 17 & 11 are just favoured numbers in our household. We also have a cat named Phaedrus!

You will find other literary links, too. There is a planet Kerouac-47. Jack is one of my favourite writers and he passed at the young age of 47. Vonnegut 5 is named after the author Kurt Vonnegut, and 5 is an homeage to *Slaughterhouse Five*. Joyce-730 is an ode to James Joyce, 730 being the number of pages there was in the first edition of the novel *Ulysses*.

All content in the website itself is fictional. 

## Media 
As stated near the top of this ReadMe file, all the media in this project was generated with ChatGPT with prompts given by me, the autor of the site. Late in the project I also realised I didn't have a home button in the top left which I like to have as an option, ChatGPT also designed that for me. 

## Acknowledgements 

I would like to thank (again!) the close knit support of friends and family I have. When it comes to these projects, they all offer their continuous encouragement and offer to test things out for me. 