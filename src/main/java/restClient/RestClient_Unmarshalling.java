package restClient;

import javax.ws.rs.client.Invocation;
import javax.ws.rs.client.WebTarget;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;


public class RestClient_Unmarshalling extends RestClient
{

	public RestClient_Unmarshalling(String hostname, String port)
	{
		super(hostname, port);
	}


	public void makeGetRequest(String resource_URL) throws Exception
	{
		WebTarget getRequestController = super.webTarget.path(resource_URL);
		Invocation.Builder invocationBuilder = getRequestController.request(MediaType.APPLICATION_JSON);

		System.out.println("Java Jersey Client performing GET request to " +
				String.format("http://%s:%s%s",
						webTarget.getUri().getHost(),
						webTarget.getUri().getPort(),
						webTarget.getUri().getRawPath()
				));

		Response response = invocationBuilder.get();
		System.out.println("Java Jersey Client received the following output:");
		System.out.println(response.toString());

		if ( request_OK( response.getStatus() ) )
		{
			System.out.println("Successfully made Get request");
			System.out.println("Goint to print response content without unmarshalling");
			// From wikipedia "marshalling is the process of transforming the memory representation of an object to a data format suitable for storage or transmission"
			// So unmarshalling means reconverting it back to the object
			print_with_unmarshalling(response);
		}
		else
		{
			System.out.println("BadAss error happened");
			System.exit(-1);
		}
	}


	public void print_with_unmarshalling(Response response)
	{
		// this method prints the result obtained from the resource directly as a JSON string
		//todo
		String message = response.readEntity(String.class);
		System.out.println(message);
	}




	public static void main(String[] args)
	{
		// This must be verified so that they point to the respective microservices
		String hostname = "127.0.0.1";
		String port_auth = "5000";
		String port_pay = "5001";
		String port_airlines = "5002";


		/************************************************
		 *
		 * Some tests with authentication microservice
		 *
		 *
		 * [Done] Test Message
		 * curl http://127.0.0.1:5000/
		 *
		 * Log in test message
		 * curl http://127.0.0.1:5000/Authentication/Log_in
		 *
		 * [Done] Log in
		 * curl http://127.0.0.1:5000/Authentication/Log_in -d '{"email":"inigo.lopezgazpio@deusto.es", "password":"XXX" }' -X POST -H "Content-Type: application/json" -v
		 *
		 * Create user test message
		 * curl http://127.0.0.1:5000/Authentication/Create_user
		 *
		 * [Done] Create user
		 * curl http://127.0.0.1:5000/Authentication/Create_user -d '{"name":"Inigo", "last_name":"Lopez-Gazpio", "email":"inigo.lopezgazpio@deusto.es"}' -X POST -H "Content-Type: application/json" -v
		 *
		 * Change passwd test message
		 * curl http://127.0.0.1:5000/Authentication/Change_password
		 *
		 * [Done] Change passwd
		 * curl http://127.0.0.1:5000/Authentication/Change_password -d '{"email":"inigo.lopezgazpio@deusto.es", "password":"XXX", "password_new":"XXX"}' -X PUT -H "Content-Type: application/json" -v
		 *
		 * [Done] Delete user test message
		 * curl http://127.0.0.1:5000/Authentication/Delete_user
		 *
		 * Delete user
		 * curl http://127.0.0.1:5000/Authentication/Delete_user -d '{"email":"inigo.lopezgazpio@deusto.es", "password":"XXX" }' -X DELETE -H "Content-Type: application/json" -v
		 ************************************************/
		RestClient_Unmarshalling c1 = new RestClient_Unmarshalling(hostname, port_auth);
		// Some requests to the microservices... check the microservices are online previously with curl! check the docs for this

		try {
			// All this are just ping requests
			c1.makeGetRequest("/");
			c1.makeGetRequest("/Authentication/Log_in");
			c1.makeGetRequest("/Authentication/Create_user");
			c1.makeGetRequest("/Authentication/Change_password");
			c1.makeGetRequest("/Authentication/Delete_user");

			// real requests

			// todo c1.makePostRequest("This is a client super complex message to send to server");
		} catch (Exception e) {
			System.out.println("Catched exception: " + e.getMessage());
		}







		/*********************************************
		 *
		 * Some tests with payment microservice
		 *
		 * [DONE] Test message
		 * curl http://127.0.0.1:5001/
		 *
		 * [DONE] Make payment test message
		 * curl http://127.0.0.1:5001/Payments/Make_payment
		 *
		 * Make payment
		 * curl http://127.0.0.1:5001/Payments/Make_payment -d '{"email":"inigo.lopezgazpio@deusto.es", "total_amount":"20.5", "concept":"Hello World Payment" }' -X POST -H "Content-Type: application/json" -v
		 *
		 * [DONE] Create user test message
		 * curl http://127.0.0.1:5001/Payments/Create_user
		 *
		 * Create user
		 * curl http://127.0.0.1:5001/Payments/Create_user -d '{"name":"Inigo", "last_name":"Lopez-Gazpio", "email":"inigo.lopezgazpio@deusto.es", "currency":"20.5"}' -X POST -H "Content-Type: application/json" -v
		 *
		 * [DONE] Update currency test message
		 * curl http://127.0.0.1:5001/Payments/Update_currency
		 *
		 * Update currency
		 * curl http://127.0.0.1:5001/Payments/Update_currency -d '{"email":"inigo.lopezgazpio@deusto.es", "currency":"100"}' -X PUT -H "Content-Type: application/json" -v
		 *********************************************/
		RestClient_Unmarshalling c2 = new RestClient_Unmarshalling(hostname, port_pay);

		try {
			c2.makeGetRequest("/");
			c2.makeGetRequest("/Payments/Make_payment");
			c2.makeGetRequest("/Payments/Create_user");
			c2.makeGetRequest("/Payments/Update_currency");

			// todo c2.makePostRequest("This is a client super complex message to send to server");
		} catch (Exception e) {
			System.out.println("Catched exception: " + e.getMessage());
		}


		/**************************************************
		 *
		 * Some tests with airlines microservice
		 *
		 * [DONE] Test message
		 * curl http://127.0.0.1:5000/Airlines/Search_Flights
		 *
		 * Search all flights
		 * curl http://127.0.0.1:5000/Airlines/Search_Flights -d '{ }' -X POST -H "Content-Type: application/json" -v
		 *
		 * Search flights by both: airport_departure_name and airport_arrival_name
		 * curl http://127.0.0.1:5000/Airlines/Search_Flights -d '{"airport_departure_name":"Hondarribia", "airport_arrival_name":"Tabarnia" }' -X POST -H "Content-Type: application/json" -v
		 *
		 * Search flights also by free seats available (At least XXX free seats)
		 * curl http://127.0.0.1:5000/Airlines/Search_Flights -d '{"airport_departure_name":"Hondarribia", "airport_arrival_name":"Tabarnia", "free_seats":"100" }' -X POST -H "Content-Type: application/json" -v
		 *
		 * Search flights also by maximum price
		 * curl http://127.0.0.1:5000/Airlines/Search_Flights -d '{"airport_departure_name":"Hondarribia", "airport_arrival_name":"Tabarnia", "free_seats":"100", "price":"700" }' -X POST -H "Content-Type: application/json" -v
		 *
		 * Search flights also by proximity to departure date (between given date and given date + 10 days)
		 * curl http://127.0.0.1:5000/Airlines/Search_Flights -d '{"airport_departure_name":"Hondarribia", "airport_arrival_name":"Tabarnia", "free_seats":"100", "price":"700", "departure_date":"2020/04/03 09:00:00" }' -X POST -H "Content-Type: application/json" -v
		 **************************************************/
		RestClient_Unmarshalling c3 = new RestClient_Unmarshalling(hostname, port_airlines);

		try {
			c3.makeGetRequest("/");

			// todo c1.makePostRequest("This is a client super complex message to send to server");
		} catch (Exception e) {
			System.out.println("Catched exception: " + e.getMessage());
		}
	}
}
