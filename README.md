### Detailed breakdown of the workflow -

 ### endpoints for seller side. (Words in Bold indicates table names)

 
-[ ]  seller signs up using his mobile number that creates an **account**
	-[x]  Take mobile number & OTP (random) as input to the API
	-[x]  Create customer account in accounts table.
	-[x]  Issue a token.  

-[ ]  seller creates his **store**
	-[x]  Take store name & address as input.  
	-[x]  Create store in store table. One customer can have multiple stores.
	-[x]  Generate a unique store link based on his store name.
	-[x]  Respond back with storeid and link.

-[ ]  seller starts uploading inventory in the form of **products** and **seller**.
	-[x]  Take product name, description, MRP, Sale price, image & category as input.  
	-[x]  Create a category if it doesn't exist.
	-[x]  Create product
	-[x]  Respond back with id, name and image.
	 
  
-[ ]  Seller can accept **orders** from his **customers**.
	-[x]  Create a customer table with a mobile number as unique and address details.    
	-[x]  Create a order table to store orders data.
	-[x]  When someone places an order from the buyer side, the records will be saved here.
	   

### Endpoints for Buyer side

 
-[ ]  Seller shares his store link with his customers. To get basic store details
	-[ ]  Take store link as input    
	-[x]  Respond back with storeId, store name, address

-[ ]  To get product catalog & categories
	-[ ]  Take storelink as input    
	-[x]  Respond back with the catelog, grouped by categories & sorted by number of products in the category.

-[ ]  people (Un-authenticated users) can add items into their cart.
	-[ ]  Maintain a cart on the server in either DB or redis or MongoDb    
	-[ ]  On cart change (add / remove item) update the cart on server
	-[ ]  For cart line items take product id, qty, storeLink as input and fetch product meta data from the DB and save them.
  
-[ ]  Customer place an order for a product. 
	-[x]  Identity customer using JWT or token which can be generated using his mobile number and a OTP 
	-[x]  Bypass the actual OTP validation flow and issue a token on any random number & OTP combination
	-[x]  Create a customer record if didn’t already exist for that mobile number.
	-[ ]  Take the cart object as input and convert that into an order.
	-[x]  Create an order for that store & customer and return back the order id.