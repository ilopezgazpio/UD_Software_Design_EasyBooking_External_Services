package Demo;

import MarshallingClasses.Auth_MicroService.Simple_pass_result;
import MicroserviceDataFormat.Auth_MicroService.A_User;
import org.json.simple.parser.JSONParser;
import restClient.RestClient;
import org.json.simple.JSONObject;

import javax.ws.rs.core.Response;

public class Jersey_Auth_Client_Requests
{

    // mvn clean compile exec:java -PJersey_Auth_Client_Requests
    public static void main (String [] args)
    {
        // Some requests to the microservices... check the microservices are online previously with curl! check the docs for this

        System.out.println("-------------------------------------------------------");
        System.out.println("Authentication Server test");
        System.out.println("-------------------------------------------------------");

        String path = "/";
        System.out.println("Trying GET at " + path + " (Test message)");
        System.out.println("CURL call: curl http://127.0.0.1:5000/");

        // Note below we instantiate a RestClient generic class to be used with A_User class
        RestClient<A_User> client = new RestClient<>(args[0], args[1]);

        try {
                client.simplePrint(
                        client.makeGetRequest(
                                client.createInvocationBuilder(path)
                        )
                );
        }
        catch (Exception e) { e.printStackTrace(); e.toString(); }









        System.out.println("------------------------------------------------------");
        System.out.println("Authentication Login Server test (GET) ");
        System.out.println("------------------------------------------------------");

        path = "/Authentication/Log_in";
        System.out.println("Trying GET at " + path + " (Log in Test message)");
        System.out.println("CURL call: curl http://127.0.0.1:5000/Authentication/Log_in");

        try {
            client.simplePrint(
                    client.makeGetRequest(
                            client.createInvocationBuilder(path)
                    )
            );
        }
        catch (Exception e) { e.printStackTrace(); e.toString(); }








        System.out.println("-------------------------------------------------------");
        System.out.println("Authentication Login Server test (POST)");
        System.out.println("-------------------------------------------------------");

        path = "/Authentication/Log_in";
        System.out.println("Trying POST at " + path + " (Log in service)");
        System.out.println("CURL call: curl http://127.0.0.1:5000/Authentication/Log_in -d '{\"email\":\"inigo.lopezgazpio@deusto.es\", \"password\":\"XXX\" }' -X POST -H \"Content-Type: application/json\" -v");

        Response response = null;
        try {
            response =
                    client.makePostRequest(
                            client.createInvocationBuilder(path) , new A_User("inigo.lopezgazpio@deusto.es", "XXX")

            );
        }
        catch (Exception e) { e.printStackTrace(); e.toString(); }
        client.simplePrint(response);
        System.out.println("We obtain a false as the user has not been created");












        System.out.println("-------------------------------------------------------");
        System.out.println("Authentication Create User Server test (GET)");
        System.out.println("-------------------------------------------------------");

        path = "/Authentication/Create_user";
        System.out.println("Trying GET at " + path + " (Create user test message)");
        System.out.println("CURL call: curl http://127.0.0.1:5000/Authentication/Create_user");

        try {
            client.simplePrint(
                    client.makeGetRequest(
                            client.createInvocationBuilder(path)
                    )
            );
        }
        catch (Exception e) { e.printStackTrace(); e.toString(); }










        System.out.println("-------------------------------------------------------");
        System.out.println("Authentication Create User Server test (POST)");
        System.out.println("-------------------------------------------------------");


        path = "/Authentication/Create_user";
        System.out.println("Trying POST at " + path + " (Create user)");
        System.out.println("CURL call: curl http://127.0.0.1:5000/Authentication/Create_user -d '{\"name\":\"Inigo\", \"last_name\":\"Lopez-Gazpio\", \"email\":\"inigo.lopezgazpio@deusto.es\"}' -X POST -H \"Content-Type: application/json\" -v");

        try {
            client.simplePrint(
                    client.makePostRequest(
                            client.createInvocationBuilder(path), new A_User("Inigo", "Lopez-Gazpio", "test@deusto.es")
                    )
            );
        }
        catch (Exception e) { e.printStackTrace(); e.toString(); }


        System.out.println("We obtain the password in the response of the reply, to get this value we will need to parse the result (Marshalling)");



        Simple_pass_result result_class_password = null;
        try {
            response =
                    client.makePostRequest(
                            client.createInvocationBuilder(path), new A_User("Inigo", "Lopez-Gazpio", "inigo.lopezgazpio@deusto.es")
                    );
        }
        catch (Exception e) { e.printStackTrace(); e.toString(); }

        String reply = response.readEntity(String.class);

        // Create a JSONObject to parse the respond inside the Simple_pass_result
        try {
            result_class_password = new Simple_pass_result(reply);
        } catch (Exception e) {e.printStackTrace(); e.toString(); }

        result_class_password.print();

        long password = result_class_password.getContentNumber();











        System.out.println("--------------------------------------------------------");
        System.out.println("Authentication Change Password Server test (GET)");
        System.out.println("--------------------------------------------------------");

        path = "/Authentication/Change_password";
        System.out.println("Trying GET at " + path + " (Change_password test message)");
        System.out.println("CURL call: curl http://127.0.0.1:5000/Authentication/Change_password");

        try {
            client.simplePrint(
                    client.makeGetRequest(
                            client.createInvocationBuilder(path)
                    )
            );
        }
        catch (Exception e) { e.printStackTrace(); e.toString(); }











        System.out.println("--------------------------------------------------------");
        System.out.println("Authentication Change Password Server test (POST)");
        System.out.println("--------------------------------------------------------");

        path = "/Authentication/Change_password";
        System.out.println("Trying POST at " + path + " (Change_password resource)");
        System.out.println("CURL call: curl http://127.0.0.1:5000/Authentication/Change_password -d '{\"email\":\"inigo.lopezgazpio@deusto.es\", \"password\":\"XXX\", \"password_new\":\"XXX\"}' -X PUT -H \"Content-Type: application/json\" -v");

        try {
            client.simplePrint(
                    client.makePutRequest(
                            client.createInvocationBuilder(path), new A_User(null, null, "inigo.lopezgazpio@deusto.es", String.valueOf(password), "XXX")
                    )
            );
        }
        catch (Exception e) { e.printStackTrace(); e.toString(); }









        System.out.println("-------------------------------------------------------");
        System.out.println("Authentication NEW Login Server test (POST)");
        System.out.println("-------------------------------------------------------");

        path = "/Authentication/Log_in";
        System.out.println("Trying POST at " + path + " (Log in service)");


        boolean operation_result = false;

        try {
            String new_login_response =
                    client.makePostRequest(
                            client.createInvocationBuilder(path) , new A_User("inigo.lopezgazpio@deusto.es", "XXX")

                    ).readEntity(String.class);

            JSONParser myParser = new JSONParser();
            JSONObject myJsonObject = (JSONObject) myParser.parse(new_login_response);
            operation_result = (boolean) myJsonObject.get("Result");
        }
        catch (Exception e) { e.printStackTrace(); e.toString(); }

        System.out.println("Attempt of trying to log_in with changed passwd for user is: " + operation_result);











        System.out.println("--------------------------------------------------------");
        System.out.println("Authentication Delete_user Server test (GET)");
        System.out.println("--------------------------------------------------------");

        path = "/Authentication/Delete_user";
        System.out.println("Trying GET at " + path + " (Delete user test message)");
        System.out.println("CURL call: curl http://127.0.0.1:5000/Authentication/Delete_user");

        try {
            client.simplePrint(
                    client.makeGetRequest(
                            client.createInvocationBuilder(path)
                    )
            );
        }
        catch (Exception e) { e.printStackTrace(); e.toString(); }











        System.out.println("--------------------------------------------------------");
        System.out.println("Authentication Delete_user Server test (POST)");
        System.out.println("--------------------------------------------------------");

        path = "/Authentication/Delete_user";
        System.out.println("Trying POST at " + path + " (delete user resource)");
        System.out.println("CURL call: curl http://127.0.0.1:5000/Authentication/Delete_user -d '{\"email\":\"inigo.lopezgazpio@deusto.es\", \"password\":\"XXX\" }' -X DELETE -H \"Content-Type: application/json\" -v");

        try {
            client.simplePrint(
                    client.makePutRequest(
                            client.createInvocationBuilder(path), new A_User("inigo.lopezgazpio@deusto.es", "XXX")
                    )
            );
        }
        catch (Exception e) { e.printStackTrace(); e.toString(); }
    }
}
