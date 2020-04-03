# UD_Software_Design_EasyBooking_External_Services
Code repository for the external services of the EasyBooking application (Software Design Deusto ADE + Inf).
This repository contains both:
1. Server side implementation of the external microservices ( implemented with python and flask_restful )
2. Client side implementation of the external microservices ( implemented with Java and Jersey )

# Step 1 - How to launch the microservices

Authentication, Payments and Airlines microservices are located under the ```src/main/python``` folder respectively.
Each one follows the abstraction (the methods) defined in the interface, which are the following ones:

1) Authentication microservice interface (**Interface_Authentication.py**)

```
    @abstractmethod
    def log_in( self, email: str, password: str) -> bool:
        """                                                                                                                                                                                  
        Method to log in an existing user                                                                                                                                                        
        Returns boolean, True <=> Correct login                                                                                                                                                  
        """
        pass


    @abstractmethod
    def create_user( self, user: User) -> str:
        """                                                                                                                                                                                      
        Method to create a new user with password                                                                                                                                                
        Returns string with password for created user or None if user is not created                                                                                                             
        """
        pass


    @abstractmethod
    def change_password(self, email: str, password_old: str, password_new: str) -> bool:
        """                                                                                                                                                                                      
        Method to update password                                                                                                                                                                
        Returns boolean, True <=> Correct update                                                                                                                                                 
        """
        pass


    @abstractmethod
    def delete_user( self, email: str, password: str) -> bool:
        """                                                                                                                                                                                      
        Method to delete an existing user                                                                                                                                                        
        Returns boolean, True <=> Correct deletion                                                                                                                                               
        """
        pass
```

2) Payments microservice interface (**Payments microservice interface**)
```
 @abstractmethod
    def make_payment(self, email: str, total_amount : float, concept : str) -> str:
        """                                                                                                                                                                                      
        Method to log in an existing user                                                                                                                                                        
        Returns receipt id                                                                                                                                                                       
        """
	pass

    @abstractmethod
    def create_user(self, user: UserAccount, currency : float) -> bool:
	"""                                                                                                                                                                                      
        Method to create a new user with some currency                                                                                                                                           
        Returns boolean, True <=> Correct update                                                                                                                                                 
        """
	pass

    @abstractmethod
    def update_currency(self, email: str, currency: float) -> bool:
	"""                                                                                                                                                                                      
        Method to update currency of user                                                                                                                                                        
        Returns boolean, True <=> Correct update                                                                                                                                                 
        """
	pass
```

3) Airlines microservice interface (**Interface_Airlines.py**)
```
    @abstractmethod
    def search_flights( self, **kwparams) -> [ Flight ]:
        """                                                                                                                                                                                      
        Method to query airline for all flights                                                                                                                                                                                                                                                                                                                        
        Returns a list of flights according to the filters passed                                                                                                                                
        """
	pass
```


Currently these code provides 3 microservices that follow the mentioned abstractions:
1) DeustoAuth
2) DeustoPay
3) DeustoAirlines

which can be launched using these scripts:
```
python3.6 launch_DeustoAuth_micro_service.py       --host 127.0.0.1 --port 5000
python3.6 launch_DeustoPay_micro_service.py        --host 127.0.0.1 --port 5001
python3.6 launch_DeustoAirlines_micro_service.py   --host 127.0.0.1 --port 5002
```

the requirements are described below:
```
python3
flask
flask_restful
json
bson
pymongo
jsonpickle

```


# Step 2 - How to make direct (through curl) calls to the microservices

Each microservice defines different resources to be used by the clients.
The following code shows how to call the resources **using curl**

#### Requests related to DeustoAuth microservice
```
Test Message
curl http://127.0.0.1:5000/

Log in test message
curl http://127.0.0.1:5000/Authentication/Log_in

Log in
curl http://127.0.0.1:5000/Authentication/Log_in -d '{"email":"inigo.lopezgazpio@deusto.es", "password":"XXX" }' -X POST -H "Content-Type: application/json" -v

Create user test message
curl http://127.0.0.1:5000/Authentication/Create_user

Create user
curl http://127.0.0.1:5000/Authentication/Create_user -d '{"name":"Inigo", "last_name":"Lopez-Gazpio", "email":"inigo.lopezgazpio@deusto.es"}' -X POST -H "Content-Type: application/json" -v

Change passwd test message
curl http://127.0.0.1:5000/Authentication/Change_password

Change passwd
curl http://127.0.0.1:5000/Authentication/Change_password -d '{"email":"inigo.lopezgazpio@deusto.es", "password":"XXX", "password_new":"XXX"}' -X PUT -H "Content-Type: application/json" -v

Delete user test message
curl http://127.0.0.1:5000/Authentication/Delete_user

Delete user
curl http://127.0.0.1:5000/Authentication/Delete_user -d '{"email":"inigo.lopezgazpio@deusto.es", "password":"XXX" }' -X PUT -H "Content-Type: application/json" -v

```

The message parsing format is defined as:
```
user_parser = reqparse.RequestParser()
user_parser.add_argument('name', type=str, help= "User name")
user_parser.add_argument('last_name', type=str, help= "User last name")
user_parser.add_argument('email', type=str, help= "User email")
user_parser.add_argument('password', type=str, help= "Current password")
user_parser.add_argument('password_new', type=str, help= "New password")
```

#### Requests related to DeustoPay microservice
```
Test message
curl http://127.0.0.1:5001/

Make payment test message
curl http://127.0.0.1:5001/Payments/Make_payment 

Make payment
curl http://127.0.0.1:5001/Payments/Make_payment -d '{"email":"inigo.lopezgazpio@deusto.es", "total_amount":"20.5", "concept":"Hello World Payment" }' -X POST -H "Content-Type: application/json" -v

Create user test message
curl http://127.0.0.1:5001/Payments/Create_user

Create user
curl http://127.0.0.1:5001/Payments/Create_user -d '{"name":"Inigo", "last_name":"Lopez-Gazpio", "email":"inigo.lopezgazpio@deusto.es", "currency":"20.5"}' -X POST -H "Content-Type: application/json" -v

Update currency test message
curl http://127.0.0.1:5001/Payments/Update_currency

Update currency
curl http://127.0.0.1:5001/Payments/Update_currency -d '{"email":"inigo.lopezgazpio@deusto.es", "currency":"100"}' -X PUT -H "Content-Type: application/json" -v

```

The message parsing format is defined as:
```
user_parser = reqparse.RequestParser()
user_parser.add_argument('name', type=str, help= "User name")
user_parser.add_argument('last_name', type=str, help= "User last name")
user_parser.add_argument('email', type=str, help= "User email")
user_parser.add_argument('total_amount', type=float, help= "Payment amount")
user_parser.add_argument('concept', type=str, help= "Payment concept string")
user_parser.add_argument('currency', type=float, help= "Initial currency")
```

#### Requests related to DeustoAirlines microservice
```
Test message
curl http://127.0.0.1:5002/Airlines/Search_Flights

Search all flights
curl http://127.0.0.1:5002/Airlines/Search_Flights -d '{ }' -X POST -H "Content-Type: application/json" -v                                                                                                                              

Search flights by both: airport_departure_name and airport_arrival_name
curl http://127.0.0.1:5002/Airlines/Search_Flights -d '{"airport_departure_name":"Hondarribia", "airport_arrival_name":"Tabarnia" }' -X POST -H "Content-Type: application/json" -v                                                     

Search flights also by free seats available (At least XXX free seats)
curl http://127.0.0.1:5002/Airlines/Search_Flights -d '{"airport_departure_name":"Hondarribia", "airport_arrival_name":"Tabarnia", "free_seats":"100" }' -X POST -H "Content-Type: application/json" -v                                 
    
Search flights also by maximum price 
curl http://127.0.0.1:5002/Airlines/Search_Flights -d '{"airport_departure_name":"Hondarribia", "airport_arrival_name":"Tabarnia", "free_seats":"100", "price":"700" }' -X POST -H "Content-Type: application/json" -v                  

Search flights also by proximity to departure date (between given date and given date + 10 days) 
curl http://127.0.0.1:5002/Airlines/Search_Flights -d '{"airport_departure_name":"Hondarribia", "airport_arrival_name":"Tabarnia", "free_seats":"100", "price":"700", "departure_date":"2020/04/03 09:00:00" }' -X POST -H "Content-Type: application/json" -v   

```

The message parsing format is defined as:
```
flight_parser = reqparse.RequestParser()
flight_parser.add_argument('airport_departure_name', type=str, help= "Departure airport name", required=False)
flight_parser.add_argument('airport_arrival_name', type=str, help= "Arrival airport name", required=False)
flight_parser.add_argument('free_seats', type=int, help= "Minimum number of free seats in flight", required=False)
flight_parser.add_argument('price', type=float, help= "Maximum price of flight", required=False)
flight_parser.add_argument('departure_date', type=str, help= "String to be parsed to datetime value following %Y/%m/%d %H:%M:%S format", required=False)
```


# Step 3 - How to make Java calls to the microservices
The pom.xml included in this repository has some profiles that call Java files under ```src/main/java``` with sample tests. 
The host and port parameters must be verified in the properties of the pom so that they point to the correct microservices.

To launch **Jersey_Auth_Client_Requests**:
```
mvn clean
mvn compile
mvn exec:java -PJersey_Auth_Client_Requests

or

mvn clean compile exec:java -PJersey_Auth_Client_Requests
```

To launch **Jersey_Pay_Client_Requests**:
```
mvn clean
mvn compile
mvn exec:java -PJersey_Pay_Client_Requests

or 

mvn clean compile exec:java -PJersey_Pay_Client_Requests

```

To launch **Jersey_Airlines_Client_Requests**:
```
mvn clean
mvn compile
mvn exec:java -PJersey_Airlines_Client_Requests

or

mvn clean compile exec:java -PJersey_Airlines_Client_Requests
```
