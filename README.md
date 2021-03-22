### Detailed breakdown of the workflow -

 ### endpoints for seller side. (Words in Bold indicates table names)

 
1.  seller signs up using his mobile number that creates an **account**
	-[X]  Take mobile number & OTP (random) as input to the API
	-[X]  Create customer account in accounts table.
	-[X]  Issue a token.  

2.  seller creates his **store**
	-[X]  Take store name & address as input.  
	-[X]  Create store in store table. One customer can have multiple stores.
	-[X]  Generate a unique store link based on his store name.
	-[X]  Respond back with storeid and link.

3.  seller starts uploading inventory in the form of **products** and **seller**.
	-[X]  Take product name, description, MRP, Sale price, image & category as input.  
	-[X]  Create a category if it doesn't exist.
	-[X]  Create product
	-[X]  Respond back with id, name and image.
	 
  
4.  Seller can accept **orders** from his **customers**.
	-[X]  Create a customer table with a mobile number as unique and address details.    
	-[X]  Create a order table to store orders data.
	-[X]  When someone places an order from the buyer side, the records will be saved here.
	   

### Endpoints for Buyer side

 
1.  Seller shares his store link with his customers. To get basic store details
	-[ ]  Take store link as input    
	-[X]  Respond back with storeId, store name, address

2.  To get product catalog & categories
	-[ ]  Take storelink as input    
	-[X]  Respond back with the catelog, grouped by categories & sorted by number of products in the category.

3.  people (Un-authenticated users) can add items into their cart.
	-[ ]  Maintain a cart on the server in either DB or redis or MongoDb    
	-[ ]  On cart change (add / remove item) update the cart on server
	-[ ]  For cart line items take product id, qty, storeLink as input and fetch product meta data from the DB and save them.
  
4.  Customer place an order for a product. 
	-[X]  Identity customer using JWT or token which can be generated using his mobile number and a OTP 
	-[X]  Bypass the actual OTP validation flow and issue a token on any random number & OTP combination
	-[X]  Create a customer record if didn’t already exist for that mobile number.
	-[ ]  Take the cart object as input and convert that into an order.
	-[X]  Create an order for that store & customer and return back the order id.