# photography_website

 This is a photography website developed using django. I have used html, css, sass and javascript for frontend and Django for backend.

# Lets see the features of the website

  * This website is designed to communicate with the customers who wants photography service, the customer can place their order in the `contact` page.

  * This website is used to display the photography and videography content.

  * I have used `django-resized` module to reduce the size of the image, so that the buffering can reduced.

  ```python
      image = ResizedImageField(size=[1000, 1000], quality=99)
  ```
  * The admin can view the orders placed by customers in admin page.

  # AWS
    
* This website uses Postgresql database from amazon RDS. so the database is more powerfull.

* The static and media files are served in amazon S3 buckets. 

# Heroku
 * This website is deployed in Heroku platform. so anyone can view it.
 [ click here to view](https://smilestudios.herokuapp.com/)

# Contribution
  
  * If any one intrested in contributing this website, contributers are always welcome :blush:

