![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Table of contents
* [User Experience](#user-experience)
  * [User Stories](#user-stories) 
  * [Design](#design)
* [Features](#features)
  * [Existing Features](#existing-features)
  * [Features Left To Implement](#features-left-to-implement)
* [Technologies](#technologies)
* [Testing](#testing)
  * [Validator Testing](#validator-testing)
  * [Manual Testing](#manual-testing)
  * [Bugs](#bugs)
* [Deployment](#deployment)
* [Credits](#credits)

# Project 4 - Code Institute Full Stack Diploma

This is a blog created in Django for completion of 4th project at Code Institute (Full Stack Developer Course).
Please find the link [here](https://djangofilmblog.herokuapp.com/).

![image](https://user-images.png)

***

# User Stories and Design

### First Time User Goals
<details><summary>First Time User Goals</summary>

* As a First Time User, I understand the objective of the blog.
* As a First Time User, I understand how to navigate through the website.
* As a First Time User, I can register an account.
* As a First Time User, I can read blog's posts.
</details>
<details><summary>Frequent User Goals</summary>

* As a Frequent User, I can log in to gain access to my account.
* As a Frequent User, I can create my own blog post and post it on the website.
* As a Frequent User, I can edit and delete my posts.
* As a Frequent User, I can comment on a blog post.
* As a Frequent User, I can like a post.
* As a Frequent User, I can change my password incase their is a security risk.
</details>

<details><summary>Admin User Goals</summary>

* As an Admin, I can create, read, update and delete posts from admin panel and directly from website.
* As an Admin, I can approve or disapprove comments.
</details>

***
### Design

<details>

</details>

<details><summary>Imagery</summary>
Images are mainly depicting 
![Imagery](static/images/readme/readme-placeholder.jpg)
</details>

<details><summary>Color Scheme</summary>
Three colors are used in this website, these being #000000, #FFFFFF and #FF0030. The background, text and foreground colors have a sufficient contrast ratio to aid with accessibility.

![Color Pallete](static/images/readme/palette.png)
</details>

<details><summary>Fonts</summary>
The font used throughout the website is Ssk. 
![Fonts](static/images/readme/readme-font.png)
</details>

***

# Features
## Existing Features
<details><summary>Home Page</summary>
 
Home Page will display the base.html, which contains Log in or Register options.
From Home Page user can access posts as well. 

![image](https://user-imag6.png)
 
</details>

<details><summary>Navigation Bar</summary>
 
The nav bar display changes depending on user access. If user is not staff or admin will be able to see EDIT PROFILE option and Log Out.
If it is Admin or Staff User will have the option to Add Post.
![image](https://user-images.githubusercontent.com/98277650/188749607-8643846a-77b6-4970-bdb8-edab95b1e5f2.png)

</details> 

<details><summary>Footer</summary>
 
Footer has link to LinkedIn.
```
![image](https://user-1ab900.png)
 
</details>

<details><summary>Post Detail</summary>
 
When one of the posts on the home page is clicked, the user is taken to post detail view. Here the user can see the author, date/time posted and the content itself.



The purpose of this is to fulfill the following user stories:
```
As a First Time User, I can choose a post I would like to inspect further.
```
![image](https://user-images.githubusercontent.com/98277650/188749721-9345eef1-0846-4a4d-b8be-72f458072e50.png)
 
</details>

<details><summary>Like/Unlike</summary>
 
Just below the post itself, two icons are visible. One of these being a clickable Like button that can only be interacted with when the user has logged in. The second icon shows the amount of comments the post has recieved.

The purpose of this is to fulfill the following user story:
```
As a Frequent User, I can like a post to show that I enjoyed it.
```
![image](static/images/readme/like-unlike.png)

I also added a link that will enable the user to share the blog post to their own Twitter account.

The purpose of this is to fulfill the following user story:
```
As a Frequent User, I can share a post to my own personal social media account.
```
![image](static/images/readme/twitter-share.png)

</details>

<details><summary>Post Comments</summary>
 
At the bottom of the post is the comments section, where the user is able to write and post a comment on the blog post.

The purpose of this is to fulfill the following user story:
```
As a Frequent User, I can comment on a blog post with my thoughts on the subject.
```
![image](https://user-images.githubusercontent.com/98277650/188749804-bde80368-9193-471d-8a64-3e419e1adebe.png)

When the user has posted a comment, an alert replaces the text field letting them know that their comment is awaiting inspection and approval.

The purpose of this is to fulfill the following user story:
```
As an Admin, I can approve or disapprove comments so that I can filter out objectionable comments.
```

![image](https://user-images.githubusercontent.com/98277650/188749923-dfdab3c8-331c-47c1-99a0-e4f917a0f4af.png)
 
</details>

<details><summary>Add Post</summary>
 
This page of the website allows the user to create their own blog post. I implemented a rich text editor which allows the user to add a bit more style to their post. For security reasons I have to give the user staff privileges to be able to post, which is common practice in other professional websites. This is to ensure that not just anyone off the internet can find my website and post questionable things.

The purpose of this is to fulfill the following user stories:
```
As a Frequent User, I can create my own blog post and post it on the website.
```
![image](https://user-images.githubusercontent.com/98277650/188750032-7fd19423-9acf-4851-80fb-bb2af0e0365b.png)

</details>

<details><summary>Edit/Delete Post</summary>
 
When detected as author of the post, User can delete or edit it.

![image](https://user-imag8277650/188750267-9fe41ace-f585-42a9-bafa-7c69fdb28e04.png)

![image](https://user-imagom/98277650/188750296-f19bc082-072f-4a46-8a2a-2f2c240afc16.png)

When the user clicks the delete button they are taken to a new page with a warning, making sure they are aware that they are about to permanently delete the post. This is so if they change their mind and want to keep it, they can.

![image](https://user-images.githubusercontent.com/98277650/188750325-c4fde938-07be-45cd-b2bd-5104da48feb0.png)

</details>

<details><summary>Register</summary>
 
User can register and after registration will gain access to commenting, and if authorized, to make posts.
![image](static/images/readme/register.png)

</details>

<details><summary>Log In</summary>
 
User can log in to account make likes, comments and, if authorized, make posts.
```
![image](static/images/login.png)

</details>

<details><summary>Edit Profile</summary>
 
User can edit and update:
* Username
* Email
* First Name
* Last Name

The purpose of this is to fulfill the following user stories:
```
As a Frequent User, I can change aspects of my personal account details.
```
![image](https://user-images.githubusercontent.com/98277650/188750457-33d23728-d41b-4f35-b28f-2f82f222a4ee.png)

</details>

<details><summary>Change Password</summary>
 
Change password is an option provided within the Edit Profile site.
![image](3c1.png)

When the user has confirmed their new password, they are taken to a page informing them that the change was successful.

![image](https://user-images.githubusercontent.cog)

</details>

***

# Technologies

* HTML
* CSS
* JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* Django](https://en.wikipedia.org/wiki/Django_(web_framework))
* Bootstrap](https://en.wikipedia.org/wiki/Bootstrap_(front-end_framework))
* Heroku
* Font Awesome](https://fontawesome.com/)
* Google Fonts](https://fonts.google.com/)

***

# Testing

## Validator Testing

### Code Validation

Code was validated through various sources: 

* HTML Validation

  All HTML code was checked with the [W3C Markup Validation Service](https://validator.w3.org/).

   <details>
   <summary>Home Page</summary>

   ![image](https://user-images.deb5.png)

   </details>
   <details>
   <summary>Post Detail</summary>

   ![image](https://use81ebacb.png)

   </details>
   <details>
   <summary>Sign Up</summary>

   ![image](https://user3f1.png)

   </details>
   <details>
   <summary>Log In</summary>

   ![image](https://uspng)

   </details>
   <details>
   <summary>Add Post</summary>

   One error returned. As seen in the code below, I have had to use {{ form.as_p }} to get the rich text editor to function correctly. As of right now I am unsure of a solution.

   ![image](https://user-images.githubusercontent.com/98277650/187972452-e1a36e47-c8ec-4367-9b6a-595ed69114de.png)


   ![image](https://user-images.githubusercontent.com/98277650/187972057-046a277d-71b6-4eac-8f6a-1754f95f633f.png)

   </details>
   <details>
   <summary>Edit Profile</summary>

   I was unable to validate this page due to the page only being accessible to a user who is logged in and able to edit their profile.

   ![image](https://user-images.githubusercontent.com/98277650/187972974-6047d7bb-40ea-4596-9c23-f18c3a808ccc.png)

   </details>
   <details>
   <summary>Log Out</summary>

   ![image](https://user-images.githubusercontent.com/98277650/187973621-a01a08f4-4271-4ef0-826e-7f3eb836001f.png)

   </details>
   
* CSS Validation

  All CSS code was checked with the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/).

   <details>
   <summary>CSS Results</summary>

   ![image](https://user-images.githubusercontent.com/98277650/187975424-1d87fd98-b930-4009-874a-adbb4210bd86.png)

   </details>
   
* Python Validation

  All Python code was checked with the [PEP8 Online Service](http://pep8online.com/).

  <details>
  <summary>admin.py</summary>

  ![image](https://user-images.githubusercontent.com/98277650/188003211-31fd93b3-c8bb-4e13-ab52-b9ef5f929f03.png)

  </details>
  <details>
  <summary>apps.py</summary>

  ![image](https://user-images.githubusercontent.com/98277650/188003527-aa13b4d9-f627-474e-a6d2-8aafae96a2f9.png)

  </details>
  <details>
  <summary>forms.py</summary>

  ![image](https://user-images.githubusercontent.com/98277650/188004880-1f45b1fa-234b-42d9-9b09-01a9201fb825.png)

  </details>
  <details>
  <summary>models.py</summary>

  ![image](https://user-images.githubusercontent.com/98277650/188005177-1c8a8ed1-2d8a-4de6-aab0-e5c2b07e8efc.png)

  </details>
  <details>
  <summary>urls.py</summary>

  ![image](https://user-images.githubusercontent.com/98277650/188005370-ba06262e-cb7e-4d7f-b5a2-443bd9b1282a.png)

  </details>
  <details>
  <summary>views.py</summary>

  ![image](https://user-images.githubusercontent.com/98277650/188005494-cc4cd2bd-4cd8-446a-a2a2-0681761026f8.png)

  </details>

* Accessibility

accessibility tested with the [WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/).

  <details>
  <summary>WAVE report</summary>

  ![image](static/images/readme/wave.png)

  </details>

## Testing

  Websit is responsive, tested it on different screen sizes (including cellphones screens).

  <details><summary>Google Doc</summary>

  ![image](static/images/readme/manual-testing.png)

  </details>

***

## Bugs
This project was specially difficult for me in . 

***

# Deployment
* Code Institute template was use to create project
* Make instalations in Gitpod
* As per tutorial recommendations, project was deployed from first commitment.
* App created in Heroku
* Configurations in Heroku were set up as per tutorial recoomendations
* Click on Deploy in Heroku

***

# Credits
My project was heavily based on Code Institute tutorials. I also learnt different approaches from Youtube and reutilize code from several projects.