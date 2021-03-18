package Others;
import java.beans.PropertyChangeEvent;
import java.beans.PropertyChangeListener;
import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.Executors;
import java.util.concurrent.ThreadPoolExecutor;

import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpServer;

import Controllers.LampBrandXController;
import Objects.LampBrandX;
import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class Run extends Application  {
	
	static LampBrandX lamp = LampBrandX.getInstance();


	
	public void start (Stage primaryStage) throws Exception {
		Stage secStage = new Stage();
		
		Parent root = FXMLLoader.load(getClass().getResource("LampBrandX.fxml"));
		primaryStage.setTitle("lamp1");
		primaryStage.setScene(new Scene(root,600,400));
		primaryStage.show();
	}
	
	public static void main(String[] args) {
		System.out.print("Running");
		try {
			ThreadPoolExecutor threadPoolExecutor = (ThreadPoolExecutor)Executors.newFixedThreadPool(10);
			HttpServer server = HttpServer.create(new InetSocketAddress("localhost", 8001), 0);
			server.createContext("/getstatus", new getHandler());
			server.createContext("/setstatus", new setHandler());
			server.setExecutor(threadPoolExecutor);
			server.start();
			
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		

        launch(args);
	}
	
	static class getHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange t) throws IOException {
            String response = lamp.getState() + "";
            t.sendResponseHeaders(200, response.length());
            OutputStream os = t.getResponseBody();
            os.write(response.getBytes());
            os.close();
        }
    }
	
	static class setHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange t) throws IOException {
        	lamp.setState();
            String response = "OK";
            t.sendResponseHeaders(200, response.length());
            OutputStream os = t.getResponseBody();
            os.write(response.getBytes());
            os.close();
        	Map<String, String> params = queryToMap(t.getRequestURI().getQuery());         	
        }
    }
	
	public static Map<String, String> queryToMap(String query) {
	    Map<String, String> result = new HashMap<>();
	    for (String param : query.split("&")) {
	        String[] entry = param.split("=");
	        if (entry.length > 1) {
	            result.put(entry[0], entry[1]);
	        }else{
	            result.put(entry[0], "");
	        }
	    }
	    return result;
	}
	
	
}
