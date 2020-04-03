package Demo;

import MarshallingClasses.Auth_MicroService.Flight_JSON;
import MicroserviceDataFormat.Airlines_MicroService.Flight_parameters;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import restClient.RestClient;


import javax.ws.rs.core.Response;
import java.util.List;
import java.util.stream.Collectors;

public class Jersey_Airlines_Client_Requests
{

    // mvn clean compile exec:java -PJersey_Airlines_Client_Requests
    public static void main (String [] args)
    {

        // Some requests to the microservices... check the microservices are online previously with curl! check the docs for this

        System.out.println("-------------------------------------------------------");
        System.out.println("Airlines Server test (GET) ");
        System.out.println("-------------------------------------------------------");

        String path = "/";
        System.out.println("Trying GET at " + path + " (Test message)");
        System.out.println("CURL call: curl http://127.0.0.1:5002/");

        // Note below we instantiate a RestClient generic class to be used with Flight_parameters class
        RestClient<Flight_parameters> client = new RestClient<Flight_parameters>(args[0], args[1]);

        try {
            client.simplePrint(
                    client.makeGetRequest(
                            client.createInvocationBuilder(path)
                    )
            );
        }
        catch (Exception e) { e.printStackTrace(); e.toString(); }








        System.out.println("-------------------------------------------------------");
        System.out.println("Search flights Airlines Server test (GET) ");
        System.out.println("-------------------------------------------------------");

        path = "/Airlines/Search_Flights";
        System.out.println("Trying GET at " + path + " (Test message)");
        System.out.println("CURL call: curl http://127.0.0.1:5000/Airlines/Search_Flights");

        try {
            client.simplePrint(
                    client.makeGetRequest(
                            client.createInvocationBuilder(path)
                    )
            );
        }
        catch (Exception e) { e.printStackTrace(); e.toString(); }






        System.out.println("-------------------------------------------------------");
        System.out.println("Search flights Airlines Server test (POST) ");
        System.out.println("-------------------------------------------------------");

        path = "/Airlines/Search_Flights";
        System.out.println("Trying POST at " + path + " (Search All Flights message)");
        System.out.println("CURL call: curl http://127.0.0.1:5000/Airlines/Search_Flights -d '{ }' -X POST -H \"Content-Type: application/json\" -v");

        try {
            client.simplePrint(
                    client.makePostRequest(
                            client.createInvocationBuilder(path) , new Flight_parameters()
                    )
            );
        }
        catch (Exception e) { e.printStackTrace(); e.toString(); }

        System.out.println("We obtain the flights array... ok... but parsing this as a String can be a real pain in the ass...");
        System.out.println("We'll use JSONArray and JSONObject classes to easily and happily parse all the hard stuff :) ");





        System.out.println("------------------------------------------------------");
        System.out.println("Search flights Airlines Server test (POST) ");
        System.out.println("------------------------------------------------------");

        path = "/Airlines/Search_Flights";
        System.out.println("Trying POST at " + path + " (Search All Flights message)");
        System.out.println("CURL call: curl http://127.0.0.1:5000/Airlines/Search_Flights -d '{ }' -X POST -H \"Content-Type: application/json\" -v");

        Response response = null;
        try {
            response =
                    client.makePostRequest(
                            client.createInvocationBuilder(path) , new Flight_parameters()
                    );
        }
        catch (Exception e) { e.printStackTrace(); e.toString(); }


        // JSON SIMPLE PARSER STUFF...
        List<Flight_JSON> myFlightArray;
        try
        {
            String json_string = response.readEntity(String.class);
            JSONParser myParser = new JSONParser();
            JSONArray flightsArray = (JSONArray) myParser.parse( json_string );

            // Lambda expression to print array
            flightsArray.stream().forEach(
                    element -> System.out.println(element)
            );

            // Lambda expression to map JSONObjects inside JSONArray to flight objects
            myFlightArray = (List) flightsArray.stream()
                    .map( element -> new Flight_JSON( element))
                    .collect(Collectors.toList()
            );

            System.out.println("Number of flights collected:");
            System.out.println(myFlightArray.size());

            System.out.println("Print some flight as string");
            myFlightArray.get(0).print();

            System.out.println("Print some random flight parameters");
            System.out.println( myFlightArray.get(0).getAirportArrivalCity() );
            System.out.println( myFlightArray.get(0).getAirportArrivalCode() );
            System.out.println( myFlightArray.get(0).getAirportDepartureCity() );
            System.out.println( myFlightArray.get(0).getAirportDepartureCode() );
            System.out.println( myFlightArray.get(0).getCode() );
            System.out.println( myFlightArray.get(0).getDepartureDate() );
            System.out.println( myFlightArray.get(0).getDepartureDate( true) );
            System.out.println( myFlightArray.get(0).getDepartureDate( false) );
            System.out.println( myFlightArray.get(0).getFreeSeats());
            System.out.println( myFlightArray.get(0).getTotalSeats());
            System.out.println( myFlightArray.get(0).getPrice());

        } catch (Exception e) { e.printStackTrace(); e.toString(); }











        System.out.println("-------------------------------------------------------");
        System.out.println("Search flights Airlines Server test (POST) ");
        System.out.println("-------------------------------------------------------");

        path = "/Airlines/Search_Flights";
        System.out.println("Trying POST at " + path + " (Search All Flights message)");
        System.out.println("CURL call: curl http://127.0.0.1:5000/Airlines/Search_Flights -d '{\"airport_departure_name\":\"Tabarnia\", \"airport_arrival_name\":\"Donostia\" }' -X POST -H \"Content-Type: application/json\" -v");

        System.out.println("Search flights providing origin and destination");

        try {
            client.simplePrint(
                    client.makePostRequest(
                            client.createInvocationBuilder(path) , new Flight_parameters("Tabarnia","Donostia")
                    )
            );
        }
        catch (Exception e) { e.printStackTrace(); e.toString(); }












        System.out.println("-------------------------------------------------------");
        System.out.println("Search flights Airlines Server test (POST) ");
        System.out.println("-------------------------------------------------------");

        path = "/Airlines/Search_Flights";
        System.out.println("Trying POST at " + path + " (Search All Flights message)");
        System.out.println("CURL call: curl http://127.0.0.1:5000/Airlines/Search_Flights -d '{\"airport_departure_name\":\"Hondarribia\", \"airport_arrival_name\":\"Tabarnia\", \"free_seats\":\"100\" }' -X POST -H \"Content-Type: application/json\" -v");

        System.out.println("Search flights providing origin, destination and free seats available (at least X)");

        try {
            client.simplePrint(
                    client.makePostRequest(
                            client.createInvocationBuilder(path) , new Flight_parameters("Tabarnia","Donostia", 100)
                    )
            );
        }
        catch (Exception e) { e.printStackTrace(); e.toString(); }












        System.out.println("-------------------------------------------------------");
        System.out.println("Search flights Airlines Server test (POST) ");
        System.out.println("-------------------------------------------------------");

        path = "/Airlines/Search_Flights";
        System.out.println("Trying POST at " + path + " (Search All Flights message)");
        System.out.println("CURL call: curl http://127.0.0.1:5000/Airlines/Search_Flights -d '{\"airport_departure_name\":\"Hondarribia\", \"airport_arrival_name\":\"Tabarnia\", \"free_seats\":\"100\", \"price\":\"700\" }' -X POST -H \"Content-Type: application/json\" -v");

        System.out.println("Search flights providing origin, destination, free seats available (at least X) and maximum price");

        try {
            client.simplePrint(
                    client.makePostRequest(
                            client.createInvocationBuilder(path) , new Flight_parameters("Tabarnia","Donostia", 100, 370)
                    )
            );
        }
        catch (Exception e) { e.printStackTrace(); e.toString(); }









        System.out.println("-------------------------------------------------------");
        System.out.println("Search flights Airlines Server test (POST) ");
        System.out.println("-------------------------------------------------------");

        path = "/Airlines/Search_Flights";
        System.out.println("Trying POST at " + path + " (Search All Flights message)");
        System.out.println("CURL call: curl http://127.0.0.1:5000/Airlines/Search_Flights -d '{\"airport_departure_name\":\"Hondarribia\", \"airport_arrival_name\":\"Tabarnia\", \"free_seats\":\"100\", \"price\":\"700\", \"departure_date\":\"2020/04/03 09:00:00\" }' -X POST -H \"Content-Type: application/json\" -v");

        System.out.println("Search flights providing origin, destination, free seats available, maximum price and also Search flights also by proximity to departure date (between given date and given date + 10 days)");

        try {
            client.simplePrint(
                    client.makePostRequest(
                            client.createInvocationBuilder(path) , new Flight_parameters("Tabarnia","Donostia", 100, 370, "2020/04/10 09:00:00")
                    )
            );
        }
        catch (Exception e) { e.printStackTrace(); e.toString(); }

    }
}
