### Running on development machine

    # Clone repository
    git@github.com:ShubhamKhandare/storeio.git
     OR
    https://github.com/ShubhamKhandare/storeio.git
    
    # Change into project directory
    cd storeio
    
    # Make virtual environment [Optional]
    mkvirtualenv <project_name>
    
    # Activate virtual environment [Optional]
    workon <project_name>
    
    # Install requirements
    pip install -r requirements.txt
    
    # Check migrations
    python manage.py makemigrations
    
    # Run migrations
    python manage.py migrate
    
    # Start the development server
    python manage.py runserver
    
### Postman API collection
    - Import postman collection JSON from `extra/` folder
    - Refer: https://learning.postman.com/docs/getting-started/importing-and-exporting-data/#importing-data-into-postman
 
### Rough Database design
    - Link: https://drive.google.com/file/d/1Ss8shX80w5rb9of1gFEJIBU4k8b0IZ45/view?usp=sharing
    - Created with webapp app.diagrams.net 
   
### Detailed breakdown of the workflow -

 ### endpoints for seller side. (Words in Bold indicates table names)
 
- [x]  seller signs up using his mobile number that creates an **account**
	- [x]  Take mobile number & OTP (random) as input to the API
	- [x]  Create customer account in accounts table.
	- [x]  Issue a token.  

- [x]  seller creates his **store**
	- [x]  Take store name & address as input.  
	- [x]  Create store in store table. One customer can have multiple stores.
	- [x]  Generate a unique store link based on his store name.
	- [x]  Respond back with store id and link.

- [x]  seller starts uploading inventory in the form of **products** and **seller**.
	- [x]  Take product name, description, MRP, Sale price, image & category as input.  
	- [x]  Create a category if it doesn't exist.
	- [x]  Create product
	- [x]  Respond back with id, name and image.
	 
  
- [x]  Seller can accept **orders** from his **customers**.
	- [x]  Create a customer table with a mobile number as unique and address details.    
	- [x]  Create a order table to store orders data.
	- [x]  When someone places an order from the buyer side, the records will be saved here.
	   

### Endpoints for Buyer side

 
- [x]  Seller shares his store link with his customers. To get basic store details
	- [x]  Take store link as input    
	- [x]  Respond back with storeId, store name, address

- [x]  To get product catalog & categories
	- [x]  Take store link as input    
	- [x]  Respond back with the catalog, grouped by categories & sorted by number of products in the category.

- [x]  people (Un-authenticated users) can add items into their cart.
	- [x]  Maintain a cart on the server in either DB or redis or MongoDb    
	- [x]  On cart change (add / remove item) update the cart on server
	- [x]  For cart line items take product id, qty, storeLink as input and fetch product meta data from the DB and save them.
  
- [x]  Customer place an order for a product. 
	- [x]  Identity customer using JWT or token which can be generated using his mobile number and a OTP 
	- [x]  Bypass the actual OTP validation flow and issue a token on any random number & OTP combination
	- [x]  Create a customer record if didn't already exist for that mobile number.
	- [x]  Take the cart object as input and convert that into an order.
	- [x]  Create an order for that store & customer and return back the order id.
