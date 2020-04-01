package Demo;

import MicroserviceDataFormat.Pay_MicroService.P_User;
import restClient.RestClient;

public class Jersey_Pay_Client_Requests
{

    // mvn clean compile exec:java -PJersey_Pay_Client_Requests
    public static void main (String [] args)
    {

        // Some requests to the microservices... check the microservices are online previously with curl! check the docs for this

        System.out.println("-------------------------------------------------------");
        System.out.println("Payments Server test (GET) ");
        System.out.println("-------------------------------------------------------");

        String path = "/";
        System.out.println("Trying GET at " + path + " (Test message)");
        System.out.println("CURL call: curl http://127.0.0.1:5001/");

        // Note below we instantiate a RestClient generic class to be used with P_User class
        RestClient<P_User> client = new RestClient<>(args[0], args[1]);

        try {
                client.simplePrint(
                        client.makeGetRequest(
                                client.createInvocationBuilder(path)
                        )
                );
        }
        catch (Exception e) { e.printStackTrace(); e.toString(); }








        System.out.println("-------------------------------------------------------");
        System.out.println("Make payment Server test (GET) ");
        System.out.println("-------------------------------------------------------");

        path = "/Payments/Make_payment";
        System.out.println("Trying GET at " + path + " (Test message)");
        System.out.println("CURL call: curl http://127.0.0.1:5001/Payments/Make_payment");

        try {
            client.simplePrint(
                    client.makeGetRequest(
                            client.createInvocationBuilder(path)
                    )
            );
        }
        catch (Exception e) { e.printStackTrace(); e.toString(); }









        System.out.println("-------------------------------------------------------");
        System.out.println("Make payment Server test (POST)");
        System.out.println("-------------------------------------------------------");

        path = "/Payments/Make_payment";
        System.out.println("Trying POST at " + path );
        System.out.println("CURL call: curl http://127.0.0.1:5001/Payments/Make_payment -d '{\"email\":\"inigo.lopezgazpio@deusto.es\", \"total_amount\":\"20.5\", \"concept\":\"Hello World Payment\" }' -X POST -H \"Content-Type: application/json\" -v");

        try {
            client.simplePrint(
                    client.makePostRequest(
                            client.createInvocationBuilder(path) , new P_User("inigo.lopezgazpio@deusto.es", 100, "Hello World Payment")
                    )
            );
        }
        catch (Exception e) { e.printStackTrace(); e.toString(); }

        System.out.println("Note that we obtain a false result because the user does not exist in the Payments microservice");











        System.out.println("-------------------------------------------------------");
        System.out.println("Create_user Server test (GET) ");
        System.out.println("-------------------------------------------------------");

        path = "/Payments/Create_user";
        System.out.println("Trying GET at " + path + " (Test message)");
        System.out.println("CURL call: curl http://127.0.0.1:5001/Payments/Create_user");

        try {
            client.simplePrint(
                    client.makeGetRequest(
                            client.createInvocationBuilder(path)
                    )
            );
        }
        catch (Exception e) { e.printStackTrace(); e.toString(); }











        System.out.println("-------------------------------------------------------");
        System.out.println("Create_user Server test (POST)");
        System.out.println("-------------------------------------------------------");

        path = "/Payments/Create_user";
        System.out.println("Trying POST at " + path );
        System.out.println("CURL call: curl http://127.0.0.1:5001/Payments/Create_user -d '{\"name\":\"Inigo\", \"last_name\":\"Lopez-Gazpio\", \"email\":\"inigo.lopezgazpio@deusto.es\", \"currency\":\"20.5\"}' -X POST -H \"Content-Type: application/json\" -v");

        try {
            client.simplePrint(
                    client.makePostRequest(
                            client.createInvocationBuilder(path) , new P_User("Inigo", "Lopez-Gazpio", "inigo.lopezgazpio@deusto.es", 10000)
                    )
            );
        }
        catch (Exception e) { e.printStackTrace(); e.toString(); }

        System.out.println("Now that we have a user with currency we can perform a payment with success");










        System.out.println("------------------------------------------------------");
        System.out.println("Make payment Server test (POST)");
        System.out.println("------------------------------------------------------");

        path = "/Payments/Make_payment";
        System.out.println("Trying POST at " + path );
        System.out.println("CURL call: curl http://127.0.0.1:5001/Payments/Make_payment -d '{\"email\":\"inigo.lopezgazpio@deusto.es\", \"total_amount\":\"20.5\", \"concept\":\"Hello World Payment\" }' -X POST -H \"Content-Type: application/json\" -v");

        try {
            client.simplePrint(
                    client.makePostRequest(
                            client.createInvocationBuilder(path) , new P_User("inigo.lopezgazpio@deusto.es", 100, "Hello World Payment")
                    )
            );
        }
        catch (Exception e) { e.printStackTrace(); e.toString(); }

        System.out.println("We now obtain a success :)");






        System.out.println("-------------------------------------------------------");
        System.out.println("Update currency Server test (GET) ");
        System.out.println("-------------------------------------------------------");

        path = "/Payments/Update_currency";
        System.out.println("Trying GET at " + path + " (Test message)");
        System.out.println("CURL call: curl http://127.0.0.1:5001/Payments/Update_currency");

        try {
            client.simplePrint(
                    client.makeGetRequest(
                            client.createInvocationBuilder(path)
                    )
            );
        }
        catch (Exception e) { e.printStackTrace(); e.toString(); }







        System.out.println("------------------------------------------------------");
        System.out.println("Update currency Server test (POST)");
        System.out.println("------------------------------------------------------");

        path = "/Payments/Update_currency";
        System.out.println("Trying POST at " + path );
        System.out.println("CURL call: curl http://127.0.0.1:5001/Payments/Update_currency -d '{\"email\":\"inigo.lopezgazpio@deusto.es\", \"currency\":\"100\"}' -X PUT -H \"Content-Type: application/json\" -v");

        try {
            client.simplePrint(
                    client.makePostRequest(
                            client.createInvocationBuilder(path) , new P_User("inigo.lopezgazpio@deusto.es",10000)
                    )
            );
        }
        catch (Exception e) { e.printStackTrace(); e.toString(); }

        System.out.println("We now obtain an error, be careful because this call is not a POST request but a PUT request");









        System.out.println("-------------------------------------------------------");
        System.out.println("Update currency Server test (POST)");
        System.out.println("-------------------------------------------------------");

        path = "/Payments/Update_currency";
        System.out.println("Trying POST at " + path );
        System.out.println("CURL call: curl http://127.0.0.1:5001/Payments/Update_currency -d '{\"email\":\"inigo.lopezgazpio@deusto.es\", \"currency\":\"100\"}' -X PUT -H \"Content-Type: application/json\" -v");

        try {
            client.simplePrint(
                    client.makePutRequest(
                            client.createInvocationBuilder(path) , new P_User("inigo.lopezgazpio@deusto.es",10000)
                    )
            );
        }
        catch (Exception e) { e.printStackTrace(); e.toString(); }

        System.out.println("We now obtain a success :)");
    }
}
