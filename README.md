# Space Shack on planet Phaedrus 17-11 website 

![The Space Shack Website]

# Contents 

* [Introduction](#introduction)

* [Site objectives](#site-objectives)

* [User Experience](#user-experience)
    * [Target Audience](#target-audience)
    * [User Stores](#user-stories)

* [Design Development](#design-development)
    * [Wireframes](#wireframes)
    * [Images](#images)
    * [Database Tables](#database-tables)
    * [Flow Diagrams](#flow-diagrams)

* [Features](#features)

* [Ideas going forward](#ideas-going-forward)

* [Technologies Used](#technologies-used)

* [Languages Used](#languages-used)

* [External programs and libraries](#external-programs-or-libraries-used)

* [Deployment](#deployment-and-accessing-code-workspace)
      
* [My Own Deployment](#my-own-deployment)

* [Credits](#credits)

* [Code Inspiration](#code-inspiration)

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

### New Visitor Goals 

- Gain an understanding of what Phaedrus-1711 and the Space Shack experience offers, through an immersive landing page and rich descriptions.

- Successfully navigate the site to explore reviews and comments from previous “guests.”

- Register for an account to become part of the interplanetary travel community.

- Engage with site content by reading stories, submitting their own reviews, and optionally making a (rather expensive) booking.

### Existing Visitor Goals 

- Log in and out of their account securely.

- Submit, view, edit, or delete their own reviews and comments.

- Interact with new and returning users by commenting on reviews and contributing to the community feel.

- Submit and manage a booking enquiry, simulating a luxury stay on Phaedrus-1711.

- Enjoy a consistent and responsive user interface across devices, reinforcing a seamless and immersive space tourism experience.


# Design Development

## Wireframes 

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

